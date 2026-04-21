from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from config import settings

#Cria conexão com o banco via URL que vem do config.py
engine = create_engine(settings.database_url)

#Fábrica de sessões.
# Cada requisição abre uma nova sessão e fecha no final
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

#Permite o SQLAlchemy criar tabelas no banco.
#Herdado por todos os models
class Base(DeclarativeBase):
    pass

#Função de injeção de dependência
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()