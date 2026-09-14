from datetime import date, time
from typing import Literal

from pydantic import BaseModel, Field


class ScheduledTask(BaseModel):
    item_type: Literal["task"]
    id: int = Field(gt=0)
    title: str = Field(min_length=1, max_length=40)
    start_time: time
    end_time: time | None = None
    category_id: int | None = Field(default=None, gt=0)
    final_status: Literal["To Do", "In progress", "Completed"]


class ScheduledRecurringBlock(BaseModel):
    item_type: Literal["recurring_block"]
    id: int = Field(gt=0)
    title: str = Field(min_length=1, max_length=25)
    start_time: time
    end_time: time
    category_id: int = Field(gt=0)
    is_fixed: bool


class UnscheduledTask(BaseModel):
    id: int = Field(gt=0)
    title: str = Field(min_length=1, max_length=40)
    final_status: Literal["To Do", "In progress", "Completed"]
    category_id: int | None = Field(default=None, gt=0)


class DailyPlanResponse(BaseModel):
    selected_date: date
    weekday: Literal[
        "segunda",
        "terça",
        "quarta",
        "quinta",
        "sexta",
        "sábado",
        "domingo",
    ]
    scheduled_items: list[ScheduledTask | ScheduledRecurringBlock] = Field(
        default_factory=list
    )
    unscheduled_tasks: list[UnscheduledTask] = Field(default_factory=list)
