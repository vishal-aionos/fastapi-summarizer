# app/gemini_utils.py
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash-exp-image-generation")

def summarize_with_gemini(text: str):
    prompt = f"""
You are a financial analyst. Read the following text from an earnings report and generate a concise summary of key financial metrics, revenue changes, profit/loss, and any forward guidance.

Text:
{text[:15000]}  # Gemini input limit is around 30,000 tokens, so we keep a slice for safety.
"""
    response = model.generate_content(prompt)
    return response.text
