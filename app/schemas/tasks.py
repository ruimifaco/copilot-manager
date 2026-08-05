# app/schemas: Nessa pasta ficam os Schemas do Pydantic (as classes que herdam de BaseModel). Schema é uma estrutura que organiza e deifine regras para dados

from datetime import date
from pydantic import BaseModel, Field
from datetime import time
from typing import Literal

class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=40)
    task_date: date | None = None
    planned_start_time: time | None = None
    planned_end_time: time | None = None
    actual_start_time: time | None = None
    actual_end_time: time | None = None
    final_status: Literal["To Do", "In progress", "Completed"]
    user_id: int = Field(gt=0)
    category_id: int | None = Field(default=None, gt=0)

class TaskResponse(TaskCreate):
    id: int = Field(gt=0)
