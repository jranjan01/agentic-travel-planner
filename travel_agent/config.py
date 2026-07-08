import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GEMINI_MODEL_1 = os.getenv("GEMINI_MODEL_1")
GEMINI_MODEL_2 = os.getenv("GEMINI_MODEL_2")
FILE_PATH = os.getenv(
    "FILE_PATH"
)  # Please clone the travel-mcp-server repository and provide the full file path to the /server directory.
