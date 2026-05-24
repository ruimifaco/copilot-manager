# app/schemas: Nessa pasta ficam os Schemas do Pydantic (as classes que herdam de BaseModel). Schema é uma estrutura que organiza e deifine regras para dados

from datetime import date
from pydantic import BaseModel
from datetime import time

class TaskCreate(BaseModel):
    title: str
    task_date: date | None = None
    planned_start_time: time | None = None
    planned_end_time: time | None = None
    actual_start_time: time | None = None
    actual_end_time: time | None = None
    final_status: str
    user_id: int
    category_id: int | None = None

class TaskResponse(BaseModel):
    id: int
    title: str
    task_date: date | None = None
    planned_start_time: time | None = None
    planned_end_time: time | None = None
    actual_start_time: time | None = None
    actual_end_time: time | None = None
    final_status: str
    user_id: int
    category_id: int | None = None