from sqlalchemy import Column, Integer, String
from app.database import Base

# Hospital table model
class Hospital(Base):
    __tablename__ = "hospitals"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    zone = Column(String, nullable=False)
    capacity = Column(Integer, default=50)
