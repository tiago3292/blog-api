# Schemas

armazena os modelos Pydantic (BaseModel), que são responsáveis por definir a estrutura, validação e serialização dos dados que entram e saem da API.

## Funções
- Validação de Dados de Entrada (Requests): Garante que os dados enviados pelo cliente (JSON) contenham os campos corretos, tipos de dados adequados (ex: int, str, email) e regras de negócio antes de chegar à lógica da aplicação.

- Serialização de Dados de Saída (Responses): Define o formato JSON que a API retornará, permitindo filtrar campos sensíveis (como senhas) ou formatar dados de resposta.

- Documentação Automática: O FastAPI utiliza esses esquemas para gerar automaticamente a documentação da API (Swagger UI/OpenAPI).

- Organização e Escalabilidade: Separa as definições de dados dos endpoints (rotas), permitindo um código mais limpo e fácil de manter em projetos maiores.