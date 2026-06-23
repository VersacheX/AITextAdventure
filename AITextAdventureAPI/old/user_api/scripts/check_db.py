"""Quick DB inspection script for local development.
Run: python -m user_api.scripts.check_db (from AITextAdventureAPI/old)
"""
import os
import json
from sqlalchemy import inspect

# load env if available
try:
 from dotenv import load_dotenv
 load_dotenv(os.path.join(os.path.dirname(__file__), '..', '..', '.env'))
except Exception:
 pass

from user_api.services.auth_service import DATABASE_URL, engine, SessionLocal
from user_api.models.auth_models import User, Save


def main():
 print(f"Using DATABASE_URL={DATABASE_URL}")
 try:
  conn = engine.connect()
  conn.close()
 except Exception as e:
  print("Failed to connect to DB:", e)
  return

 inspector = inspect(engine)
 print("Tables:", inspector.get_table_names())

 db = SessionLocal()
 try:
  users = db.query(User).limit(10).all()
  print(f"Users ({len(users)}):")
  for u in users:
   print(f" - id={u.id} username={u.username} created_at={u.created_at} password_hash={getattr(u, 'password_hash', None)}")

  saves = db.query(Save).limit(10).all()
  print(f"Saves ({len(saves)}):")
  for s in saves:
   print(f" - id={s.id} user_id={s.user_id} name={s.name} created_at={s.created_at}")
 except Exception as e:
  print("Query failed:", e)
 finally:
  db.close()


if __name__ == '__main__':
 main()
