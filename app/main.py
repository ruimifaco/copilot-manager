from fastapi import FastAPI # Aqui, FastAPI cria a aplicação web/API que vai receber requisições HTTP.
from app.db.connection import engine
from sqlalchemy import text

app = FastAPI(title="Co-piloto API") # Eu vou definir a api como app pra não ter que escrever toda vez

@app.get("/") # pra app, quero fazer um GET e quero que o endereço da rota seja só "/"
def root(): # defino a função de nome "root". Essa função roda quando alguém acessa a rota GET /
    return {"message": "Co-piloto API is running"} # Peço pra retornar isso lá na web

@app.get("/health/db")
def test_connection():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1")).scalar()
    return {"status": "conexão feita com sucesso", "valor": result}

@app.get("/categories")
def list_categories():
    with engine.connect() as conn:
        db_result = conn.execute(text("SELECT id, category_name, is_anchor, user_id FROM categories ORDER BY id;"))
        categories = db_result.mappings().all()
    return{"status": "ok", "valor": categories}