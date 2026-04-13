from pymongo import MongoClient 
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URL = "mongodb://localhost:27018"


client = MongoClient(os.getenv("MONGO_ONLINE"))

db = client["Tarefas"]

task_collection = db["tesks"]