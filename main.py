from fastapi import FastAPI
from database import Base, engine
from routers import user, post, comment

import models
#importa o pacote models, que por sua vez executa
#o models/__init__.py.
#Garante que o SQLAlchemy conhece todos os models
#antes de tentar criar as tabelas.

app = FastAPI(#cria o app e exibe informações extras no swagger
    title="Blog API",
    description="Uma simples API REST para um blog com posts, usuários e comentários",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)
#Cria as tabelas no PostgreSQL.

#metadata -> onde o SQLAlchemy guardou todas as informações dos models

#create_all -> usa o metadata para gerar o SQL e executar no banco.
#se tabelas já existem -> não faz nada.

app.include_router(user.router)
app.include_router(post.router)
app.include_router(comment.router)
#registra cada router no app principal