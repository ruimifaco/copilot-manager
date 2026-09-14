from datetime import date

from sqlalchemy import text

from app.db.connection import engine
from app.db.sql_api import (
    get_user_daily_plan_recurring_blocks_by_weekday_sql,
    get_user_daily_plan_tasks_by_date_sql,
)
from app.db.transform_data import transform_query_in_dict


def get_user_daily_plan_tasks_by_date(user_id: int, selected_date: date):
    with engine.connect() as conn:
        daily_plan_tasks = conn.execute(
            text(get_user_daily_plan_tasks_by_date_sql),
            {"user_id": user_id, "date_searched": selected_date},
        )
        tasks_result = transform_query_in_dict(daily_plan_tasks)
    return tasks_result


def get_user_daily_plan_recurring_blocks_by_weekday(user_id: int, weekday: str):
    with engine.connect() as conn:
        daily_plan_recurring_blocks = conn.execute(
            text(get_user_daily_plan_recurring_blocks_by_weekday_sql),
            {"user_id": user_id, "weekday_searched": weekday},
        )
        recurring_blocks_result = transform_query_in_dict(daily_plan_recurring_blocks)
    return recurring_blocks_result
