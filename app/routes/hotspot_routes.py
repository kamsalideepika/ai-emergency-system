from fastapi import APIRouter
from app.services.hotspot_service import find_hotspots

router = APIRouter()

# Sample accident zone data (Phase 1 MVP)
sample_accident_data = [
    "Zone-A", "Zone-B", "Zone-A",
    "Zone-C", "Zone-A", "Zone-B",
    "Zone-D", "Zone-B"
]

@router.get("/hotspots")
def get_hotspots():
    hotspots = find_hotspots(sample_accident_data)

    return {
        "message": "Accident Hotspot Zones Identified",
        "hotspots": hotspots
    }
