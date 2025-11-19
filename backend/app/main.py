import json
from fastapi import FastAPI
from fastapi.responses import JSONResponse
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
# Users endpoint
# --------------------------
@app.get("/api/users")
def get_users():
    """
    This endpoint returns the list of users stored in data/users.json.
    1. The file path is constructed relative to the current script using pathlib.
    2. The file is opened and loaded using json.load.
    3. If any error occurs (file missing or invalid JSON), return HTTP 500.
    """
    try:
        # Construct the absolute path to the users.json file
        data_file = Path("data/users.json").resolve()


        # Open and load the JSON data
        with open(data_file, "r", encoding="utf-8") as f:
            users = json.load(f)

        # Return JSON response
        return JSONResponse(content=users)

    except Exception as e:
        # Return error if file not found or invalid JSON
        return JSONResponse(
            status_code=500,
            content={"error": "Failed to load users", "details": str(e)}
        )
    
# --------------------------
# Serve frontend files
# --------------------------
app.mount("/", StaticFiles(directory="frontend/public", html=True), name="frontend")