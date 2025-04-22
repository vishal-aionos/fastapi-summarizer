from fastapi import APIRouter
from app.core import process_company

router = APIRouter()

@router.get("/summarize")
def summarize(company: str):
    data = process_company(company)

    summaries = [
        item["summary"]
        for item in data["results"]
        if "summary" in item
    ]

    source_links = [
        item["pdf_url"]
        for item in data["results"]
        if "pdf_url" in item
    ]

    return {
        "company": company,
        "summary": "\n\n".join(summaries) if summaries else "No valid summaries found.",
        "source_links": source_links
    }
