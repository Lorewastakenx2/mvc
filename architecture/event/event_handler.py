
from architecture.event.event import Event
from architecture.event.event_handler_callback import EventHandlerCallback
from logs import event_logger as logger

from abc import abstractmethod
from typing import Hashable, Callable
from inspect import FullArgSpec, getfullargspec

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
        
        _callback: EventHandlerCallback = None
        if isinstance(callback, EventHandlerCallback):
            _callback = callback
        else:

            # if the registered callback is not of type EventHandlerCallback, 
            # a wrapper is created dynamically in order to use the functionality,
            # of the EvenHandlerCallback class

            logger.debug(
                msg=f'*** creating callback wrapper for insufficient callback *** insufficient_callback={callback}'
            )

            class EventHandlerCallbackWrapper(EventHandlerCallback):

                def execute(self, caller: object, event: Event) -> None:
                    
                    argspec: FullArgSpec = getfullargspec(callback)
                    if 'caller' in argspec.args and 'event' in argspec.args:
                        callback(caller=caller, event=event)
                    elif 'caller' in argspec.args:
                        callback(caller=caller)
                    elif 'event' in argspec.args:
                        callback(event=event)
                    else:
                        callback()
            
            _callback = EventHandlerCallbackWrapper()
        
        self.__registered_callbacks[identification] = _callback

        logger.debug(
            msg=f'*** callback registered *** identification={identification}, callback={_callback}'
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

            callback(caller=caller, event=event)

        except Exception as err:

            if isinstance(err, ignored_exceptions):
                logger.debug(
                    msg=f'*** ignored exception while handling event *** exception={err}'
                )
            else:
                raise err



