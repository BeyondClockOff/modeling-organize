from functools import wraps


def model_wrapper(function):
    @wraps(function)
    def wrapped(*args, **kwargs):
        _results = function(*args, **kwargs)
        if not isinstance(_results, dict):
            raise Exception("Output type must be dict")
        return _results

    return wrapped
