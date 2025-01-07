from typing import Optional
from pydantic import BaseModel, Field, EmailStr
from datetime import datetime  # For accurate timestamp typing and usage

class UserBase(BaseModel):
    """
    Base schema for user-related data. Includes common fields like username, email, and password.
    """
    username: str = Field(..., description="Unique username for the user")
    email: EmailStr = Field(..., description="Email address of the user")
    password: str = Field(
        ..., 
        min_length=8, 
        description="Password for the user, must be at least 8 characters"
    )

class UserCreate(UserBase):
    """
    Schema for creating a new user.
    Inherits username, email, and password fields from UserBase.
    """
    pass

class User(UserBase):
    """
    Full schema for a user.
    Extends UserBase with additional fields like id, profile_picture, bio, created_at, and updated_at.
    """
    id: int = Field(..., description="Unique identifier for the user")
    profile_picture: Optional[str] = Field(
        None, 
        description="URL to the user's profile picture"
    )
    bio: Optional[str] = Field(
        None, 
        description="A brief bio or description of the user"
    )
    created_at: Optional[datetime] = Field(
        None, 
        description="Timestamp when the user account was created"
    )
    updated_at: Optional[datetime] = Field(
        None, 
        description="Timestamp when the user account was last updated"
    )

    class Config:
        orm_mode = True  # Enables ORM integration for tools like SQLAlchemy

class UserUpdate(BaseModel):
    """
    Schema for updating user data.
    Allows partial updates by making fields optional.
    """
    username: Optional[str] = Field(
        None, 
        description="New username for the user"
    )
    email: Optional[EmailStr] = Field(
        None, 
        description="New email address for the user"
    )
    password: Optional[str] = Field(
        None, 
        min_length=8, 
        description="New password for the user, must be at least 8 characters"
    )
    profile_picture: Optional[str] = Field(
        None, 
        description="URL to the user's new profile picture"
    )
    bio: Optional[str] = Field(
        None, 
        description="Updated bio or brief description of the user"
    )

    class Config:
        orm_mode = True

