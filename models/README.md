# Models

Armazena as definições de estruturas de dados que interagem diretamente com o banco de dados. Ela faz parte da camada de persistência de dados (geralmente usando ORMs como SQLAlchemy) e serve para organizar e separar essas definições da lógica de API.

## Exemplos de uso
- Definição de Tabelas (ORM): Classes dentro da pasta models representam as tabelas no seu banco de dados SQL (ex: User, Product, Order). Elas definem os tipos de colunas, chaves primárias e relacionamentos.

- Organização e Manutenção: Ao centralizar os modelos de banco de dados, fica mais fácil realizar manutenções e entender a estrutura de dados da aplicação.

- Separação de Preocupações: Ela separa os modelos ORM (banco de dados) dos modelos Pydantic (esquemas de validação de API).

- Facilita o uso de ORMs: Geralmente, os arquivos nesta pasta herdam de uma Base do SQLAlchemy para criar os mapas de dados, permitindo interações assíncronas com o banco.