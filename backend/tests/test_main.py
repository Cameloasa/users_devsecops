import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent)) 

from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_health ():
    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["service"] == "FastAPI backend"

def test_get_users():
    response = client.get("/api/users")
    assert response.status_code == 200
    users = response.json()
    assert isinstance(users,list)
    assert len(users) > 0
    assert "name" in users[0]