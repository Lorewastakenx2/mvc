

from architecture.event.EventDispatcher import EventDispatcher

from architecture.repository.Accessor import Accessor
from architecture.repository.Field import Field
from architecture.repository.Repository import Repository


class Controllable:

    def __init__(self) -> None:
        
        self.__accessor: Accessor = Accessor()
        self.__model_view_repository: Repository = None
        self.__event_dispatcher: EventDispatcher = EventDispatcher(owner=self) 
        
    @property
    def accessor(self) -> Accessor:
        return self.__accessor

    @property
    def model_view_repository(self) -> Repository:
        return self.__model_view_repository

    @property
    def event_dispatcher(self) -> EventDispatcher:
        return self.__event_dispatcher
    
    def register_model_view_repository(self, repository: Repository) -> None:
        self.__model_view_repository = repository
    


