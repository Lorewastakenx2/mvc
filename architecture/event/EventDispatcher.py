#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2024-08-17 11:19:59
# @Author  : Your Name (you@example.org)
# @Link    : link
# @Version : 1.0.0


"""
EventDispatcher
"""

from architecture.event.Event import Event
from architecture.event.EventManager import EventManager

from architecture.misc import overwrite_protection


from abc import abstractmethod
from typing import Any, Callable, Hashable



class i_EventDispatcher:
    

    @overwrite_protection
    @abstractmethod
    def register_manager(self, manager: EventManager) -> Exception:
        """
        
        """

    @overwrite_protection
    @abstractmethod
    def register_caller(self, caller: object) -> Exception:
        """
        
        """


    @abstractmethod
    def dispatch_event(self, event: Event) -> None:
        """
        
        """



class EventDispatcher(i_EventDispatcher):
    
    def __init__(self) -> None:
        
        self.__manager: EventManager = None
        self.__caller: object = None


    @overwrite_protection
    def register_manager(self, manager: EventManager) -> Exception:
        
        err: Exception = None
        if self.__manager:
            err = PermissionError

        self.__manager = manager
        return err


    @overwrite_protection
    def register_caller(self, caller: object) -> Exception:

        err: Exception = None
        if self.__caller:
            err = PermissionError

        self.__caller = caller
        return err


    def dispatch_event(self, event: Event) -> None:
        self.__manager.notify_event(event=event, caller=self.__caller)


