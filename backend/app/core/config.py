from pydantic import BaseModel
import os
class Settings(BaseModel):
    SQLALCHEMY_DATABASE_URI: str = os.getenv("DATABASE_URL", "postgresql+psycopg2://app:secret@localhost:5432/cmms")
    JWT_SECRET: str = os.getenv("JWT_SECRET", "change-me")
    JWT_ALG: str = os.getenv("JWT_ALG", "HS256")
settings = Settings()