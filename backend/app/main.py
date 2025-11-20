import json
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from typing import Optional
from pathlib import Path
from fastapi.staticfiles import StaticFiles



# Create FastAPI app instance
app = FastAPI(
    title="DevSecOps Python+FastAPI",
    description="A simple fast API backend for CI/CD",
    version="1.0"
)

# --------------------------
# Health check endpoint
# --------------------------
@app.get("/api/health")
def health_check():
    """
    This endpoint returns the health status of the application.
    It is used by the frontend to check if the backend is running.
    """
    return {
        "status": "ok",
        "service": "FastAPI backend",
        "version": "1.0"
    }

# --------------------------
# Users endpoint GET
# --------------------------
@app.get("/api/users")
def get_users():
    """
    This endpoint returns the list of users stored in data/users.json.
    1. The file path is constructed relative to the current script using pathlib.
    2. The file is opened and loaded using json.load.
    3. If any error occurs (file missing or invalid JSON), return HTTP 500.
    """
    id: Optional[int] = Query(None),
    name: Optional[str] = Query(None),
    email: Optional[str] = Query(None),
    age: Optional[int] = Query(None),
    role: Optional[str] = Query(None),
    
    try:
        # Construct the absolute path to the users.json file
        data_file = Path("data/users.json").resolve()


        # Open and load the JSON data
        with open(data_file, "r", encoding="utf-8") as f:
            users = json.load(f)

        # Apply filters
        # Apply filters
        if id is not None:
            users = [u for u in users if u["id"] == id]

        if name is not None:
            users = [u for u in users if u["name"].lower() == name.lower()]

        if email is not None:
            users = [u for u in users if u["email"].lower() == email.lower()]

        if age is not None:
            users = [u for u in users if u["age"] == age]

        if role is not None:
            users = [u for u in users if u["role"].lower() == role.lower()]


        # Return JSON response
        return JSONResponse(content=users)

    except Exception as e:
        # Return error if file not found or invalid JSON
        return JSONResponse(
            status_code=500,
            content={"error": "Failed to load users and filter users", "details": str(e)}
        )
    
# --------------------------
# Serve frontend files
# --------------------------
app.mount("/", StaticFiles(directory="frontend/public", html=True), name="frontend")