
from architecture.event.event_dispatcher import EventDispatcher

from abc import abstractmethod


class i_Controllable:


    @property
    @abstractmethod
    def event_dispatcher(self) -> EventDispatcher:
        """
        
        """

class Controllable(i_Controllable):
    
    def __init__(self) -> None:
    
        self.__event_dispatcher: EventDispatcher = EventDispatcher()

    @property
    def event_dispatcher(self) -> EventDispatcher:
        return self.__event_dispatcher
