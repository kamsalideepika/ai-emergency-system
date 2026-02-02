from sqlalchemy import Column, Integer, String
from app.database import Base

# Accident table model
class Accident(Base):
    __tablename__ = "accidents"

    id = Column(Integer, primary_key=True, index=True)
    location = Column(String, nullable=False)
    zone = Column(String, nullable=False)
    severity = Column(Integer, default=1)
