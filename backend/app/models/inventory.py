from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Numeric, Integer
from app.db.base import Base
import uuid
def gen_uuid():
    return str(uuid.uuid4())
class InventoryItem(Base):
    __tablename__ = "inventory_items"
    id: Mapped[str] = mapped_column(primary_key=True, default=gen_uuid)
    sku: Mapped[str] = mapped_column(String, unique=True, index=True)
    name: Mapped[str] = mapped_column(String)
    unit: Mapped[str] = mapped_column(String, default="pcs")
    cost: Mapped[float] = mapped_column(Numeric(12,2), default=0)
    price: Mapped[float] = mapped_column(Numeric(12,2), default=0)
    reorder_level: Mapped[int] = mapped_column(Integer, default=0)