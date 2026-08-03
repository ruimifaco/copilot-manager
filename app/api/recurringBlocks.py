from fastapi import APIRouter, HTTPException
from sqlalchemy import text
from app.schemas.recurring import recurringBlocks
from app.db.connection import engine
from app.schemas.recurring import blocksResponse
from app.repositories.recurring_data import get_all_recurring_blocks, get_recurring_block_by_id


router = APIRouter()

@router.get("/recurring")
def list_Blocks():
    return{"status": "ok", "value": get_all_recurring_blocks()}

@router.get("/recurring/{id}")
def list_recurring_id(id: int):
    recurring_block_searched = get_recurring_block_by_id(id)
    if recurring_block_searched is None:
        raise HTTPException(status_code=404, detail="ID not found")
    return {"status": "ok", "value": recurring_block_searched}

@router.post("/recurring", response_model=blocksResponse)
def insert_blocks(recurring: recurringBlocks):
    with engine.begin() as conn:
        block_insert = conn.execute(text("INSERT INTO recurring_blocks (title, days_of_week, start_time, end_time, is_fixed, user_id, category_id) VALUES (:title, :days_of_week, :start_time, :end_time, :is_fixed, :user_id, :category_id) RETURNING id, title, days_of_week, start_time, end_time, is_fixed, user_id, category_id;"), {"title": recurring.title, "days_of_week": recurring.days_of_week, "start_time": recurring.start_time, "end_time": recurring.end_time, "is_fixed": recurring.is_fixed, "user_id": recurring.user_id, "category_id": recurring.category_id})
        result = block_insert.mappings().one()
    return {result}
