from pydantic import BaseModel
from datetime import time

class recurringBlocks(BaseModel):
    title: str
    days_of_week: str
    start_time: time
    end_time: time
    is_fixed: bool = True
    user_id: int
    category_id: int