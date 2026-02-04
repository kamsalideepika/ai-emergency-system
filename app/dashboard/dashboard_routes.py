from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/dashboard", response_class=HTMLResponse)
def dashboard():
    return """
    <html>
        <head>
            <title>Emergency Dashboard</title>
        </head>
        <body>
            <h2>🚑 AI Emergency Pressure Dashboard</h2>
            <p>Phase 2 Functional Dashboard MVP</p>
            <p>Status: ✅ Server Running | Phase 3 Ready</p>

            <ul>
                <li><a href="/docs">API Documentation</a></li>
                <li><a href="/predict-pressure?accidents=10&ambulance_load=5">
                    Test Pressure Prediction</a></li>
                <li><a href="/hotspots">Hotspot Zones</a></li>
            </ul>
        </body>
    </html>
    """
