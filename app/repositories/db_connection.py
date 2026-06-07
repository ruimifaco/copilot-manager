from app.db.connection import engine # importa a variável do outro arquivo
from sqlalchemy import text # importa a função de texto do SQLAlchemy
from app.db.sql_api import get_category_sql


def category_db_connection(sql):
    with engine.connect() as conn:
        result_before_transformation = conn.execute(text(sql)) # .scalar() ausente porque eu pedi a tabela inteira
    return result_before_transformation