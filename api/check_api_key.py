from fastapi import HTTPException, Header
from dotenv import load_dotenv
import os

load_dotenv()  # Load the variables from .env into the environment
API_KEY = os.getenv("API_KEY")

def check_api_key(api_key: str = Header(...)):
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
