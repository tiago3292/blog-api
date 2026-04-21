from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean

#Importa a classe Base do database.py.
#Faz o SQLAlchemy entender que se trata de uma tabela
from database import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    is_author: Mapped[bool] = mapped_column(Boolean, default=False)

    posts: Mapped[list["Post"]] = relationship(back_populates="author")
    #^ Atalho do SLAlchemy para acessar todos os posts de um usuário via user.posts
    #back_populates conecta os dois lados da relação.
    comments: Mapped[list["Comment"]] = relationship(back_populates="user")
    #^ mesma ideia, mas para comentários, via user.comments