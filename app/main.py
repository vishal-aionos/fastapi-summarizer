from fastapi import FastAPI
from app.api import router

app = FastAPI(title="Company Summarizer API")
app.include_router(router)
