# security.py

from fastapi import Depends, HTTPException, Header, status
from fastapi.security.api_key import APIKeyHeader
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY_NAME = os.getenv("API_KEY_NAME")
API_KEY = os.getenv("API_KEY")


class ApiKeyHeaderCustom(APIKeyHeader):
    def __init__(self, name: str = API_KEY_NAME, auto_error: bool = True):
        super().__init__(name=name, auto_error=auto_error)


def verify_api_key(api_key: str = Depends(ApiKeyHeaderCustom())):
    if api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key",
        )
    return api_key
