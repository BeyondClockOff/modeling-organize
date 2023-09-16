from typing import Any, Dict
from tqdm import tqdm
from metadata.variables import TaskGroupType, TaskType


class ModelTask:
    def __init__(
        self,
        task_name: str,
        task_info: Dict[str, Any],
    ):
        if not isinstance(task_info, dict):
            raise Exception("Type of tasks must be dictionary")

        for task_group_type in TaskGroupType.__members__:
            if (
                task_group_type in task_info.keys()
                and TaskType.sequence.value not in task_info.get(task_group_type).keys()
            ):
                raise Exception(f"sequence must be included in {task_group_type}")

        self.task_name = task_name
        self.task_info = task_info


class ModelExecutor:
    def __init__(
        self,
        task: ModelTask,
        params: Dict[str, Any],
    ):
        self.task_name = task.task_name
        self.task_info = task.task_info
        self.task_outputs = {}
        self.task_outputs.update(params)

    def execute(self, process_name: str):
        _process = self.task_info.get(process_name)
        _sequence = _process.get(TaskType.sequence.value)

        progress_bar = tqdm(_sequence)
        progress_bar.set_description(process_name)
        for task_group, task in progress_bar:
            if task_group == TaskType.sql.value:
                print(f"{task_group}: {task} execute")  ##FIXME: logging
                ##TODO: execute sql
            elif task_group == TaskType.function.value:
                _task_output = _process.get(task_group).get(task)(**self.task_outputs)
                self.task_outputs.update(_task_output)
                print(f"{task_group}: {task} execute")  ##FIXME: logging
            else:
                raise Exception("task group is not verified")
