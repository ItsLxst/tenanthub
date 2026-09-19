from sqlalchemy import Integer, String, Text, TIMESTAMP, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
from datetime import datetime

class Base(DeclarativeBase):
    pass

class Organization(Base):
    __tablename__ = "organizations"

    organization_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP)
    updated_at: Mapped[datetime] = mapped_column(TIMESTAMP)

class User(Base):
    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    first_name: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100))
    status: Mapped[str] = mapped_column(String(20))
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP)
    updated_at: Mapped[datetime] = mapped_column(TIMESTAMP)

class Membership(Base):
    __tablename__ = "memberships"

    membership_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    organization_id: Mapped[int] = mapped_column(ForeignKey("organizations.organization_id"), nullable=False)
    organization : Mapped["Organization"] = relationship()

    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"), nullable=False)
    user : Mapped["User"] = relationship()

    role: Mapped[str] = mapped_column(String(50), nullable=False)
    invited_at: Mapped[datetime] = mapped_column(TIMESTAMP)
    joined_at: Mapped[datetime] = mapped_column(TIMESTAMP)
    left_at: Mapped[datetime] = mapped_column(TIMESTAMP)
    status: Mapped[str] = mapped_column(String(20))
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP)
    updated_at: Mapped[datetime] = mapped_column(TIMESTAMP)