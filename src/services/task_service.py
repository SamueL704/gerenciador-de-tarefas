from src.repositories.repository import *

def create_task_service(task):
    result = create_task(task.model_dump())
    return {"message": "tarefa salva", "id": str(result.inserted_id)}