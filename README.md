# 📝 Blog API

API REST para um blog simples, construída com FastAPI e PostgreSQL. Permite gerenciar usuários, posts e comentários com endpoints CRUD completos.

> Projeto desenvolvido como parte de um roadmap Full Stack de 12 meses — Mês 4: FastAPI & APIs.

---

## 🚀 Tecnologias

- **[FastAPI](https://fastapi.tiangolo.com/)** — framework web moderno e de alta performance
- **[SQLAlchemy](https://www.sqlalchemy.org/)** — ORM para comunicação com o banco de dados
- **[PostgreSQL](https://www.postgresql.org/)** — banco de dados relacional
- **[Pydantic](https://docs.pydantic.dev/)** — validação de dados e schemas
- **[Uvicorn](https://www.uvicorn.org/)** — servidor ASGI para rodar a aplicação

---

## 📁 Estrutura do projeto

```
blog-api/
├── routers/
│   ├── users.py        # Endpoints de usuários
│   ├── posts.py        # Endpoints de posts
│   └── comments.py     # Endpoints de comentários
├── models/
│   ├── __init__.py     # Registra os models no SQLAlchemy
│   ├── user.py         # Tabela de usuários
│   ├── post.py         # Tabela de posts
│   └── comment.py      # Tabela de comentários
├── schemas/
│   ├── user.py         # Schemas Pydantic para usuários
│   ├── post.py         # Schemas Pydantic para posts
│   └── comment.py      # Schemas Pydantic para comentários
├── services/
│   └── README.md       # Camada reservada para lógica de negócio futura
├── main.py             # Ponto de entrada da aplicação
├── config.py           # Leitura e validação das variáveis de ambiente
├── database.py         # Configuração da conexão com o banco
├── .env.example        # Modelo de variáveis de ambiente (sem dados reais)
└── .gitignore
```

---

## ⚙️ Como rodar localmente

**1. Clone o repositório**
```bash
git clone https://github.com/seu-usuario/blog-api.git
cd blog-api
```

**2. Crie e ative o ambiente virtual**
```bash
python -m venv venv
source venv/Scripts/activate  # Windows com Git Bash
```

**3. Instale as dependências**
```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic-settings python-dotenv
```

**4. Configure as variáveis de ambiente**
```bash
cp .env.example .env
```
Abra o `.env` e preencha com os dados do seu banco de dados:
```
DATABASE_URL=postgresql://usuario:senha@localhost:5432/blog
SECRET_KEY=sua-chave-secreta
```

**5. Suba o servidor**
```bash
uvicorn main:app --reload
```

A API estará disponível em `http://localhost:8000`.

---

## 📖 Documentação

O FastAPI gera documentação interativa automaticamente. Com o servidor rodando, acesse:

- **Swagger UI** → [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc** → [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🔗 Endpoints

### Usuários `/users`
| Método | Rota | Descrição |
|--------|------|-----------|
| `POST` | `/users/` | Cria um novo usuário |
| `GET` | `/users/` | Lista todos os usuários |
| `GET` | `/users/{id}` | Busca um usuário pelo ID |
| `DELETE` | `/users/{id}` | Deleta um usuário |

### Posts `/posts`
| Método | Rota | Descrição |
|--------|------|-----------|
| `POST` | `/posts/` | Cria um novo post (requer `is_author=true`) |
| `GET` | `/posts/` | Lista todos os posts |
| `GET` | `/posts/{id}` | Busca um post pelo ID |
| `PUT` | `/posts/{id}` | Atualiza um post |
| `DELETE` | `/posts/{id}` | Deleta um post |

### Comentários `/comments`
| Método | Rota | Descrição |
|--------|------|-----------|
| `POST` | `/comments/` | Cria um novo comentário |
| `GET` | `/comments/` | Lista todos os comentários |
| `GET` | `/comments/post/{post_id}` | Lista comentários de um post |
| `PUT` | `/comments/{id}` | Atualiza um comentário |
| `DELETE` | `/comments/{id}` | Deleta um comentário |

---

## 💡 Conceitos praticados

- **Injeção de dependência** com `Depends()` do FastAPI
- **Variáveis de ambiente** com `pydantic-settings`
- **ORM** com SQLAlchemy e relacionamentos entre tabelas
- **Schemas** Pydantic separados por operação (`Create`, `Update`, `Response`)
- **Documentação automática** com Swagger
- **Arquitetura em camadas** separando routers, models e schemas

---

## 📌 Observações

- Neste projeto a autenticação é simulada via `user_id` e `author_id` passados manualmente nos endpoints. Em produção, isso seria substituído por um sistema de autenticação JWT.
- Usuários com `is_author=false` podem comentar mas não criar posts.
- Apenas o autor de um post ou comentário pode editá-lo ou deletá-lo.
