
from architecture.event.event import Event
from architecture.event.event_callback import EventHandlerCallback
from logs import event_logger as logger

from abc import abstractmethod
from typing import Hashable, Callable, Union
from inspect import FullArgSpec, getfullargspec


t_Event = Union[Event, Hashable]

class errors:

    class NoRegisteredEventsError(Exception):
        def __init__(self, *args: object) -> None:
            super().__init__(*args)

    class EventNotRegisteredError(Exception):
        def __init__(self, *args: object) -> None:
            super().__init__(*args)



class i_EventHandler:

    @abstractmethod
    def register_callback(self, event_id: Hashable, callback: Callable) -> None:
        """
        
        """


    @abstractmethod
    def _handle_event(self, caller: object, event: t_Event, exception_handlers: dict={}) -> None:
        """
        protected method.
        should only be accessed by event dispatchers.
        """


class EventHandler(i_EventHandler):
    
    def __init__(self) -> None:
        logger.debug(
            msg=f'*** initializing EventHandler ***, event_handler={self}'
        )

        self.__registered_callbacks: dict = {}


    def register_callback(self, event_id: Hashable, callback: Callable) -> None:
        
        if event_id in self.__registered_callbacks:
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
        
        self.__registered_callbacks[event_id] = _callback

        logger.debug(
            msg=f'*** callback registered *** event_id={event_id}, callback={_callback}'
        )


    def _handle_event(self, caller: object, event: t_Event, exception_handlers: dict={}) -> None:

        logger.debug(
            msg=f'*** handling event *** handler={self}, caller={caller}, event={event}'
        )

        # if the sent event is not of type Event an event is created

        _event: Event = None
        if isinstance(event, Event):
            _event = event
        elif isinstance(event, Hashable):
            _event = Event(id=event)
        else:
            raise ValueError

        try:

            if not self.__registered_callbacks:
                raise errors.NoRegisteredEventsError
        
            if not event.event_id in self.__registered_callbacks:
                raise errors.EventNotRegisteredError

            callback: Callable = self.__registered_callbacks[event.event_id]
            callback(caller=caller, event=event)

        except Exception as err:

            logger.debug(
                msg=f'*** exception occurred while handling event *** caller={caller}, event={event}, exception={err}'
            )

            if isinstance(err, exception_handlers):
                exception_handler: Callable = exception_handlers[err.__class__]
                if exception_handler:
                    exception_handler()
                    logger.debug(
                        msg=f'*** exception handled ***'
                    )
                else:
                    logger.debug(
                        msg=f'*** exception ignored ***'
                    )                    
            else:
                raise err



