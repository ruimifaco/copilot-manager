from fastapi import APIRouter
from sqlalchemy import text
from app.schemas.recurring import recurringBlocks
from app.db.connection import engine
from app.schemas.recurring import blocksResponse
from app.repositories.recurring_data import get_all_recurring_blocks


router = APIRouter()

@router.get("/recurring")
def list_Blocks():
    return{"status": "ok", "value": get_all_recurring_blocks()}

@router.get("/recurring/{id}")
def list_recurring_id(id: int):
    with engine.connect() as conn:
        recurring_id = conn.execute(text("SELECT title, days_of_week, start_time, end_time, is_fixed, user_id, category_id FROM categories WHERE id = :id_searched"), {"id_searched": id})
        id_result = recurring_id.mappings().first() # mappings() transforma cada linha em um dicionário. all() manda devolver todos os registros.
    return {"status": "ok", "value": id_result}

@router.post("/recurring", response_model=blocksResponse)
def insert_blocks(recurring: recurringBlocks):
    with engine.begin() as conn:
        block_insert = conn.execute(text("INSERT INTO recurring_blocks (title, days_of_week, start_time, end_time, is_fixed, user_id, category_id) VALUES (:title, :days_of_week, :start_time, :end_time, :is_fixed, :user_id, :category_id) RETURNING id, title, days_of_week, start_time, end_time, is_fixed, user_id, category_id;"), {"title": recurring.title, "days_of_week": recurring.days_of_week, "start_time": recurring.start_time, "end_time": recurring.end_time, "is_fixed": recurring.is_fixed, "user_id": recurring.user_id, "category_id": recurring.category_id})
        result = block_insert.mappings().one()
    return {result}

