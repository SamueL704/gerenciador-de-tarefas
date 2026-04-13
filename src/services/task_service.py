from src.repositories.repository import *

def format_task(task):
    task["_id"] = str(task["_id"])
    return task

def create_task_service(task):
    result = create_task(task.model_dump())
    return {"message": "tarefa salva", "id": str(result.inserted_id)}

def get_all_tasks_service():
    tasks = get_all_tasks()
    print(get_all_tasks())
    return [format_task(task) for task in tasks]