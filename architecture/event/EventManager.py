#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2024-08-17 11:19:49
# @Author  : Your Name (you@example.org)
# @Link    : link
# @Version : 1.0.0


"""
EventManager
"""

from architecture.event.Event import Event
from architecture.event.EventListener import EventListener

from architecture.misc import overwrite_protection

from abc import abstractmethod
from typing import Any, Callable, Hashable


class i_EventManager:


    @overwrite_protection
    @abstractmethod
    def register_listener(self, listener: EventListener) -> Exception:
        """
        
        """


    @abstractmethod
    def notify_event(self, event: Event, caller: object) -> None:
        """
        
        """


class EventManager(i_EventManager):

    def __init__(self) -> None:
        
        self.__listeners: list = []


    @overwrite_protection
    def register_listener(self, listener: EventListener) -> Exception:

        err: Exception = None
        if listener in self.__listeners:
            err = PermissionError

        self.__listeners.append(listener)
        return err
    

    def notify_event(self, event: Event, caller: object) -> None:
        
        for listener in self.__listeners:
            listener: EventListener = listener
            listener.trigger_event(event=event, caller=caller)


