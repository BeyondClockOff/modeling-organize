from example_model.task_meta import ExampleTask, ExampleExecutor
from example_model.example_functions import set_variables, add_one_x
from metadata.variables import TaskGroupType, TaskType


example_task = ExampleTask(
    task_name="example",
    tasks={
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
                "set_variables": set_variables,
                "add_one_x": add_one_x,
            },
            TaskType.sequence.value: [
                (TaskType.sql.value, "sql1"),
                (TaskType.function.value, "set_variables"),
                (TaskType.function.value, "add_one_x"),
            ],
        },
    },
)

example_executor = ExampleExecutor(tasks=example_task)

example_executor.preprocessing()
example_executor.modeling()
example_executor.task_result
