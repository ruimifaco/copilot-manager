# Co-piloto

Backend inicial de um copiloto pessoal de rotina. A API organiza categorias, blocos recorrentes e tarefas para montar uma base confiável de acompanhamento diário.

Na V1, a LLM pode apoiar parsing de mensagens e verbalização de respostas, mas as regras centrais de cadastro, vínculo entre entidades e geração da visão diária ficam no sistema.

## Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker
- Pydantic
- Uvicorn

## Estrutura atual

- `app/main.py`: cria a aplicação FastAPI, registra routers e expõe rotas globais.
- `app/api/`: concentra as rotas HTTP de categorias, tasks e blocos recorrentes.
- `app/db/`: guarda a conexão com o banco e o SQL inicial de prática.
- `app/repositories/`: isola as operações de leitura e escrita no PostgreSQL.
- `app/schemas/`: define os schemas Pydantic de entrada e saída da API.
- `docs/`: registra requisitos, decisões, roadmap e diagramas da V1.

## Banco de dados

O banco roda localmente em PostgreSQL. O schema inicial está em `app/db/practice.sql` e cria as tabelas:

- `users`
- `categories`
- `recurring_blocks`
- `tasks`

O mesmo arquivo também insere dados de teste para desenvolvimento local.

## Como preparar o banco

Com um container PostgreSQL local chamado `postgres-local` e um banco `copiloto_db`, execute:

```bash
docker exec -i postgres-local psql -U postgres -d copiloto_db < ./app/db/practice.sql
```

Esse comando aplica o schema de `app/db/practice.sql`, recria as tabelas iniciais e carrega os dados de teste.

## Como rodar a API

Crie um `.env` na raiz do projeto com a URL do banco:

```env
DATABASE_URL=postgresql+psycopg2://postgres:senha@localhost:5432/copiloto_db
```

Instale as dependências e suba o servidor:

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Endpoints disponíveis

- `GET /`: verifica se a API está rodando.
- `GET /health/db`: verifica a conexão com o banco.
- `GET /categories`: lista categorias.
- `GET /categories/{id}`: busca uma categoria por ID.
- `POST /categories`: cria uma categoria.
- `GET /tasks`: lista tasks.
- `GET /tasks/{id}`: busca uma task por ID.
- `POST /tasks`: cria uma task.
- `GET /recurring`: lista blocos recorrentes.
- `GET /recurring/{id}`: busca um bloco recorrente por ID.
- `POST /recurring`: cria um bloco recorrente.

## Status atual

A V1 atual já conecta no PostgreSQL local, lista categorias e permite criar uma nova categoria via API.
