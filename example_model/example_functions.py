from typing import Dict
from metadata.wrapper import model_wrapper


@model_wrapper
def add_one_x(x: int, **kwargs) -> Dict[str, int]:
    return {
        "x": x + 1,
    }
