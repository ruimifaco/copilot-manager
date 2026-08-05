from fastapi import APIRouter, HTTPException, status
from app.schemas.recurring import recurringBlocks
from app.schemas.recurring import blocksResponse
from app.repositories.recurring_data import get_all_recurring_blocks, get_recurring_block_by_id, insert_recurring_block_db


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

@router.post("/recurring", response_model=blocksResponse, status_code=status.HTTP_201_CREATED)
def insert_blocks(recurring: recurringBlocks):
    user_recurring_block_data = {
        "title": recurring.title,
        "days_of_week": recurring.days_of_week,
        "start_time": recurring.start_time,
        "end_time": recurring.end_time,
        "is_fixed": recurring.is_fixed,
        "user_id": recurring.user_id,
        "category_id": recurring.category_id
    }

    insert_user_recurring_block = insert_recurring_block_db(user_recurring_block_data)
    return insert_user_recurring_block
