from typing import Any, Dict
from metadata.variables import TaskGroupType
from metadata.abstract import ModelTask, ModelExecutor


class ExampleTask(ModelTask):
    def __init__(
        self,
        task_name: str,
        task_info: Dict[str, Any],
    ):
        super().__init__(
            task_name=task_name,
            task_info=task_info,
        )


class ExampleExecutor(ModelExecutor):
    def __init__(
        self,
        task: ExampleTask,
        params: Dict[str, Any] = {},
    ):
        super().__init__(
            task=task,
            params=params,
        )

    def preprocessing(self):
        super().execute(process_name=TaskGroupType.preprocessing.value)

    def modeling(self):
        super().execute(process_name=TaskGroupType.modeling.value)

    def prediction(self):
        super().execute(process_name=TaskGroupType.prediction.value)
