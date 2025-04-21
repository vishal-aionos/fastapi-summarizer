# app/pdf_utils.py
import pdfplumber
from typing import Union
from io import BytesIO

def extract_text_from_pdf(pdf_file: Union[str, BytesIO]) -> str:
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text
