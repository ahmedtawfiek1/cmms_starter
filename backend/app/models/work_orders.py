from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime, Text
from app.db.base import Base
import uuid, datetime
def gen_uuid():
    return str(uuid.uuid4())
class WorkOrder(Base):
    __tablename__ = "work_orders"
    id: Mapped[str] = mapped_column(primary_key=True, default=gen_uuid)
    wo_number: Mapped[str] = mapped_column(String, unique=True, index=True)
    status: Mapped[str] = mapped_column(String, default="open")
    priority: Mapped[str] = mapped_column(String, default="medium")
    description: Mapped[str] = mapped_column(Text, nullable=True)
    opened_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=datetime.datetime.utcnow)
    closed_at: Mapped[datetime.datetime | None] = mapped_column(DateTime, nullable=True)