# app/scraper.py
from serpapi import GoogleSearch
from dotenv import load_dotenv
load_dotenv()
import os

SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")

def search_pdfs(company_name: str):
    query = f"{company_name} earnings report filetype:pdf"

    search = GoogleSearch({
        "q": query,
        "api_key": SERPAPI_API_KEY,
        "num": 10
    })

    results = search.get_dict()
    pdf_links = []

    for result in results.get("organic_results", []):
        link = result.get("link")
        if link and link.lower().endswith(".pdf"):
            pdf_links.append(link)

    return pdf_links
