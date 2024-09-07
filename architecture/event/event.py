
from typing import Hashable


class Event:

    def __init__(self, trigger: Hashable, payload: dict=None) -> None:
        
        self.__trigger: Hashable = trigger
        self.__payload: dict = payload or {}

    @property
    def trigger(self) -> Hashable:
        return self.__trigger
    
    @property
    def payload(self) -> dict:
        return self.__payload
    
    def __str__(self) -> str:
        return f'Event(trigger={self.__trigger}, payload={self.__payload})'



