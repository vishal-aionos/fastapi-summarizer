from app.scraper import search_pdfs
from app.s3_utils import download_and_upload_pdf
from app.pdf_utils import extract_text_from_pdf
from app.gemini_utils import summarize_with_gemini
import requests
from io import BytesIO

def process_company(company_name: str):
    pdf_links = search_pdfs(company_name)
    summaries = []

    for report_type in ["earnings", "annual"]:
        link = pdf_links.get(report_type)

        if not link:
            summaries.append({
                "report_type": report_type,
                "error": "No PDF link found for this report type"
            })
            continue

        try:
            pdf_res = requests.get(link)
            pdf_res.raise_for_status()
            pdf_bytes = BytesIO(pdf_res.content)

            extracted_text = extract_text_from_pdf(pdf_bytes)
            summary = summarize_with_gemini(extracted_text)
            s3_uri = download_and_upload_pdf(link, company_name)

            summaries.append({
                "report_type": report_type,
                "pdf_url": link,
                "s3_location": s3_uri,
                "summary": summary
            })
        except Exception as e:
            summaries.append({
                "report_type": report_type,
                "pdf_url": link,
                "error": str(e)
            })

    return {
        "company": company_name,
        "reports": summaries
    }
