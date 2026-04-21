from pydantic import BaseModel, EmailStr

#representação dos dados em JSON
#que a API espera receber ao criar um usurário
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    is_author: bool = False

#representação dos dados que a API devolve após uma operação
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    is_author: bool

model_config = {"from_attributes": True}
#^ Pydantic, por padrão, lê apenas dicionários,
# mas o SQLAlchemy devolve objetos com atributos.
#Com essa configuração, o Pydantic passa a aceitar objetos.