from src.repositories.task_repository import *

def format_task(task):
    task["_id"] = str(task["_id"])
    return task

def create_task_service(task):
    result = create_task(task.model_dump())
    return {"message": "tarefa salva", "id": str(result.inserted_id)}

def get_all_tasks_service():
    tasks = get_all_tasks()
    return [format_task(task) for task in tasks]

def get_task_by_id_service(id_task):
    try:
        task = get_task_by_id(id_task)
    except:
        return {"erro: id inválido"}
    
    if not task:
        return {"erro": "tarefa não encontrada"}

    return format_task(task)

def update_task_service(id_task, data_dict):
    try:
        data = data_dict.model_dump(exclude_unset=True)
        if not data:
            return {"Nenhum dado inserido"}
        
        result = update_task(id_task, data)
        
        if result.matched_count == 0:
            return {"erro": "tarefa não encontrada"}
    
    except Exception as e:
        return {"erro": str(e)}

    return {"message": "terefa atualizada"}