from fastapi import FastAPI
from fastapi.responses import FileResponse
from app.api import router
import os

app = FastAPI(title="Company Summarizer API")

# Serve the openapi.json file
@app.get("/.well-known/openapi.json", include_in_schema=False)
def serve_openapi():
    # Assuming the openapi.json is in the same directory as main.py
    return FileResponse("openapi.json", media_type="application/json")

# Include the router
app.include_router(router)
