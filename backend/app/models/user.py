from typing import Optional
from pydantic import BaseModel, Field, EmailStr

class UserBase(BaseModel):
    username: str = Field(..., description="Unique username for the user")
    email: EmailStr = Field(..., description="Email address of the user")
    password: str = Field(
        ..., 
        min_length=8, 
        description="Password for the user, minimum 8 characters"
    )

class UserCreate(UserBase):
    """
    Schema for creating a new user.
    Inherits username, email, and password fields from UserBase.
    """
    pass

class User(UserBase):
    id: int = Field(..., description="ID of the user")
    profile_picture: Optional[str] = Field(
        None, 
        description="URL to the user's profile picture"
    )
    bio: Optional[str] = Field(
        None, 
        description="Brief description of the user"
    )
    created_at: Optional[str] = Field(
        None, 
        description="Timestamp when the user account was created"
    )
    updated_at: Optional[str] = Field(
        None, 
        description="Timestamp when the user account was last updated"
    )

    class Config:
        orm_mode = True  # Enables ORM mode for integration with ORMs like SQLAlchemy

class UserUpdate(BaseModel):
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
        description="New password for the user, minimum 8 characters"
    )
    profile_picture: Optional[str] = Field(
        None, 
        description="URL to the user's new profile picture"
    )
    bio: Optional[str] = Field(
        None, 
        description="Updated brief description of the user"
    )

    class Config:
        orm_mode = True
