from pydantic import BaseModel
from datetime import datetime

class CommentCreate(BaseModel):
    content: str
    post_id: int

class CommentUpdate(BaseModel):
    content: str

class CommentResponse(BaseModel):
    id: int
    content: str
    created_at: datetime
    post_id: int
    user_id: int

model_config = {"from_attributes": True}