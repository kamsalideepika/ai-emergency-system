from fastapi import FastAPI
from app.database import Base, engine

# Import models (so tables are created)
from app.models.hospital import Hospital
from app.models.accident import Accident
from app.models.ambulance_log import AmbulanceArrival

# Import routes
from app.routes.prediction_routes import router as prediction_router
from app.routes.hotspot_routes import router as hotspot_router

# Create all tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(title="AI Emergency Pressure Prediction MVP")

# Include prediction routes
app.include_router(prediction_router)
app.include_router(hotspot_router)

@app.get("/")
def home():
    return {"message": "Phase 1 MVP Running Successfully ✅"}
