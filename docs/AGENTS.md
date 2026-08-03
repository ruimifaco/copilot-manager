# AGENTS.md

## Projeto
O Co-piloto é um sistema pessoal de constância que organiza tasks,
blocos recorrentes, categorias-âncora e uma visão diária.

## Regra de aprendizagem
O objetivo do projeto também é o aprendizado do desenvolvedor.

- Não implemente uma nova abstração ou padrão sem explicar antes.
- Rui implementa manualmente o primeiro exemplo de cada conceito novo.
- Depois que o primeiro exemplo for aprovado, o Codex pode repetir
  o padrão nas outras entidades.
- Não antecipe funcionalidades fora da fase atual.
- Não altere decisões de arquitetura sem aprovação.
- Antes de codificar, apresente o plano da tarefa.
- Depois de codificar, informe arquivos alterados, testes executados
  e decisões tomadas.

## Responsabilidades
- API: recebe e valida requisições.
- Repository: acessa o banco de dados.
- Service: contém regras de negócio.
- Schema: define entrada e saída.
- db: contém conexão e infraestrutura de persistência.

## Stack
- Python
- FastAPI
- PostgreSQL
- SQLAlchemy Core com SQL explícito
- Telegram na interface da V1
- OpenAI somente para parsing e verbalização

## Comandos
- Rodar API: ...
- Rodar testes: ...
- Subir banco: ...