#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2024-08-17 11:21:00
# @Author  : Your Name (you@example.org)
# @Link    : link
# @Version : 1.0.0


"""
Event
"""


from abc import abstractmethod
from typing import Any, Callable, Hashable


class i_Event:

    @property
    @abstractmethod
    def trigger(self) -> Hashable:
        """
        
        """
        
    @property
    @abstractmethod
    def payload(self) -> dict:
        """
        
        """


    @abstractmethod
    def __str__(self) -> str:
        """
        
        """


class Event(i_Event):

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


