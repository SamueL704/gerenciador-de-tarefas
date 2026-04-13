from fastapi import APIRouter
from src.schemas.taskDTO import Task
from src.services.task_service import *

router = APIRouter()

@router.post("/tasks")
def create_task(task_dict: Task):
    return create_task_service(task_dict)

@router.get("/tasks")
def get_all_tasks():
    return get_all_tasks_service()