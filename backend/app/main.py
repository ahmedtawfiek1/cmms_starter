from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from app.db.session import engine
from app.db.base import Base
from app.api.v1.inventory import router as inventory_router
app = FastAPI(title="CMMS API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)
app.include_router(inventory_router)
@app.get("/health")
def health():
    with engine.connect() as conn:
        conn.execute(text("select 1"))
    return {"status": "ok"}