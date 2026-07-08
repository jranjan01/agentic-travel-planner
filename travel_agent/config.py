import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GEMINI_MODEL_1 = os.getenv("GEMINI_MODEL_1")
GEMINI_MODEL_2 = os.getenv("GEMINI_MODEL_2")
