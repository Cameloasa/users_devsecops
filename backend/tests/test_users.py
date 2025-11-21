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

def test_get_user_by_role():
    response = client.get("/api/users", params={"role": "user"})
    assert response.status_code == 200

    users = response.json()
    assert all(u["role"].lower() == "user" for u in users)

def test_get_user_by_email():
    response = client.get("/api/users", params={"email": "alice.brown@example.com"})
    assert response.status_code == 200

    users = response.json()
    assert len(users) == 1
    assert users[0]["name"] == "Alice Brown"

# ----------------------
# NEGATIVE TESTS / EDGE CASES
# ----------------------
def test_get_user_nonexistent_id():
    response = client.get("/api/users", params={"user_id": 999})
    assert response.status_code == 200

    users = response.json()
    assert users == []

def test_get_user_nonexistent_role():
    response = client.get("/api/users", params={"role": "ghost"})
    assert response.status_code == 200

    users = response.json()
    assert users == []

def test_get_user_nonexistent_email():
    response = client.get("/api/users", params={"email": "nonexistent@example.com"})
    assert response.status_code == 200

    users = response.json()
    assert users == []

def test_get_user_combination_filters():
    response = client.get("/api/users", params={"role": "admin", "age": 30})
    assert response.status_code == 200

    users = response.json()
    assert len(users) == 1
    assert users[0]["name"] == "John Doe"

    