import os
from dotenv import load_dotenv

# Optional: load from .env file for local dev
load_dotenv()

# Microservice base URL
TARGET_HOST = os.getenv("TARGET_HOST", "http://localhost:4999")

# Add more shared constants here later if needed
# e.g. MAX_WAIT = int(os.getenv("MAX_WAIT", 10))
