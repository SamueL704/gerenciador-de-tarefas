from pydantic import BaseModel
from enum import Enum

class TaskStatus(str, Enum):
    pendente = "pendente"
    em_andamento = "em andamento"
    concluido = "concluido"

class TaskPrioridade(str, Enum):
    baixa = "baixa"
    media = "media"
    alta = "alta"

class Task(BaseModel):
    Titulo: str
    prioridade: TaskPrioridade
    status: TaskStatus
    vencimento: str