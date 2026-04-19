from fastapi import FastAPI
from database import Base, engine
from routers import user, post, comment
import models

app = FastAPI(
    title="Blog API",
    description="Uma simples API REST para um blog com posts, usuários e comentários",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(user.router)
app.include_router(post.router)
app.include_router(comment.router)