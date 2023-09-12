from abc import ABCMeta, abstractmethod
from typing import Any, Dict
from tqdm import tqdm
from metadata.variables import TaskGroupType, TaskType


class ModelTask(metaclass=ABCMeta):
    @abstractmethod
    def __init__(
        self,
        task_name: str,
        tasks: Dict[str, Any],
    ):
        if not isinstance(tasks, dict):
            raise Exception("tasks type must be dictionary")

        for task_group_type in TaskGroupType.__members__:
            if TaskType.sequence.value not in tasks.get(task_group_type).keys():
                raise Exception(f"sequence must be included in {task_group_type}")

        self.task_name = task_name
        self.tasks = tasks


class ModelExecutor(metaclass=ABCMeta):
    @abstractmethod
    def __init__(
        self,
        tasks: ModelTask,
        params: Dict[str, Any],
    ):
        self.task_name = tasks.task_name
        self.tasks = tasks.tasks

    def execute(self, process_name: str):
        _process = self.tasks.get(process_name)
        _sequence = _process.get(TaskType.sequence.value)
        self.task_result = {"params": self.params}
        progress_bar = tqdm(_sequence)
        progress_bar.set_description(process_name)
        for task_group, task in progress_bar:
            if task_group == TaskType.sql.value:
                print(f"{task_group}: {task} execute")  ##FIXME: logging
                ##TODO: execute sql
            elif task_group == TaskType.function.value:
                _task_result = _process.get(task_group).get(task)(**self.task_result)
                self.task_result.update(_task_result)
                print(f"{task_group}: {task} execute")  ##FIXME: logging
            else:
                raise Exception("task group is not verified")
