from app.db.connection import engine
from sqlalchemy import text
from app.db.sql_api import get_recurring_block_by_id_sql, get_recurring_blocks_sql
from app.db.transform_data import transform_query_in_dict, transform_query_in_dict_first


def get_all_recurring_blocks():
    with engine.connect() as conn:
        result_before_transformation = conn.execute(text(get_recurring_blocks_sql))
        result_after_transformation = transform_query_in_dict(result_before_transformation)
    return result_after_transformation


def get_recurring_block_by_id(id: int):
    with engine.connect() as conn:
        recurring_block_result = conn.execute(text(get_recurring_block_by_id_sql), {"id_searched": id})
        recurring_block = transform_query_in_dict_first(recurring_block_result)
    return recurring_block
