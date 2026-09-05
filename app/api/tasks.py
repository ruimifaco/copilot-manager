from app.schemas.tasks import TaskCreate
from fastapi import APIRouter, HTTPException, status
from app.schemas.tasks import TaskResponse
from app.repositories.task_data import get_all_tasks, get_task_by_id, insert_task_db

router = APIRouter()

@router.get ("/tasks", response_model=list[TaskResponse])
def list_tasks():
    return get_all_tasks()

@router.get("/tasks/{id}", response_model=TaskResponse)
def list_task_id(id: int):
    task_searched = get_task_by_id(id)
    if task_searched is None:
        raise HTTPException(status_code=404, detail="ID not found")
    return task_searched

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
