from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    is_author: bool = False

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    is_author: bool

model_config = {"from_attributes": True}