

from typing import Generic, TypeVar

from .Accessor import Accessor


T = TypeVar('T')
class Field(Generic[T]):

    def __init__(self, rvalue: T=None) -> None:

        self.__rvalue: T = rvalue
        self.__accessors: list = []

    @property
    def rvalue(self) -> T:
        return self.__rvalue
    
    @rvalue.setter
    def rvalue(self, value: T) -> None:

        if not self.__rvalue is None and not isinstance(value, self.__rvalue.__class__):
            raise TypeError
        
        self.__rvalue = value

    @property
    def accessors(self) -> list:
        return self.__accessors

    def add_accessor(self, accessor: Accessor) -> None:
        self.__accessors.append(accessor)

    def remove_accessor(self, accessor: Accessor) -> None:
        self.__accessors.pop(accessor)