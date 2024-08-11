
from architecture.event.event import Event
from logs import event_logger as logger

from abc import ABC, abstractmethod
from typing import Any



class i_ExceptionHandler:

    @abstractmethod
    def __call__(self, caller: object, event: Event, err: Exception) -> None:
        """
        
        """
    
    @abstractmethod
    def execute(self, caller: object, event: Event, err: Exception) -> None:
        """
        
        """


class ExceptionHandler(ABC, i_ExceptionHandler):

    def __call__(self, caller: object, event: Event, err: Exception) -> None:
        logger.debug(
            msg=f'*** handling exception *** handler={self}, caller={caller}, event={event}, err={err}'
        )
        self.execute(caller=caller, event=event, err=err)
        logger.debug(
            msg=f'*** exception handled without errors ***'
        )

    @abstractmethod
    def execute(self, caller: object, event: Event, err: Exception) -> None:
        pass