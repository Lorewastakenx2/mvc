
from architecture.event.event import Event
from architecture.event.event_dispatcher import EventDispatcher
from logs import mvc_logger as logger


from abc import abstractmethod
from typing import Hashable

"""
controllable is owned by controller.
controllable has no knowledge of controller.
controllable owns an event dispatcher which is linked to the controller's event handler.
"""


class i_Controllable:


    @abstractmethod
    def dispatch_event(self, event: Event, exception_handlers: tuple=()) -> None:
        """
        wrapper method for the owned event dispatcher.
        only exists to add the "caller" argument to the event dispatcher.
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

    def dispatch_event(self, event: Event, exception_handlers: dict={}) -> None:

        logger.debug(
            msg=f'*** dispatching event *** event_dispatcher={self}, event={event}, exception_handlers={exception_handlers}'
        )

        self.__event_dispatcher.dispatch_event(caller=self, event=event, exception_handlers=exception_handlers)
