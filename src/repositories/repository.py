from src.database.mongo import task_collection

def create_task(task):
    return task_collection.insert_one(task)

def get_all_tasks():
    return list(task_collection.find())
