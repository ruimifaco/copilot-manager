from fastapi import APIRouter
from sqlalchemy import text
from app.schemas.recurring import recurringBlocks
from app.db.connection import engine



router = APIRouter()

@router.get("/recurring")
def list_Blocks():
    with engine.connect() as conn:
        db_result = conn.execute(text("SELECT title, days_of_week, start_time, end_time, is_fixed, user_id, category_id FROM recurring_blocks ORDER BY id;"))
        blocks = db_result.mappings().all()
    return{"status": "ok", "value": blocks}

@router.post("/recurring")
def insert_blocks(recurring: recurringBlocks):
    with engine.begin() as conn:
        block_insert = conn.execute(text("INSERT INTO recurring_blocks (title, days_of_week, start_time, end_time, is_fixed, user_id, category_id) VALUES (:title, :days_of_week, :start_time, :end_time, :is_fixed, :user_id, :category_id) RETURNING id, title, days_of_week, start_time, end_time, is_fixed, user_id, category_id;"), {"title": recurring.title, "days_of_week": recurring.days_of_week, "start_time": recurring.start_time, "end_time": recurring.end_time, "is_fixed": recurring.is_fixed, "user_id": recurring.user_id, "category_id": recurring.category_id})
        result = block_insert.mappings().one()
    return {"status": "ok", "value": result}


