from fastapi import FastAPI
from app.api import router
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI(title="Company Summarizer API")

# Include API routes
app.include_router(router)

# Serve static OpenAPI schema
app.mount(
    "/.well-known",
    StaticFiles(directory=os.path.join("static", ".well-known")),
    name="well-known",
)
