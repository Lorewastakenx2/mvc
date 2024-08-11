

from abc import abstractmethod
from typing import Hashable


class i_Event:

    @property
    @abstractmethod
    def identification(self) -> Hashable:
        """
        
        """

    @property
    @abstractmethod
    def payload(self) -> dict:
        """
        
        """


class Event(i_Event):
    
    def __init__(self, identification: Hashable, payload: dict={}) -> None:
        
        self.__identification: Hashable = identification
        self.__payload: dict = payload

    def __hash__(self) -> int:
        return hash(self.__identification)
    
    @property
    def identification(self) -> Hashable:
        return self.__identification

    @property
    def payload(self) -> dict:
        return self.__payload



