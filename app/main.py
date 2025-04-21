from fastapi import FastAPI
from fastapi.responses import FileResponse
import os
from app.api import router

app = FastAPI(title="Company Summarizer API")

# Serve openapi.json at the standard GPT location
@app.get("/.well-known/openapi.json", include_in_schema=False)
def serve_openapi_spec():
    return FileResponse(os.path.join(os.getcwd(), "openapi.json"), media_type="application/json")

# Include your main API router
app.include_router(router)
