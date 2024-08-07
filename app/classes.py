from pydantic import BaseModel
from typing import List, Optional


class UserBase(BaseModel):
    id: str
    sso_id: int
    email: str
    name: str
    picture: str
    sso_type: str

class ThemeBase(BaseModel):
    id: str
    user_id: str
    portfolio_name: str


