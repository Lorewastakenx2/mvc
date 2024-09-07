


from typing import Any
from .Field import Field


class Registry:

    def __init__(self) -> None:
        
        self.__fields: dict = {}

    def register_field(self, lvalue: str, rvalue: Any, accessor: int) -> None:
        self.__fields[lvalue] = Field[type(rvalue)](value=rvalue, accessor=accessor)

    def get_field(self, lvalue: str) -> Field:
        return self.__fields[lvalue]
    







if __name__ == '__main__':

    reg = Registry()

    reg.register_field(lvalue='some_field', rvalue=1, accessor=1)
    reg.get_field(lvalue='some_field').modify(value=20, accessor=1)