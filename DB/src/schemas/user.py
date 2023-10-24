from typing import Optional
from pydantic import BaseModel, HttpUrl, EmailStr


class User(BaseModel):
    id: Optional[int]
    first_name: str
    last_name: str
    full_name: str
    job_title: str
    job_type: str
    phone: str
    email: EmailStr
    image: HttpUrl
    country: str
    city: str
    onboarding_completion: int
