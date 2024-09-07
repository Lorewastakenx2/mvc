
from .Event import Event
from .EventListener import EventListener


class EventBus:

    def __init__(self) -> None:
        
        self.__listeners: list[EventListener] = []

    def add_listener(self, listener: EventListener) -> None:

        if listener in self.__listeners:
            raise PermissionError

        self.__listeners.append(listener)

    def notify_event(self, event: Event, caller: object) -> None:
        
        for listener in self.__listeners:
            listener.trigger_event(event=event, caller=caller)