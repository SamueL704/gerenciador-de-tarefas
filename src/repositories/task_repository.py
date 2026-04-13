from src.database.mongo import task_collection
from bson import ObjectId

def create_task(task):
    return task_collection.insert_one(task)

def get_all_tasks():
    return list(task_collection.find())

def get_task_by_id(id_task):
    return task_collection.find_one({"_id": ObjectId(id_task)})