from typing import Dict
from metadata.wrapper import model_wrapper


@model_wrapper
def set_variables(**kwargs) -> Dict[str, int]:
    return {
        "x": 2,
        "y": 3,
    }


@model_wrapper
def add_one_x(x: int, **kwargs) -> Dict[str, int]:
    return {
        "x": x + 1,
    }
