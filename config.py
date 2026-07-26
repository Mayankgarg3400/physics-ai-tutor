import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

PDF_PATH = "data/Physics-Book.pdf"

CHROMA_DB = "chroma_db"