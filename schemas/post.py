from pydantic import BaseModel
from datetime import datetime

class PostCreate(BaseModel):
    title: str
    content: str

class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    author_id: int

model_config = {"from_attributes": True}