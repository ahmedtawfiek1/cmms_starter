from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.inventory import InventoryItem
from app.schemas.inventory import ItemCreate, ItemOut
router = APIRouter(prefix="/inventory", tags=["inventory"])
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@router.post("/items", response_model=ItemOut)
def create_item(payload: ItemCreate, db: Session = Depends(get_db)):
    if db.query(InventoryItem).filter(InventoryItem.sku == payload.sku).first():
        raise HTTPException(status_code=400, detail="SKU exists")
    item = InventoryItem(
        sku=payload.sku, name=payload.name, unit=payload.unit,
        cost=payload.cost, price=payload.price, reorder_level=payload.reorder_level
    )
    db.add(item); db.commit(); db.refresh(item)
    return ItemOut(**{k: getattr(item, k) for k in ItemOut.model_fields.keys()})