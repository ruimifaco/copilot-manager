from app.db.connection import engine
from sqlalchemy import text
from app.db.sql_api import get_category_sql
from app.db.transform_data import transform_query_in_dict
from app.db.sql_api import get_category_by_id_sql
from app.db.transform_data import transform_query_in_dict_first
from app.db.sql_api import post_category_sql
from app.db.transform_data import transform_query_in_dict_one


def get_all_categories():
    with engine.connect() as conn:
        result_before_transformation = conn.execute(text(get_category_sql))
        result_after_transformation = transform_query_in_dict(result_before_transformation)
    return result_after_transformation

def get_category_by_id(id: int):
    with engine.connect() as conn:
        categories_id = conn.execute(text(get_category_by_id_sql), {"id_searched": id})
        id_result = transform_query_in_dict_first(categories_id)
    return id_result

def insert_category_db(insert_category_data: dict):
    with engine.begin() as conn:
        category_insert = conn.execute(text(post_category_sql), insert_category_data)
        insert_result = transform_query_in_dict_one(category_insert)
    return insert_result
