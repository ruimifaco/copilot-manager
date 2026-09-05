from pydantic import BaseModel, Field
from datetime import time

class recurringBlocks(BaseModel):
    title: str = Field(min_length=1, max_length=25)
    days_of_week: str = Field(min_length=1)
    start_time: time
    end_time: time
    is_fixed: bool = True
    user_id: int = Field(gt=0)
    category_id: int = Field(gt=0)

class blocksResponse(recurringBlocks):
    id: int = Field(gt=0)
