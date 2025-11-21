# 1. Standard library
import sys
from pathlib import Path

# 2. Third-party libraries
from fastapi.testclient import TestClient

# 3. Add project root to path (if really needed)
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

# 4. Local imports
from backend.app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["service"] == "FastAPI backend"
