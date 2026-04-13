from pymongo import MongoClient 

MONGO_URL = "mongodb://localhost:27018"

client = MongoClient()

db = client["Tarefas"]

task_collection = db["tesks"]