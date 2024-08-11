
from architecture.event.event import Event

import logging
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
        logging.log(
            level=logging.DEBUG, 
            msg=f'*** executing callback ***'
        )
        self.execute(caller=caller, event=event)

    @abstractmethod
    def execute(self, caller: object, event: Event) -> None:
        """
        
        """