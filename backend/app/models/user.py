from typing import Optional
from pydantic import BaseModel, Field, EmailStr, validator
from datetime import datetime
from uuid import uuid4  # For generating unique IDs

class BaseConfig:
    orm_mode = True  # Enables ORM integration for tools like SQLAlchemy

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

    @validator('username')
    def username_alphanumeric(cls, v):
        if not v.isalnum():
            raise ValueError('Username must be alphanumeric')
        return v

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
    id: str = Field(default_factory=lambda: str(uuid4()), description="Unique identifier for the user")
    profile_picture: Optional[str] = Field(
        None, 
        description="URL to the user's profile picture"
    )
    bio: Optional[str] = Field(
        None, 
        description="A brief bio or description of the user"
    )
    created_at: datetime = Field(
        default_factory=datetime.utcnow, 
        description="Timestamp when the user account was created"
    )
    updated_at: datetime = Field(
        default_factory=datetime.utcnow, 
        description="Timestamp when the user account was last updated"
    )
    is_active: bool = Field(
        default=True, 
        description="Indicates if the user account is active"
    )
    last_login: Optional[datetime] = Field(
        None, 
        description="Timestamp of the user's last login"
    )

    class Config(BaseConfig):
        pass

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
    is_active: Optional[bool] = Field(
        None, 
        description="Update the active status of the user account"
    )

    class Config(BaseConfig):
        pass
