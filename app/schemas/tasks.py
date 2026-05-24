from datetime import date
from pydantic import BaseModel
from datetime import time

class TaskCreate(BaseModel):
    title: str
    task_date: date
    planned_start_time: time
    planned_end_time: time
    actual_start_time: time
    actual_end_time: time
    final_status: str
    user_id: int
    category_id: int

class TaskResponse(BaseModel):
    id: int