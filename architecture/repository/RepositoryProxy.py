
from typing import Any

from .Field import Field
from .Repository import Repository


class RepositoryProxy:

    def __init__(self, repository: Repository, owner: Any) -> None:
        
        self.__repository: Repository = repository
        self.__owner: Any = owner

    def register_field(self, lvalue: str, field: Field) -> None:
        self.__repository.register_field(lvalue=lvalue, field=field, owner=self.__owner)

    def get(self, lvalue: str) -> Any:
        return self.__repository.get(lvalue=lvalue)
    
    def set(self, lvalue: str, rvalue: Any) -> None:
        self.__repository.set(lvalue=lvalue, rvalue=rvalue, caller=self.__owner)