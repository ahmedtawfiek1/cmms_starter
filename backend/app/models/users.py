from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean
from app.db.base import Base
import uuid
def gen_uuid():
    return str(uuid.uuid4())
class User(Base):
    __tablename__ = "users"
    id: Mapped[str] = mapped_column(primary_key=True, default=gen_uuid)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String)
    full_name: Mapped[str] = mapped_column(String, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)