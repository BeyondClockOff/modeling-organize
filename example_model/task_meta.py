from typing import Any, Dict
from metadata.abstract import ModelTask, ModelExecutor


class ExampleTask(ModelTask):
    def __init__(
        self,
        task_name: str,
        tasks: Dict[str, Any],
    ):
        super().__init__(
            task_name=task_name,
            tasks=tasks,
        )


class ExampleExecutor(ModelExecutor):
    def __init__(
        self,
        tasks: ExampleTask,
    ):
        super().__init__(
            tasks=tasks,
        )

    def preprocessing(self):
        super().execute(process_name="preprocessing")

    def modeling(self):
        super().execute(process_name="modeling")

    def prediction(self):
        super().execute(process_name="prediction")
