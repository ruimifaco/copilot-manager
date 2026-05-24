from app.db.connection import engine # importa a variável do outro arquivo
from sqlalchemy import text # importa a função de texto do SQLAlchemy
from app.schemas.tasks import TaskCreate # Importa as regras definidas para os dados que serão usados nesse arquivo. Aqui é o schema de entrada.
from fastapi import APIRouter # app fica em main.py. Como tiramos a api de lá, precisamos expandir "app". Pra isso, usamos APIRouter.
from app.schemas.tasks import TaskResponse # Importa as regras definidas pra saída do schema de Tasks

router = APIRouter() # Atribui APIRouter a palavra "router".

@router.get ("/tasks")
def list_tasks():
    with engine.connect() as conn: # Apelida a conexão com o banco como "conn"
        db_result = conn.execute(text("SELECT id, title, task_date, planned_start_time, planned_end_time, actual_start_time, actual_end_time, final_status, user_id, category_id FROM tasks ORDER BY id;")) # Executa o SELECT em texto. Isso é a execução do SQL no banco.
        tasks = db_result.mappings().all() # transforma a tabela inteira em uma lista de dicionários
    return {"status": "ok", "value": tasks} # Isso é o que a API deve retornar em caso de sucesso

@router.get("/tasks/{id}")
def list_task_id(id: int):
    with engine.connect() as conn:
        list_id = conn.execute(text("SELECT id, title, task_date, planned_start_time, planned_end_time, actual_start_time, actual_end_time, final_status, user_id, category_id FROM tasks WHERE id = :id_searched"), {"id_searched": id})
        id_result = list_id.mappings().first() # mappings() transforma cada linha em um dicionário. all() manda devolver todos os registros.
    return {"status": "ok", "value": id_result}

@router.post ("/tasks", response_model=TaskResponse)
def insert_task(task: TaskCreate):
    with engine.begin() as conn:
        task_insert = conn.execute(text("INSERT INTO tasks (title, task_date, planned_start_time, planned_end_time, actual_start_time, actual_end_time, final_status, user_id, category_id) VALUES (:title, :task_date, :planned_start_time, :planned_end_time, :actual_start_time, :actual_end_time, :final_status, :user_id, :category_id) RETURNING id, title, task_date, planned_start_time, planned_end_time, actual_start_time, actual_end_time, final_status, user_id, category_id;"), {"title": task.title, "task_date": task.task_date, "planned_start_time": task.planned_start_time, "planned_end_time": task.planned_end_time, "actual_start_time": task.actual_start_time, "actual_end_time": task.actual_end_time, "final_status": task.final_status, "user_id": task.user_id, "category_id": task.category_id})
        insert_result = task_insert.mappings().one() # one() manda devolver apenas uma linha.
    return {insert_result}
