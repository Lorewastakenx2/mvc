



from typing import Any, TypeVar, Generic


T = TypeVar('T')
class Field(Generic[T]):

    def __init__(self, value: T, accessor: int) -> None:

        self.__value: T = value
        self.__accessor: int = accessor


    @property
    def value(self) -> T:
        return self.__value


    def modify(self, value: T, accessor: int) -> None:

        if self.__accessor and self.__accessor != accessor:
            raise PermissionError

        self.__value = value