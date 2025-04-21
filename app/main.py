from fastapi import FastAPI
from fastapi.responses import FileResponse
import os
from app.api import router

app = FastAPI(title="Company Summarizer API")

# Serves openapi.json from the app folder
@app.get("/.well-known/openapi.json", include_in_schema=False)
def serve_openapi():
    file_path = os.path.join(os.path.dirname(__file__), "openapi.json")
    return FileResponse(file_path, media_type="application/json")

# Include your API router
app.include_router(router)
