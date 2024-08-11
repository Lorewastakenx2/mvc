
from architecture.event.event import Event
from architecture.event.event_handler import EventHandler
from logs import event_logger as logger


from abc import abstractmethod


class i_EventDispatcher:


    @abstractmethod
    def register_handler(self, handler: EventHandler) -> None:
        """
        
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

    def register_event_handler(self, handler: EventHandler) -> None:

        if self.__event_handler:
            raise PermissionError
        
        self.__event_handler = handler

        logger.debug(
            msg=f'*** event handler registered *** event_dispatcher={self}, event_handler={handler}'
        )
        

    def dispatch_event(self, caller: object, event: Event, exception_handlers: dict={}) -> None:
        logger.debug(
            msg=f'*** dispatching event *** event_dispatcher={self}, event={event}'
        )
        self.__event_handler.handle_event(caller=caller, event=event, exception_handlers=exception_handlers)
    
