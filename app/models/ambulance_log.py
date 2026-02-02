from sqlalchemy import Column, Integer, String
from app.database import Base

# Ambulance arrival table model
class AmbulanceArrival(Base):
    __tablename__ = "ambulance_arrivals"

    id = Column(Integer, primary_key=True, index=True)
    hospital_zone = Column(String, nullable=False)
    arrival_count = Column(Integer, default=1)
