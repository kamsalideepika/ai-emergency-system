from fastapi import FastAPI

from app.routes.prediction_routes import router as prediction_router
from app.routes.hotspot_routes import router as hotspot_router
from app.dashboard.dashboard_routes import router as dashboard_router

app = FastAPI(title="AI Emergency Pressure System")

@app.get("/")
def root():
    return {"message": "Phase 2 Running Successfully ✅"}

# Include all routes
app.include_router(prediction_router)
app.include_router(hotspot_router)
app.include_router(dashboard_router)
