from app.db.connection import engine # importa a variável do outro arquivo
from sqlalchemy import text # importa a função de texto do SQLAlchemy
from app.schemas.tasks import TaskCreate
from fastapi import APIRouter


router = APIRouter()

@router.get ("/tasks")
def list_tasks():
    with engine.connect() as conn: # Apelida a conexão com o banco como "conn"
        db_result = conn.execute(text("SELECT id, title, task_date, planned_start_time, planned_end_time, actual_start_time, actual_end_time, final_status, user_id, category_id FROM tasks ORDER BY id;"))
        tasks = db_result.mappings().all() # transforma a tabela inteira em uma lista de dicionários
    return {"status": "ok", "value": tasks}

@router.post ("/tasks")
def insert_task(task: TaskCreate):
    with engine.begin() as conn:
        task_insert = conn.execute(text("INSERT INTO tasks (title, task_date, planned_start_time, planned_end_time, actual_start_time, actual_end_time, final_status, user_id, category_id) VALUES (:title, :task_date, :planned_start_time, :planned_end_time, :actual_start_time, :actual_end_time, :final_status, :user_id, :category_id) RETURNING id, title, task_date, planned_start_time, planned_end_time, actual_start_time, actual_end_time, final_status, user_id, category_id;"), {"title": task.title, "task_date": task.task_date, "planned_start_time": task.planned_start_time, "planned_end_time": task.planned_end_time, "actual_start_time": task.actual_start_time, "actual_end_time": task.actual_end_time, "final_status": task.final_status, "user_id": task.user_id, "category_id": task.category_id})
        insert_result = task_insert.mappings().one()
    return {"status": "ok", "value": insert_result}
