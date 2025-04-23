from serpapi import GoogleSearch
from dotenv import load_dotenv
import os

load_dotenv()
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")

def search_pdfs(company_name: str):
    queries = {
        "earnings": f"{company_name} earnings report filetype:pdf",
        "annual": f"{company_name} annual report filetype:pdf"
    }

    results = {}

    for report_type, query in queries.items():
        search = GoogleSearch({
            "q": query,
            "api_key": SERPAPI_API_KEY,
            "num": 5
        })

        search_results = search.get_dict()
        pdf_links = []

        for result in search_results.get("organic_results", []):
            link = result.get("link")
            if link and link.lower().endswith(".pdf"):
                pdf_links.append(link)

        # Take the first valid PDF
        results[report_type] = pdf_links[0] if pdf_links else None

    return results
