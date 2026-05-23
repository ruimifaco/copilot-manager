# Aqui é que deve ser criada o framework da API
# Centraliza as primeiras rotas
# Fica aqui apenas a configuração global

from fastapi import FastAPI # Aqui, FastAPI cria a aplicação web/API que vai receber requisições HTTP.
from app.db.connection import engine # importa a variável do outro arquivo
from sqlalchemy import text # importa a função de texto do SQLAlchemy

app = FastAPI(title="Co-piloto API") # Eu vou definir a api como app pra não ter que escrever toda vez

@app.get("/") # pra app, quero fazer um GET e quero que o endereço da rota seja só "/"
def root(): # defino a função de nome "root". Essa função roda quando alguém acessa a rota GET /
    return {"message": "Co-piloto API is running"} # Peço pra retornar isso lá na web

@app.get("/health/db") # criação da rota que atesta a saúde da API
def test_connection():
    with engine.connect() as conn: # "with": fecha a conexão com o banco automaticamente; "engine.connect()" inicia  conexão com o banco; "conn" é apelido
        result = conn.execute(text("SELECT 1")).scalar() # apelido executa em texto SELECT. O scalar () pega da tabela apenas o valor puro, transformando em um número comum no Python
    return {"status": "conexão feita com sucesso", "valor": result}