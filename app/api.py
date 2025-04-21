from fastapi import APIRouter
from app.core import process_company

router = APIRouter()

@router.get("/summarize")
def summarize(company: str):
    return process_company(company)
