from metadata.variables import TaskGroupType, TaskType
from example_model.task_meta import ExampleTask, ExampleExecutor
from example_model.example_functions import add_one_x


example_task = ExampleTask(
    task_name="example",
    task_info={
        TaskGroupType.preprocessing.value: {
            TaskType.sql.value: {
                "sql1": "sql1.sql",
                "sql2": "sql2.sql",
            },
            TaskType.sequence.value: [
                (TaskType.sql.value, "sql1"),
                (TaskType.sql.value, "sql2"),
            ],
        },
        TaskGroupType.modeling.value: {
            TaskType.sql.value: {
                "sql1": "sql1.sql",
            },
            TaskType.function.value: {
                "add_one_x": add_one_x,
            },
            TaskType.sequence.value: [
                (TaskType.sql.value, "sql1"),
                (TaskType.function.value, "add_one_x"),
                (TaskType.function.value, "add_one_x"),
                (TaskType.function.value, "add_one_x"),
            ],
        },
    },
)

example_executor = ExampleExecutor(
    task=example_task,
    params={
        "x": 1,
        "y": 3,
    },
)

example_executor.preprocessing()
example_executor.modeling()
example_executor.task_outputs
