from pydantic import BaseModel
from datetime import datetime

#representação dos dados em JSON
#que a API espera receber ao criar um post
class PostCreate(BaseModel):
    title: str
    content: str

#representação dos dados que a API devolve após uma operação
class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    author_id: int

model_config = {"from_attributes": True}
#^ Pydantic, por padrão, lê apenas dicionários,
# mas o SQLAlchemy devolve objetos com atributos.
#Com essa configuração, o Pydantic passa a aceitar objetos.