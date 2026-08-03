from app.schemas.category import CategoryResponse # Importa classe do schema de saída
from app.db.connection import engine # importa a variável do outro arquivo
from sqlalchemy import text # importa a função de texto do SQLAlchemy
from app.schemas.category import CategoryCreate # Chama classe que herda de BaseModel
from fastapi import APIRouter # Importa APIRouter (que serve pra expandir rota do main.py, porque app mora exclusivamente no main.py)
from app.repositories.category_data import get_all_categories
from app.repositories.category_data import get_category_by_id
from fastapi import HTTPException




router = APIRouter()

@router.get("/categories") # responsável por solicitar dados de uma categoria
def list_categories():
    return {"status": "ok", "value": get_all_categories()}

@router.get("/categories/{id}")
def list_category_id(id: int):
    category_searched = get_category_by_id(id)
    if category_searched is None:
        raise HTTPException(status_code=404, detail="ID not found")
    return {"status": "ok", "value": category_searched}

@router.post("/categories", response_model=CategoryResponse) # responsável por inserir dados de uma categoria
def insert_category(category: CategoryCreate): # Aqui tá a classe que fica em schemas
    with engine.begin() as conn: # Abre uma transação. Se der tudo bem ele salva no banco (COMMIT). Se não, desfaz tudo(ROLLBACK).
        category_insert = conn.execute(text("INSERT INTO categories (category_name, is_anchor, user_id) VALUES (:category_name, :is_anchor, :user_id) RETURNING id, category_name, is_anchor, user_id;"), {"category_name": category.category_name, "is_anchor": category.is_anchor, "user_id": category.user_id})
        insert_result = category_insert.mappings().one()
    return {"status": "ok", "value": insert_result}