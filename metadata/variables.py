from enum import Enum


class TaskGroupType(str, Enum):
    preprocessing: str = "preprocessing"
    modeling: str = "modeling"
    prediction: str = "prediction"


class TaskType(Enum):
    sql: str = "sql"
    function: str = "function"
    sequence: str = "sequence"
