from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import RedirectResponse
from fastapi import APIRouter, Query, Request
from urllib.parse import urlencode
from dotenv import load_dotenv
from httpx import AsyncClient
import requests
import os

load_dotenv()

router = APIRouter(prefix="/auth")

GOOGLE_CLIENT_URL = os.getenv("GOOGLE_CLIENT_URL")
GOOGLE_SECRET_URL = os.getenv("GOOGLE_CLIENT_SECRET")
REDIRECT_URL = "http://localhost:8000/auth/callback"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")



@router.get("/google")
async def login_google():
    params = {
        "client_id": GOOGLE_CLIENT_URL,
        "redirect_uri": REDIRECT_URL,
        "response_type": "code",
        "scope": "openid email profile",
        "prompt": "consent"
    }
    print("here")

    url = f"https://accounts.google.com/o/oauth2/auth?{urlencode(params)}"
    print(url)
    return RedirectResponse(url)

@router.get("/callback")
async def auth_callback(req: Request):
    code = req.query_params.get("code")

    token_url = "https://oauth2.googleapis.com/token"
    data = {
        "code": code,
        "client_id": GOOGLE_CLIENT_URL,
        "client_secret": GOOGLE_SECRET_URL,
        "redirect_uri": REDIRECT_URL,
        "grant_type": "authorization_code"
    }
    response = requests.post(token_url, data=data)
    print("response", response.json())
    access_token = response.json().get("access_token")
    async with AsyncClient() as client: 
        userinfo_response = await client.get(
            "https://www.googleapis.com/oauth2/v2/userinfo",
            headers = {"Authorization": f"Bearer {access_token}"}
        )
        user_info = userinfo_response.json()
    # return user_info.json()
    return {"user_info": user_info}