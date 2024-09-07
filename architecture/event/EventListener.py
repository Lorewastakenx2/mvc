
from typing import Callable, Hashable
from inspect import FullArgSpec, getfullargspec

from .Event import Event


class EventNotRegisteredError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class EventListener:
    
    def __init__(self) -> None:
        
        self.__event_handlers: dict = {}
        self.__exception_handlers: dict = {}

    def trigger_event(self, event: Event, caller: object) -> None:
        
        try:
            self.__trigger_event(event=event, caller=caller)
        except Exception as err:
            if isinstance(err, tuple(self.__exception_handlers.keys())):

                exception_handler: Callable = self.__exception_handlers[type(err)]
                argspec: FullArgSpec = getfullargspec(exception_handler)

                kwargs: dict = {}
                if 'event' in argspec.args:
                    kwargs['event'] = event
                if 'caller' in argspec.args:
                    kwargs['caller'] = caller
                if 'err' in argspec.args:
                    kwargs['err'] = err

                exception_handler(**kwargs) 
            else:
                raise err

    def __trigger_event(self, event: Event, caller: object) -> None:

        if not event.trigger in self.__event_handlers:
            raise EventNotRegisteredError
        
        event_handler: Callable = self.__event_handlers[event.trigger]
        argspec: FullArgSpec = getfullargspec(event_handler)

        kwargs: dict = {}
        if 'event' in argspec.args:
            kwargs['event'] = event
        if 'caller' in argspec.args:
            kwargs['caller'] = caller

        event_handler(**kwargs)

    def register_event_handler(self, trigger: Hashable, handler: Callable) -> None:
    
        if trigger in self.__event_handlers:
            raise PermissionError
        
        self.__event_handlers[trigger] = handler

    def register_exception_handler(self, exception: Exception, handler: Callable) -> None:
        
        if exception in self.__exception_handlers:
            raise PermissionError

        self.__exception_handlers[exception] = handler
