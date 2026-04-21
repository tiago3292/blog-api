from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Text, ForeignKey, DateTime
from datetime import datetime, timezone

#Importa a classe Base do database.py.
#Faz o SQLAlchemy entender que se trata de uma tabela
from database import Base

class Comment(Base):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
        )
    #^ O lambda calcula a data no momento de cada inserção.
    #Sem ele, a data seria calculada apenas uma vez.
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)

    post: Mapped["Post"] = relationship(back_populates="comments")
    #^ Atalho do SLAlchemy para acessar o post ao qual o comentário pertence via comment.post
    #back_populates conecta os dois lados da relação.
    user: Mapped["User"] = relationship(back_populates="comments")
    #^ mesma ideia, mas para saber quem escreveu o comentário via comment.user