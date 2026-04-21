from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text, ForeignKey, DateTime
from datetime import datetime, timezone

#Importa a classe Base do database.py.
#Faz o SQLAlchemy entender que se trata de uma tabela
from database import Base

class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),default=lambda: datetime.now(timezone.utc)
        )
    #^ O lambda calcula a data no momento de cada inserção.
    #Sem ele, a data seria calculada apenas uma vez.
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    #^ Conecta o post ao autor. número precisa existir como id na tabela users

    author: Mapped["User"] = relationship(back_populates="posts")
    #^ Atalho do SLAlchemy para acessar o objeto User completo via post.author
    #back_populates conecta os dois lados da relação.
    comments: Mapped[list["Comment"]] = relationship(back_populates="post")
    #^ mesma ideia, mas para todos os comentários de um post específico, via post.comments