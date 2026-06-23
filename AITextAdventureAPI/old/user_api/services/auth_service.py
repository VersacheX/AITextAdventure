import os
import json
import logging
from datetime import datetime, timedelta, timezone
from typing import Optional, Dict, Any, Generator, List

from jose import jwt
from jose.exceptions import JWTError, ExpiredSignatureError
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker, Session

from argon2 import PasswordHasher, exceptions as argon2_exceptions

from user_api.models.auth_models import User, Save, RefreshToken, Base, UserCreate, SaveCreate

# set up logging
logger = logging.getLogger(__name__)
if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

# Configuration via env
DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///AITextAdventure_Old.db')
# Password pepper / secret used when hashing (optional)
PASSWORD_PEPPER = os.environ.get('SECRET_KEY') or os.environ.get('AI_APP_SECRET') or ''
# JWT signing secret (use this for tokens)
JWT_SECRET = os.environ.get('JWT_SECRET') or os.environ.get('AI_APP_SECRET') or 'change_this_jwt_secret'
ALGORITHM = os.environ.get('ALGORITHM', 'HS256')
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get('ACCESS_TOKEN_EXPIRE_MINUTES', '60'))
REFRESH_TOKEN_EXPIRE_DAYS = int(os.environ.get('REFRESH_TOKEN_EXPIRE_DAYS', '30'))

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if DATABASE_URL.startswith('sqlite') else {})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

ph = PasswordHasher()

####################DB METHODS##########################
def ensure_admin_user(db: Session, username: str = 'admin', password: str = 'iamjudas') -> None:
    """Ensure an admin user exists; create if missing. Logs actions."""
    try:
        existing = db.query(User).filter(User.username == username).first()
        if existing:
            logger.info("Admin user already exists: %s (id=%s)", existing.username, getattr(existing, 'id', None))
            return
        admin_in = UserCreate(username=username, password=password)
        u = create_user(db, admin_in)
        logger.info("Created admin user: %s (id=%s)", u.username, getattr(u, 'id', None))
    except Exception as e:
        logger.exception("Failed to ensure admin user: %s", e)


# Create DB tables if missing
def init_db() -> None:
    logger.info("Initializing database: %s", DATABASE_URL)
    try:
        # test connection
        conn = engine.connect()
        conn.close()
    except Exception as e:
        logger.exception("Database connection failed: %s", e)
        raise

    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        logger.exception("Failed to create tables: %s", e)
        raise

    # report existing tables
    try:
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        logger.info("Database tables: %s", tables)
    except Exception:
        logger.exception("Failed to inspect database tables")

    # ensure admin user
    db: Session = SessionLocal()
    try:
        ensure_admin_user(db)
    finally:
        db.close()


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

######################## AUTH & USER OPS ##########################
# User operations
def _pepper_password(password: str) -> str:
    # combine password with optional pepper before hashing/verification
    if PASSWORD_PEPPER:
        return password + PASSWORD_PEPPER
    return password


def create_user(db: Session, user_in: UserCreate) -> User:
    # simple uniqueness check
    existing = db.query(User).filter(User.username == user_in.username).first()
    if existing:
        raise ValueError('username exists')
    hashed = ph.hash(_pepper_password(user_in.password))
    u = User(username=user_in.username, password_hash=hashed)
    db.add(u)
    db.commit()
    db.refresh(u)
    return u


def authenticate_user(db: Session, username: str, password: str) -> Optional[User]:
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return None
    # verify password
    try:
        ph.verify(user.password_hash, _pepper_password(password))
    except argon2_exceptions.VerifyMismatchError:
        return None
    except Exception:
        # any other argon error -> fail auth
        return None

    # optionally rehash if needed (argon2 has .check_needs_rehash)
    try:
        if ph.check_needs_rehash(user.password_hash):
            # rehash with current parameters
            user.password_hash = ph.hash(_pepper_password(password))
            db.add(user)
            db.commit()
    except Exception:
        # ignore rehash errors
        pass

    return user


# Token helpers
def create_access_token(data: Dict[str, Any], expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    now = datetime.now(timezone.utc)
    expire = now + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": int(expire.timestamp()), "iat": int(now.timestamp())})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=ALGORITHM)
    return encoded_jwt


def create_refresh_token(db: Session, user_id: int, expires_delta: Optional[timedelta] = None) -> str:
    now = datetime.now(timezone.utc)
    expire = now + (expires_delta or timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS))
    payload = {"sub": str(user_id), "exp": int(expire.timestamp()), "iat": int(now.timestamp())}
    token = jwt.encode(payload, JWT_SECRET, algorithm=ALGORITHM)
    rt = RefreshToken(user_id=user_id, token_hash=token, expires_at=expire, revoked=False)
    db.add(rt)
    db.commit()
    return token


def decode_token(token: str) -> Dict[str, Any]:
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
        return payload
    except ExpiredSignatureError as e:
        raise e
    except JWTError as e:
        raise e


######################## SAVE GAME OPS ##########################

# Save CRUD
def list_saves(db: Session, user_id: int) -> List[Dict[str, Any]]:
    """Return minimal save summaries without loading the full blob column to save memory/network.
    Fields returned: id, main_character, level, money, updated_at
    """
    # Query only the needed columns to avoid reading the large 'blob' field
    rows = (
        db.query(
            Save.id,
            Save.name,
            Save.main_character,
            Save.level,
            Save.money,
            Save.updated_at,
        )
        .filter(Save.user_id == user_id)
        .all()
    )

    out: List[Dict[str, Any]] = []
    for row in rows:
        # row is a tuple in the order requested
        rid, name, main_character, level, money, updated_at = row
        # fallback to empty string or None for main_character
        mc = main_character or None

        out.append({
            'id': rid,
            'name': name or None,
            'main_character': mc,
            'level': level,
            'money': money,
            'updated_at': updated_at,
        })

    return out

def get_save(db: Session, user_id: int, save_id: int) -> Optional[Dict[str, Any]]:
    s = db.query(Save).filter(Save.id == save_id, Save.user_id == user_id).first()
    if not s:
        return None
    
    blob = json.loads(s.blob) #if isinstance(s.blob, (str, bytes)) else s.blob

    # return explicit columns; do not include metadata contents
    return {
        "id": s.id,
        "user_id": s.user_id,
        "name": s.name,
        "schema_version": s.schema_version,
        "metadata": None,
        "blob": blob,
        "main_character": s.main_character,
        "level": s.level,
        "money": s.money,
        "updated_at": s.updated_at,
        "created_at": s.created_at,
    }


def create_save(db: Session, user_id: int, save_in: SaveCreate) -> Save:
    # serialize blob
    #blob_serialized = json.dumps(save_in.blob)

    # persist using explicit columns; do NOT use metadata_json
    s = Save(
        user_id=user_id,
        name=save_in.name,
        blob=save_in.blob,
        schema_version=save_in.schema_version,
        metadata_json=None,
        main_character=save_in.main_character,
        level=save_in.level,
        money=save_in.money,
        updated_at=datetime.now(timezone.utc),
        created_at=datetime.now(timezone.utc),
    )
    db.add(s)
    db.commit()
    db.refresh(s)
    return s

def delete_save(db: Session, user_id: int, save_id: int) -> bool:
    s = db.query(Save).filter(Save.id == save_id, Save.user_id == user_id).first()
    if not s:
        return False
    db.delete(s)
    db.commit()
    return True


def update_save(db: Session, user_id: int, save_id: int, save_in: SaveCreate) -> Optional[Save]:
    """Update an existing save belonging to user_id with new data."""
    s = db.query(Save).filter(Save.id == save_id, Save.user_id == user_id).first()
    if not s:
        return None

    s.name = save_in.name
    s.blob = save_in.blob
    s.schema_version = save_in.schema_version
    # do not use metadata_json
    s.metadata_json = None
    s.main_character = save_in.main_character
    s.level = save_in.level
    s.money = save_in.money
    s.updated_at = datetime.now(timezone.utc)
    db.add(s)
    db.commit()
    db.refresh(s)
    return s
