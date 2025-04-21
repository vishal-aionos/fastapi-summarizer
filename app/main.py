from fastapi import FastAPI
from fastapi.responses import FileResponse
import os
from app.api import router

app = FastAPI(title="Company Summarizer API")

# ✅ Route to serve the OpenAPI spec
@app.get("/.well-known/openapi.json", include_in_schema=False)
def serve_openapi():
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "openapi.json")
    return FileResponse(file_path, media_type="application/json")

# Include your actual endpoints
app.include_router(router)
