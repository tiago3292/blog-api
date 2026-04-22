# services

Camada de serviços — lógica de negócio complexa que não pertence ao router.

## Quando usar?
Quando um endpoint precisar fazer mais de uma coisa além de salvar/buscar no banco.
Exemplos:
- Criar um post e notificar seguidores por email
- Deletar um usuário e limpar todos os seus dados relacionados
- Processar um pagamento e registrar um log

## Neste projeto
Não foi necessário — a lógica é simples o suficiente para ficar nos routers.