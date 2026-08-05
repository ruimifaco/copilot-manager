from app.schemas.tasks import TaskCreate # Importa as regras definidas para os dados que serão usados nesse arquivo. Aqui é o schema de entrada.
from fastapi import APIRouter, HTTPException, status # app fica em main.py. Como tiramos a api de lá, precisamos expandir "app". Pra isso, usamos APIRouter.
from app.schemas.tasks import TaskResponse # Importa as regras definidas pra saída do schema de Tasks
from app.repositories.task_data import get_all_tasks, get_task_by_id, insert_task_db

router = APIRouter() # Atribui APIRouter a palavra "router".

@router.get ("/tasks")
def list_tasks():
    return {"status": "ok", "value": get_all_tasks()} # Isso é o que a API deve retornar em caso de sucesso

@router.get("/tasks/{id}")
def list_task_id(id: int):
    task_searched = get_task_by_id(id)
    if task_searched is None:
        raise HTTPException(status_code=404, detail="ID not found")
    return {"status": "ok", "value": task_searched}

@router.post ("/tasks", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def insert_task(task: TaskCreate):
    user_task_data = {
        "title": task.title,
        "task_date": task.task_date,
        "planned_start_time": task.planned_start_time,
        "planned_end_time": task.planned_end_time,
        "actual_start_time": task.actual_start_time,
        "actual_end_time": task.actual_end_time,
        "final_status": task.final_status,
        "user_id": task.user_id,
        "category_id": task.category_id
    }

    insert_user_task = insert_task_db(user_task_data)
    return insert_user_task
