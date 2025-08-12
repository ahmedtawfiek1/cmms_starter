from pydantic import BaseModel
class ItemCreate(BaseModel):
    sku: str
    name: str
    unit: str = "pcs"
    cost: float = 0
    price: float = 0
    reorder_level: int = 0
class ItemOut(BaseModel):
    id: str
    sku: str
    name: str
    unit: str
    cost: float
    price: float
    reorder_level: int