# Co-piloto

Backend inicial do projeto Co-piloto, uma API para organizar rotinas, categorias, blocos recorrentes e tarefas.

## Stack

Liste as tecnologias usadas:
- Python
- FastAPI
- PostgreSQL
- Docker
- SQLAlchemy

## Estrutura atual

Explique rapidamente as principais pastas:
- app/main.py: É onde fica todas as rotas importantes pro projeto, onde é importado FASTAPI, onde fica a configuração global.
- app/db/ - onde fica as coisas sobre banco de dados: código SQL e a estrutura necessária para a conexão com o banco.
- app/api/
- app/models/
- app/schemas/
- docs/ - Onde fica a documentação das versões
- tests/

Não precisa explicar todas profundamente.

## Banco de dados

Explique que o banco roda localmente via Docker e que o schema inicial está em: app/db/practice.sql

Diga também que ele cria as tabelas:
- users
- categories
- recurring_blocks
- tasks

## Como preparar o banco

Aqui você coloca o comando que você usa para rodar o SQL no banco:

docker exec -i postgres-local psql -U postgres -d copiloto_db < ./app/db/practice.sql

Esse comando executa o arquivo app/db/practice.sql dentro do banco copiloto_db, criando as tabelas iniciais e inserindo dados de teste.

## Como rodar a API

Precisa instalar tudo que tá em `requirements.txt`, configurar .env com o URL do banco e rodar o servidor com uvicorn usando `uvicorn app.main:app --reload`

## Endpoints disponíveis

Liste os endpoints atuais:

GET / -> testa se a API tá funcionando
GET /health/db -> testa se a conexão com o banco tá funcionando
GET /categories -> extrai uma célula da tabela categories
POST /categories -> insere valores relacionados à tabela categories no banco 

## Status atual

A V1 atual já conecta no PostgreSQL local, lista categorias e permite criar uma nova categoria via API.