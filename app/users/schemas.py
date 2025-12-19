from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Optional
from datetime import datetime


class UserRegister(BaseModel):
    email: EmailStr
    password: str
    username: str = Field(..., min_length=1, max_length=10, description="Username must be between 1 and 10 characters")

    @field_validator('username')
    @classmethod
    def validate_username(cls, v):
        if len(v) > 10:
            raise ValueError('Username must not exceed 10 characters')
        if len(v) < 1:
            raise ValueError('Username must not be empty')
        return v


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: str
    username: str
    is_user: bool
    is_moderator: bool
    is_admin: bool
    created_at: datetime

    class Config:
        from_attributes = True
