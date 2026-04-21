from pydantic import BaseModel
from datetime import datetime

#representação dos dados em JSON
#que a API espera receber ao criar um comentário
class CommentCreate(BaseModel):
    content: str
    post_id: int

#representação dos dados em JSON
#que a API espera receber ao alterar um comentário
class CommentUpdate(BaseModel):
    content: str

#representação dos dados que a API devolve após uma operação
class CommentResponse(BaseModel):
    id: int
    content: str
    created_at: datetime
    post_id: int
    user_id: int

model_config = {"from_attributes": True}
#^ Pydantic, por padrão, lê apenas dicionários,
# mas o SQLAlchemy devolve objetos com atributos.
#Com essa configuração, o Pydantic passa a aceitar objetos.