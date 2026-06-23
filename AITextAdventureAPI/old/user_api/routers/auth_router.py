from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.orm import Session

from user_api.models.auth_models import UserRead, Token, SaveCreate, SaveRead, SaveSummary, UserCreate
from user_api.services.auth_service import (
    get_db,
    create_user,
    authenticate_user,
    create_access_token,
    create_refresh_token,
    decode_token,
    list_saves,
    create_save,
    get_save,
    delete_save,
    init_db,
    update_save,
)

router = APIRouter(prefix="/api/auth")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/token")

# DO NOT initialize DB here at import time; init_db is called on app startup


def get_current_user_id(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)) -> int:
    try:
        payload = decode_token(token)
        sub = payload.get('sub') or payload.get('user_id')
        if not sub:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid authentication credentials')
        return int(sub)
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate credentials')


@router.post('/register', response_model=UserRead)
def api_register(user_in: UserCreate, db: Session = Depends(get_db)):
    try:
        user = create_user(db, user_in)
        return UserRead.model_validate(user) if hasattr(UserRead, 'model_validate') else UserRead.from_orm(user)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Registration failed')


@router.post('/token', response_model=Token)
def api_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Incorrect username or password')
    access_token = create_access_token({"sub": str(user.id), "user_id": user.id})
    refresh_token = create_refresh_token(db, user.id)
    return Token(access_token=access_token, token_type="bearer", refresh_token=refresh_token)


@router.post('/token/refresh', response_model=Token)
def api_refresh_token(refresh_token: str, db: Session = Depends(get_db)):
    try:
        payload = decode_token(refresh_token)
        sub = payload.get('sub')
        if not sub:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid refresh token')
        user_id = int(sub)
        # Issue new access token
        access_token = create_access_token({"sub": str(user_id), "user_id": user_id})
        return Token(access_token=access_token, token_type="bearer")
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid refresh token')



############################ SAVE GAME ENDPOINTS ############################
@router.get('/saves', response_model=List[SaveSummary])
def api_list_saves(current_user_id: int = Depends(get_current_user_id), db: Session = Depends(get_db)):
    rows = list_saves(db, current_user_id)
    # rows are minimal dicts matching SaveSummary
    return [SaveSummary.model_validate(r) if hasattr(SaveSummary, 'model_validate') else SaveSummary(**r) for r in rows]


@router.post('/saves', response_model=SaveRead)
def api_create_save(save_in: SaveCreate, current_user_id: int = Depends(get_current_user_id), db: Session = Depends(get_db)):
    s = create_save(db, current_user_id, save_in)
    return SaveRead.model_validate(s.to_summary()) if hasattr(SaveRead, 'model_validate') else SaveRead(**s.to_summary())


@router.put('/saves/{save_id}', response_model=SaveRead)
def api_update_save(save_id: int, save_in: SaveCreate, current_user_id: int = Depends(get_current_user_id), db: Session = Depends(get_db)):
    s = update_save(db, current_user_id, save_id, save_in)
    if not s:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Save not found')
    return SaveRead.model_validate(s.to_summary()) if hasattr(SaveRead, 'model_validate') else SaveRead(**s.to_summary())


@router.get('/saves/{save_id}')
def api_get_save(save_id: int, current_user_id: int = Depends(get_current_user_id), db: Session = Depends(get_db)):
    s = get_save(db, current_user_id, save_id)
    if not s:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Save not found')
    # return full save dict including 'blob' for client-side loading
    return s


@router.delete('/saves/{save_id}')
def api_delete_save(save_id: int, current_user_id: int = Depends(get_current_user_id), db: Session = Depends(get_db)):
    ok = delete_save(db, current_user_id, save_id)
    if not ok:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Save not found')
    return {"deleted": True}
