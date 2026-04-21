from pydantic_settings import BaseSettings

#Faz leitura do .env e valida variáveis
class Settings(BaseSettings):
    database_url: str
    secret_key: str

    class Config:
        env_file = ".env"

#Instância da classe. permite ser importado
#para não ter que ler o .env toda vez.
settings = Settings()