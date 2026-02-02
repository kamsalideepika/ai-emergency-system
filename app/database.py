from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Database URL (SQLite file will be created automatically)
DATABASE_URL = "sqlite:///./emergency.db"

# Engine connects Python to database
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# SessionLocal helps us interact with DB
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base is parent class for all models
Base = declarative_base()
