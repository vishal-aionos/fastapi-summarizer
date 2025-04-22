# # app/pdf_utils.py

import fitz  # PyMuPDF
from typing import Union
from io import BytesIO

def extract_text_from_pdf(pdf_file: Union[str, BytesIO]) -> str:
    text = ""
    # Open the document from path or in-memory BytesIO
    doc = fitz.open(stream=pdf_file, filetype="pdf") if isinstance(pdf_file, BytesIO) else fitz.open(pdf_file)

    for page in doc:
        # Explicitly set the cropbox to match mediabox to avoid fallback/render issues
        mediabox = page.rect
        page.set_cropbox(mediabox)

        # Extract text
        text += page.get_text()

    return text
