from typing import Optional

from pydantic import BaseModel, Field

class UserBase(BaseModel):
    username: str = Field(..., description="Unique username for the user")
    email: str = Field(..., description="Email address of the user")
    password: str = Field(..., description="Password for the user")

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int = Field(..., description="ID of the user")
    # Add additional fields as needed, e.g., profile picture, bio, etc.
    # profile_picture: Optional[str] = Field(None, description="URL to the user's profile picture")
    # bio: Optional[str] = Field(None, description="Brief description of the user")

class UserUpdate(BaseModel):
    username: Optional[str] = Field(None, description="New username for the user")
    email: Optional[str] = Field(None, description="New email address for the user")
    password: Optional[str] = Field(None, description="New password for the user")
    # Add optional fields for updating other user attributes as needed.
