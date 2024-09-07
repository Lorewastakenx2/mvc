
from typing import Any

from .Event import Event
from .EventBus import EventBus


class EventDispatcher:
    
    def __init__(self, owner: Any) -> None:
        
        self.__bus: EventBus = None
        self.__owner: Any = owner

    def register_bus(self, bus: EventBus) -> None:
        
        if not self.__manager is None:
            raise PermissionError
        
        self.__bus = bus

    #def register_default_caller(self, caller: object) -> None:

    #    if not self.__caller is None:
    #        raise PermissionError

    #    self.__caller = caller

    def dispatch_event(self, event: Event) -> None:
        self.__bus.notify_event(event=event, caller=self.__owner)

    def schedule_event_for_dispatch(self, event: Event) -> None:
        raise NotImplementedError
    
    def dispatch_scheduled_events(self) -> None:
        raise NotImplementedError