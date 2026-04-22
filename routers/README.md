# Routers

Organiza e modula os endpoints (rotas) da API, separando-os do arquivo principal (main.py). Ela permite dividir a aplicação em múltiplos arquivos funcionais, facilitando a manutenção, leitura e escalabilidade do código, especialmente quando o número de endpoints cresce.

## Usado para:
- Modularização (APIRouter): A classe APIRouter do FastAPI é usada para agrupar rotas relacionadas (ex: users.py, items.py) em arquivos separados, funcionando como "mini aplicações".

- Melhor Organização e Manutenção: Ao mover rotas para a pasta routers, o arquivo main.py fica mais limpo e focado na configuração inicial, enquanto a lógica de negócio de cada funcionalidade fica isolada.

- Agrupamento e Prefixo: Com APIRouter, é fácil definir prefixos comuns (ex: /api/v1/users) e tags para documentação automática (Swagger/OpenAPI) de todos os endpoints dentro de um módulo.

- Colaboração Facilitada: Em equipes maiores, ter múltiplos arquivos de rotas evita conflitos de merge no controle de versão (Git), já que desenvolvedores podem trabalhar em arquivos diferentes simultaneamente.