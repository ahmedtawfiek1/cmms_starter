from app.db.session import SessionLocal
from app.models.inventory import InventoryItem
def run():
    db = SessionLocal()
    items = [
        ("SKU-001","AA Batteries 4-Pack","pack",20,35,10),
        ("SKU-002","USB-C Cable 1m","pcs",30,60,15),
        ("SKU-003","LED Bulb 9W","pcs",15,40,25),
    ]
    for sku,name,unit,cost,price,rl in items:
        if not db.query(InventoryItem).filter_by(sku=sku).first():
            db.add(InventoryItem(sku=sku,name=name,unit=unit,cost=cost,price=price,reorder_level=rl))
    db.commit(); db.close()
if __name__ == "__main__":
    run()