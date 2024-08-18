#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2024-08-17 11:53:17
# @Author  : Your Name (you@example.org)
# @Link    : link
# @Version : 1.0.0


"""
Controllable
"""

from architecture.event.EventDispatcher import EventDispatcher

from abc import abstractmethod
from typing import Any, Callable, Hashable


class i_Controllable:


    @property
    @abstractmethod
    def event_dispatcher(self) -> EventDispatcher:
        """
        
        """


class Controllable(i_Controllable):
    
    def __init__(self) -> None:
        
        self.__event_dispatcher: EventDispatcher = EventDispatcher()
        self.__event_dispatcher.register_caller(caller=self)

    @property
    def event_dispatcher(self) -> EventDispatcher:
        return self.__event_dispatcher


