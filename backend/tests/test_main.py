# 1. Third-party libraries
from fastapi.testclient import TestClient

# 2. Local imports
from backend.app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["service"] == "FastAPI backend"
