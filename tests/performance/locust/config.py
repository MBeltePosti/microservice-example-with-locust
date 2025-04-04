import os
from dotenv import load_dotenv

load_dotenv()

# Microservice base URL
TARGET_HOST = os.getenv("TARGET_HOST", "http://localhost:4999")
