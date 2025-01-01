from pydantic import BaseModel, Field, EmailStr

class UserModel(BaseModel):
    name: str = Field(..., description="Username")
    email: EmailStr = Field(..., description="User email")
    password: str = Field(..., min_length=6, description="User password")
    