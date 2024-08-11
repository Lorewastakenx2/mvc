
from architecture.event.event import Event
from architecture.event.event_dispatcher import EventDispatcher
from logs import mvc_logger as logger


from abc import abstractmethod
from typing import Hashable

class i_Controllable:


    @abstractmethod
    def dispatch_event(self, event: Event, ignored_exceptions: tuple=()) -> None:
        """
        wrapper method for the owned event dispatcher
        """

    @property
    @abstractmethod
    def _event_dispatcher(self) -> EventDispatcher:
        """
        protected variable for event dispatcher.
        is accessed by controller for registration.
        """


class Controllable(i_Controllable):
    
    def __init__(self) -> None:
        logger.debug(
            msg=f'*** initializing Controllable *** controllable={self}'
        )
        self.__event_dispatcher: EventDispatcher = EventDispatcher()

    @property
    def _event_dispatcher(self) -> EventDispatcher:
        return self.__event_dispatcher

    def dispatch_event(self, event: Event, ignored_exceptions: tuple = ()) -> None:
        
        logger.debug(
            msg=f'*** dispatching event *** event_dispatcher={self}, event={event}, ignored_exceptions={ignored_exceptions}'
        )

        _event: Event = None
        if isinstance(event, Event):
            _event = event
        elif isinstance(event, str):
            _event = Event(identification=event)
        elif isinstance(event, Hashable):
            _event = Event(identification=event)
        else:
            raise ValueError

        self.__event_dispatcher.dispatch_event(caller=self, event=_event, ignored_exceptions=ignored_exceptions)
