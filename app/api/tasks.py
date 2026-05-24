from app.db.connection import engine # importa a variável do outro arquivo
from sqlalchemy import text # importa a função de texto do SQLAlchemy
from app.schemas.tasks import TaskCreate
from fastapi import APIRouter


router = APIRouter()

@router.get ("/tasks")
def list_tasks():
    with engine.connect() as conn: # Apelida a conexão com o banco como "conn"
        db_result = conn.execute(text("SELECT id, title, days_of_week, start_time, end_time, is_fixed, user_id, category_id FROM tasks ORDER BY id;"))
        tasks = db_result.mappings().all() # transforma a tabela inteira em uma lista de dicionários
    return {"status": "ok", "value": tasks}

@router.post ("/tasks")
def insert_task(task: TaskCreate):
    with engine.begin() as conn:
        task_insert = conn.execute(text("INSERT INTO tasks (title, days_of_week, start_time, end_time, is_fixed, user_id, category_id) VALUES (:title, :days_of_week, :start_time, :end_time, :is_fixed, :user_id, :category_id RETURNING id, title, days_of_week, start_time, end_time, is_fixed, user_id, category_id;"), {"title": task.title, "days_of_week": task.days_of_week, "start_time": task.start_time, "end_time": task.end_time, "is_fixed": task.is_fixed, "user_id": task.user_id, "category_id": task.category_id})
        insert_result = task_insert.mappings().one()
    return {"status": "ok", "value": insert_result}
