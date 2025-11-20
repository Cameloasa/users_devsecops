import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent)) 

from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

# ----------------------
# POZITIVE TESTS
# ----------------------
def test_get_all_users():
    response = client.get("/api/users")
    assert response.status_code == 200

    users = response.json()
    assert isinstance(users,list)
    assert len(users) == 4

def test_get_user_by_id():
    response = client.get("/api/users", params={"id": 1})
    assert response.status_code == 200

    users = response.json()
    assert len(users) == 1
    assert users[0]["name"] == "John Doe"

    