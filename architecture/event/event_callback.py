
from architecture.event.event import Event
from logs import event_logger as logger


from abc import ABC, abstractmethod
from typing import Any


class i_EventHandlerCallback:

    @abstractmethod
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        
        """


    @abstractmethod
    def execute(self, caller: object, event: Event) -> None:
        """
        
        """


class EventHandlerCallback(ABC, i_EventHandlerCallback):

    @abstractmethod
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        pass

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
        pass