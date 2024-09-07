
from typing import Any

from .Controllable import Controllable
from .event.EventDispatcher import EventDispatcher
from .repository.Field import Field
from .repository.Repository import Repository
from .repository.RepositoryProxy import RepositoryProxy


class Model(Controllable):

    def __init__(self) -> None:
        Controllable.__init__(self)

        self.__repository_proxy: RepositoryProxy = None
        self._fields: dict[str, Field] = {}

    @property
    def repository(self) -> RepositoryProxy:
        return self.__repository_proxy

    def __setattr__(self, name: str, value: Any) -> None:
        
        try:
            fields: dict[str, Field] = object.__getattribute__(self, '_fields')
        except AttributeError:
            object.__setattr__(self, name, value)
            return

        if name in fields:
            fields[name].rvalue = value
            return            
        object.__setattr__(self, name, value)

    def __getattribute__(self, name: str) -> Any:
        
        try:
            fields: dict[str, Field] = object.__getattribute__(self, '_fields')
        except AttributeError:
            return object.__getattribute__(self, name)

        if name in fields:
            return fields[name].rvalue
        return object.__getattribute__(self, name)

    def register_repository(self, repository: Repository) -> None:

        if not self.__repository_proxy is None:
            raise PermissionError
        
        self.__repository_proxy = RepositoryProxy(repository=repository, owner=self)
        for lvalue, field in self._fields.items():
            self.__repository_proxy.register_field(lvalue=lvalue, field=field)
