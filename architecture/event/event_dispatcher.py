
from architecture.event.event import Event
from architecture.event.event_handler import EventHandler
from architecture.event.exception_handler import ExceptionHandler
from logs import event_logger as logger


from abc import abstractmethod
from typing import Callable
from inspect import FullArgSpec, getfullargspec

class i_EventDispatcher:


    @abstractmethod
    def register_handler(self, handler: EventHandler) -> None:
        """
        raises a "PermissionError" if handler is already registered.
        Dynamic registration is therefore prevented. 
        """

    @abstractmethod
    def register_standard_exception_handler(self, exception: Exception, handler: Callable) -> None:
        """
        standard exception handler that is tied to; and owned by the dispatcher.
        the dispatcher will use these handlers when dispatching events, unless overwritten by
        the field "exception_handlers" in "dispatch_event".
        """


    @abstractmethod
    def dispatch_event(self, caller: object, event: Event, exception_handlers: dict={}) -> None:
        """
        
        """



class EventDispatcher(i_EventDispatcher):
    
    def __init__(self) -> None:
        logger.debug(
            msg=f'*** initializing EventDispatcher *** event_dispatcher={self}'
        )

        self.__event_handler: EventHandler = None
        self.__standard_exception_handlers: dict = {}

    def register_event_handler(self, handler: EventHandler) -> None:

        if self.__event_handler:
            raise PermissionError
        
        self.__event_handler = handler

        logger.debug(
            msg=f'*** event handler registered *** event_dispatcher={self}, event_handler={handler}'
        )

    def register_standard_exception_handler(self, exception: type, handler: Callable) -> None:

        _handler: ExceptionHandler = None
        if isinstance(handler, ExceptionHandler):
            _handler = handler
        elif isinstance(handler, Callable):
            
            # if the registered exception handler is not of type ExceptionHandler, 
            # a wrapper is created dynamically in order to use the functionality
            # of the ExceptionHandler class

            class ExceptionHandlerWrapper(ExceptionHandler):

                def __init__(self) -> None:
                    self.__argspec: FullArgSpec = getfullargspec(handler)

                def execute(self, caller: object, event: Event, err: Exception) -> None:
                    kwargs: dict = {}
                    if 'caller' in self.__argspec.args:
                        kwargs['caller'] = caller
                    if 'event' in self.__argspec.args:
                        kwargs['event'] = event
                    if 'err' in self.__argspec.args:
                        kwargs['err'] = err
                    handler(**kwargs)

            _handler = ExceptionHandlerWrapper()
        else:
            raise ValueError

        self.__standard_exception_handlers[exception] = _handler
        

    def dispatch_event(self, caller: object, event: Event, exception_handlers: dict={}) -> None:
        logger.debug(
            msg=f'*** dispatching event *** event_dispatcher={self}, event={event}'
        )
        self.__event_handler._handle_event(caller=caller, event=event, exception_handlers=self.__standard_exception_handlers | exception_handlers)
    
