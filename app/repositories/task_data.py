from app.db.connection import engine
from sqlalchemy import text
from app.db.sql_api import get_task_by_id_sql, get_tasks_sql, post_task_sql
from app.db.transform_data import transform_query_in_dict, transform_query_in_dict_first, transform_query_in_dict_one


def get_all_tasks():
    with engine.connect() as conn:
        result_before_transformation = conn.execute(text(get_tasks_sql))
        result_after_transformation = transform_query_in_dict(result_before_transformation)
    return result_after_transformation


def get_task_by_id(id: int):
    with engine.connect() as conn:
        task_result = conn.execute(text(get_task_by_id_sql), {"id_searched": id})
        task = transform_query_in_dict_first(task_result)
    return task


def insert_task_db(insert_task_data: dict):
    with engine.begin() as conn:
        task_insert = conn.execute(text(post_task_sql), insert_task_data)
        insert_result = transform_query_in_dict_one(task_insert)
    return insert_result
