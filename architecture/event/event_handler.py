
from architecture.event.event import Event
from architecture.event.event_handler_callback import EventHandlerCallback
from logs import event_logger as logger

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
        logger.debug(
            msg=f'*** initializing EventHandler ***, event_handler={self}'
        )
        self.__registered_callbacks: dict = {}


    def register_event_handler_callback(self, identification: Hashable, callback: Callable) -> None:
        
        if identification in self.__registered_callbacks:
            raise PermissionError
        
        self.__registered_callbacks[identification] = callback

        logger.debug(
            msg=f'*** callback registered *** identification={identification}, callback={callback}'
        )


    def handle_event(self, caller: object, event: Event, ignored_exceptions: tuple=()) -> None:

        logger.debug(
            msg=f'*** handling event *** handler={self}, caller={caller}, event={event}, ignored_exceptions={ignored_exceptions}'
        )

        if not self.__registered_callbacks:
            raise errors.NoRegisteredEventsError
        
        if not event.identification in self.__registered_callbacks:
            raise errors.EventNotRegisteredError


        callback: Callable = self.__registered_callbacks[event.identification]

        try:

            if isinstance(callback, EventHandlerCallback):
                callback(caller=caller, event=event)
            else:
                callback()

        except Exception as err:

            if isinstance(err, ignored_exceptions):
                logger.debug(
                    msg=f'*** ignored exception while handling event *** exception={err}'
                )
            else:
                raise err



