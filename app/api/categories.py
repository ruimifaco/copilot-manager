
from app.db.connection import engine # importa a variável do outro arquivo
from sqlalchemy import text # importa a função de texto do SQLAlchemy
from app.schemas.category import CategoryCreate # Chama classe que herda de BaseModel
from fastapi import APIRouter

router = APIRouter()

@router.get("/categories") # responsável por solicitar dados de uma categoria
def list_categories():
    with engine.connect() as conn:
        db_result = conn.execute(text("SELECT id, category_name, is_anchor, user_id FROM categories ORDER BY id;")) # .scalar() ausente porque eu pedi a tabela inteira
        categories = db_result.mappings().all() # Transforma a tabela que foi pedida em uma lista de dicionários porque Python não lê direito se fosse direto
    return {"status": "ok", "valor": categories}

@router.post("/categories") # responsável por inserir dados de uma categoria
def insert_category(category: CategoryCreate): # Aqui tá a classe que fica em schemas
    with engine.begin() as conn: # Abre uma transação. Se der tudo bem ele salva no banco (COMMIT). Se não, desfaz tudo(ROLLBACK).
        category_insert = conn.execute(text("INSERT INTO categories (category_name, is_anchor, user_id) VALUES (:category_name, :is_anchor, :user_id) RETURNING id, category_name, is_anchor, user_id;"), {"category_name": category.category_name, "is_anchor": category.is_anchor, "user_id": category.user_id})
        insert_result = category_insert.mappings().one()
    return {"status": "ok", "valor": insert_result}