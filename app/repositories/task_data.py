from app.db.connection import engine
from sqlalchemy import text
from app.db.sql_api import get_tasks_sql
from app.db.transform_data import transform_query_in_dict


def get_all_tasks():
    with engine.connect() as conn:
        result_before_transformation = conn.execute(text(get_tasks_sql))
        result_after_transformation = transform_query_in_dict(result_before_transformation)
    return result_after_transformation
