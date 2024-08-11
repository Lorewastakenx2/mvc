
from architecture.event.event import Event
from architecture.event.event_handler_callback import EventHandlerCallback

from abc import abstractmethod
from typing import Hashable, Callable


class errors:

    class NoRegisteredEventsError(Exception):
        def __init__(self, *args: object) -> None:
            super().__init__(*args)

    class EventNotRegisteredError(Exception):
        def __init__(self, *args: object) -> None:
            super().__init__(*args)


class i_EventHandler:

    @abstractmethod
    def register_event_handler_callback(self, identification: Hashable, callback: Callable) -> None:
        """
        
        """

    @abstractmethod
    def handle_event(self, caller: object, event: Event, ignored_exceptions: tuple=()) -> None:
        """
        
        """


class EventHandler(i_EventHandler):
    
    def __init__(self) -> None:
        
        self.__registered_callbacks: dict = {}

    def register_event_handler_callback(self, identification: Hashable, callback: Callable) -> None:
        if identification in self.__registered_callbacks:
            raise PermissionError
        self.__registered_callbacks[identification] = callback

    def handle_event(self, caller: object, event: Event, ignored_exceptions: tuple=()) -> None:

        if not self.__registered_callbacks:
            raise errors.NoRegisteredEventsError
        
        if event.identification in self.__registered_callbacks:
            raise errors.EventNotRegisteredError

        # ...