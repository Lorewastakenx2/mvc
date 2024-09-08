
from typing import Any

from .Event import Event
from .EventBus import EventBus


class EventDispatcher:
    
    def __init__(self, owner: Any) -> None:
        
        self.__bus: EventBus = None
        self.__owner: Any = owner

        self.__scheduled_events: list[Event] = []

    def register_bus(self, bus: EventBus) -> None:
        
        if not self.__bus is None:
            raise PermissionError
        
        self.__bus = bus

    #def register_default_caller(self, caller: object) -> None:

    #    if not self.__caller is None:
    #        raise PermissionError

    #    self.__caller = caller

    def dispatch_event(self, event: Event) -> None:
        try:
            self.__bus.notify_event(event=event, caller=self.__owner)
        except AttributeError:
            print(f'event dispatcher owned by {self.__owner} missing event bus. \nignoring dispatch of {event}.')

    def schedule_event_for_dispatch(self, event: Event) -> None:
        self.__scheduled_events.append(event)
    
    def dispatch_scheduled_events(self) -> None:

        for event in self.__scheduled_events:
            self.__scheduled_events.remove(event)
            self.dispatch_event(event=event)