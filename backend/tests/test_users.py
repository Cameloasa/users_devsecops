import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent)) 

from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_get_all_users():
    response = client.get("/api/users")
    assert response.status_code == 200

    users = response.json()
    assert isinstance(users,list)
    assert len(users) == 4
    
    