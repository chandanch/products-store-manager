from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    CheckConstraint,
    UniqueConstraint,
)

from app.settings.db_connection import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(100), nullable=False)
    slug = Column(String(140), nullable=False)
    is_active = Column(Boolean, nullable=False, default=False, server_default="False")
    level = Column(Integer, nullable=False, default="100", server_default="100")
    parent_id = Column(Integer, nullable=True)

    __tableargs__ = (
        CheckConstraint("LENGTH(name) > 0", name="name_length_constraint"),
        CheckConstraint("LENGTH(slug) > 0", name="slugh_length_constraint"),
        UniqueConstraint("name", "level", name="unq_category_name_level_constraint"),
        UniqueConstraint("slug", name="unq_category_slug_constraint"),
    )
