

import functools
from typing import Callable, Any, TypeVar




T = TypeVar('T', bound=Callable)
def overwrite_protection(func: T) -> T:

    @functools.wraps(func)
    def wrapper(*args: Any, override: bool=False, **kwargs: Any) -> None:
        try:
            err: Exception = func(*args, **kwargs)
            if err is PermissionError and not override:
                raise err
        except PermissionError as err:
            raise err
    
    return wrapper
