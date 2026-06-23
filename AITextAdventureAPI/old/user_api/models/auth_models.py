from datetime import datetime
from typing import Any, Dict, Optional
import json

from pydantic import BaseModel, Field
# support pydantic v2 ConfigDict when available
from pydantic import ConfigDict

# Optional: SQLAlchemy ORM models for persistence. Import only if DB layer is used.
from sqlalchemy import (
	Column,
	Integer,
	String,
	DateTime,
	Text,
	Boolean,
	ForeignKey,
	func,
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# -------------------------
# Pydantic API Schemas
# -------------------------


class UserCreate(BaseModel):
	username: str = Field(..., min_length=3, max_length=64)
	password: str = Field(..., min_length=6)


class UserRead(BaseModel):
	id: int
	username: str
	created_at: datetime

	# pydantic v2 compatibility
	if ConfigDict is not None:
		model_config = ConfigDict(from_attributes=True)
	else:
		class Config:
			orm_mode = True


class Token(BaseModel):
	access_token: str
	token_type: str = "bearer"
	refresh_token: Optional[str] = None


class TokenPayload(BaseModel):
	sub: Optional[str] = None
	exp: Optional[int] = None


class SaveCreate(BaseModel):
	name: str = Field(..., min_length=1, max_length=128)
	main_character: str = Field(..., description="Name of the main character in the save")
	level: int = Field(..., ge=1, description="Current level of the player in the save")
	money: int = Field(..., ge=0, description="Amount of money the player has in the save")
	blob: str = Field(..., description="Serialized player_game content (JSON-serializable)")
	schema_version: Optional[int] = Field(1, description="Schema version of the saved blob")
	metadata: Optional[Dict[str, Any]] = None


class SaveSummary(BaseModel):
	id: int
	name: str
	main_character: Optional[str] = None
	level: Optional[int] = None
	money: Optional[int] = None
	updated_at: Optional[datetime] = None

	if ConfigDict is not None:
		model_config = ConfigDict(from_attributes=True)
	else:
		class Config:
			orm_mode = True


class SaveRead(BaseModel):
	id: int
	user_id: int
	name: str
	schema_version: int
	metadata: Optional[Dict[str, Any]] = None
	created_at: datetime
	updated_at: datetime
	# surfaced convenience fields
	main_character: str = None
	level: Optional[int] = None
	money: Optional[int] = None

	if ConfigDict is not None:
		model_config = ConfigDict(from_attributes=True)
	else:
		class Config:
			orm_mode = True


# -------------------------
# SQLAlchemy ORM models
# -------------------------
if Base is not object:

	class User(Base):
		__tablename__ = "users"

		id = Column(Integer, primary_key=True, autoincrement=True)
		username = Column(String(64), unique=True, nullable=False, index=True)
		password_hash = Column(String(256), nullable=False)
		created_at = Column(DateTime, server_default=func.now())

		def to_dict(self) -> Dict[str, Any]:
			return {"id": self.id, "username": self.username, "created_at": self.created_at}


	class RefreshToken(Base):
		__tablename__ = "refresh_tokens"

		id = Column(Integer, primary_key=True, autoincrement=True)
		user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
		token_hash = Column(String(256), nullable=False)
		expires_at = Column(DateTime, nullable=True)
		revoked = Column(Boolean, nullable=False, default=False)


	class Save(Base):
		__tablename__ = "saves"

		id = Column(Integer, primary_key=True, autoincrement=True)
		user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
		name = Column(String(128), nullable=False)
		# store JSON as text for broad DB compatibility
		blob = Column(Text, nullable=False)

		schema_version = Column(Integer, nullable=False, default=1)
		# rename attribute to metadata_json to avoid conflict with Declarative 'metadata'
		metadata_json = Column('metadata', Text, nullable=True)

		# Added fields for quick indexing and filtering
		main_character = Column(String(128), nullable=True, default=None)
		level = Column(Integer, nullable=True, default=None)
		money = Column(Integer, nullable=True, default=0)

		created_at = Column(DateTime, server_default=func.now())
		updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

		def to_summary(self) -> Dict[str, Any]:
			return {
				"id": self.id,
				"user_id": self.user_id,
				"name": self.name,
				"blob": self.blob,
				"schema_version": self.schema_version,
				"metadata": None,
				"main_character": self.main_character,
				"level": self.level,
				"money": self.money,
				"created_at": self.created_at,
				"updated_at": self.updated_at,
			}
