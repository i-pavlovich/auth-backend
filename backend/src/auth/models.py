from typing import Optional
from datetime import datetime
from sqlalchemy import String, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(55), unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]

    name: Mapped[Optional[str]] = mapped_column(String(35))
    surname: Mapped[Optional[str]] = mapped_column(String(35))

    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    is_active: Mapped[bool] = mapped_column(server_default="true")
    is_admin: Mapped[bool] = mapped_column(server_default="false")
    is_verified: Mapped[bool] = mapped_column(server_default="false")


class RefreshToken(Base):
    __tablename__ = "refresh_tokens"

    id: Mapped[int] = mapped_column(primary_key=True)
    refresh_token: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))

    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    expires_at: Mapped[datetime]
    updated_at: Mapped[Optional[datetime]] = mapped_column(onupdate=func.now())

    is_banned: Mapped[bool] = mapped_column(server_default="false")
