

from abc import abstractmethod
from typing import Hashable


class i_Event:

    @property
    @abstractmethod
    def id(self) -> Hashable:
        """
        
        """

    @property
    @abstractmethod
    def payload(self) -> dict:
        """
        
        """


class Event(i_Event):
    
    def __init__(self, id: Hashable, payload: dict={}) -> None:
        
        self.__id: Hashable = id
        self.__payload: dict = payload

    def __hash__(self) -> int:
        return hash(self.__id)
    
    def __str__(self) -> str:
        return f'Event(id={self.__id}, payload={self.__payload})'
    
    @property
    def id(self) -> Hashable:
        return self.__id

    @property
    def payload(self) -> dict:
        return self.__payload



