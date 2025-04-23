from app.scraper import search_pdfs, fallback_search_articles
from app.s3_utils import download_and_upload_pdf
from app.pdf_utils import extract_text_from_pdf
from app.gemini_utils import summarize_with_gemini
import requests
from io import BytesIO

def process_company(company_name: str):
    pdf_links = search_pdfs(company_name)
    summaries = []

    if not pdf_links:
        article_links = fallback_search_articles(company_name)
        for link in article_links[:2]:
            try:
                article_text = requests.get(link).text
                summary = summarize_with_gemini(article_text[:15000])

                summaries.append({
                    "pdf_url": link,
                    "s3_location": None,
                    "summary": summary,
                    "report_type": "article"
                })
            except Exception as e:
                summaries.append({
                    "pdf_url": link,
                    "error": str(e),
                    "report_type": "article"
                })
    else:
        for link in pdf_links[:2]:
            try:
                pdf_res = requests.get(link)
                pdf_res.raise_for_status()
                pdf_bytes = BytesIO(pdf_res.content)

                extracted_text = extract_text_from_pdf(pdf_bytes)
                summary = summarize_with_gemini(extracted_text)
                s3_uri = download_and_upload_pdf(link, company_name)

                report_type = "annual" if "annual" in link.lower() else "earnings"

                summaries.append({
                    "pdf_url": link,
                    "s3_location": s3_uri,
                    "summary": summary,
                    "report_type": report_type
                })
            except Exception as e:
                summaries.append({
                    "pdf_url": link,
                    "error": str(e),
                    "report_type": "pdf"
                })

    return {
        "company": company_name,
        "reports": summaries
    }
