# app/schemas: Nessa pasta ficam os Schemas do Pydantic (as classes que herdam de BaseModel). Schema é uma estrutura que organiza e define regras para dados

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

class blocksResponse(BaseModel):
    id: int
    title: str
    days_of_week: str
    start_time: time
    end_time: time
    is_fixed: bool = True
    user_id: int
    category_id: int