
from architecture.event.event import Event
from logs import event_logger as logger


from abc import abstractmethod



class i_EventHandlerCallback:

    @abstractmethod
    def __call__(self, caller: object, event: Event) -> None:
        """
        
        """

    @abstractmethod
    def execute(self, caller: object, event: Event) -> None:
        """
        
        """


class EventHandlerCallback(i_EventHandlerCallback):

    def __call__(self, caller: object, event: Event) -> None:
        logger.debug(
            msg=f'*** executing callback *** caller={caller}, event={event}'
        )
        self.execute(caller=caller, event=event)
        logger.debug(
            msg=f'*** callback executed without errors ***'
        )


    @abstractmethod
    def execute(self, caller: object, event: Event) -> None:
        """
        
        """