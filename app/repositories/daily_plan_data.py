from app.db.connection import engine
from app.db.transform_data import transform_query_in_dict
from app.db.sql_api import get_user_daily_plan_tasks_by_date_sql
from sqlalchemy import text
from datetime import date


def get_user_daily_plan_tasks_by_date(user_id: int, selected_date: date):
    with engine.connect() as conn:
        daily_plan_tasks = conn.execute(text(get_user_daily_plan_tasks_by_date_sql), {"user_id": user_id, "date_searched": selected_date})
        tasks_result = transform_query_in_dict(daily_plan_tasks)
    return tasks_result