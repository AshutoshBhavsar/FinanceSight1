import os
import pdfplumber
import pytesseract
from PIL import Image
from docx import Document

# If you're using Tesseract installed on Windows, set path
# Example: C:/Program Files/Tesseract-OCR/tesseract.exe
TESSERACT_PATH = os.getenv("TESSERACT_PATH", r"C:\Program Files\Tesseract-OCR\tesseract.exe")
pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

def extract_text_from_pdf(file_path):
    text = ""
    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        print(f"[PDF ERROR] {e}")
    return text

def extract_text_from_docx(file_path):
    try:
        doc = Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
    except Exception as e:
        print(f"[DOCX ERROR] {e}")
        return ""

def extract_text_from_image(image_path):
    try:
        return pytesseract.image_to_string(Image.open(image_path), lang="eng")
    except Exception as e:
        print(f"[IMAGE OCR ERROR] {e}")
        return ""
