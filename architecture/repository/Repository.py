
from typing import Any

from .Accessor import Accessor
from .Field import Field


class Repository:

    def __init__(self) -> None:
        
        self.__accessor_lookup_table: dict = {}
        self.__fields: dict = {}

    def register_field(self, lvalue: str, field: Field, owner: Any) -> None:
        
        if lvalue in self.__fields:
            raise PermissionError
        
        if not owner in self.__accessor_lookup_table:
            self.__accessor_lookup_table[owner] = [Accessor()]

        field.add_accessor(self.__accessor_lookup_table[owner][0])
        self.__fields[lvalue] = field

    def get(self, lvalue: str) -> Any:

        if not lvalue in self.__fields:
            raise KeyError
        
        field: Field = self.__fields[lvalue]
        return field.rvalue
    
    def set(self, lvalue: str, rvalue: Any, caller: Any) -> None:

        if not lvalue in self.__fields:
            raise KeyError
        
        field: Field = self.__fields[lvalue]
        
        if not caller in self.__accessor_lookup_table:
            raise KeyError
        
        if not set(self.__accessor_lookup_table[caller]) & set(field.accessors):
            raise PermissionError
        
        field.rvalue = rvalue

