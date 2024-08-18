#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2024-08-17 11:20:12
# @Author  : Your Name (you@example.org)
# @Link    : link
# @Version : 1.0.0


"""
EventListener
"""

from architecture.event.Event import Event

from architecture.misc import overwrite_protection

from inspect import getfullargspec, FullArgSpec


from abc import abstractmethod
from typing import Any, Callable, Hashable



class EventNotRegisteredError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)



class i_EventListener:
    
    @abstractmethod
    def trigger_event(self, event: Event) -> None:
        """
        
        """

    @overwrite_protection
    @abstractmethod
    def register_event_handler(self, trigger: Hashable, handler: Callable) -> Exception:
        """
        
        """

    @overwrite_protection
    @abstractmethod
    def register_exception_handler(self, exception: Exception, handler: Callable) -> Exception:
        """
        
        """


class EventListener(i_EventListener):
    
    def __init__(self) -> None:
        
        self.__event_handlers: dict = {}
        self.__exception_handlers: dict = {}


    def trigger_event(self, event: Event, caller: object) -> None:
        
        try:
            self.__trigger_event(event=event, caller=caller)
        except Exception as err:
            if isinstance(err, tuple(self.__exception_handlers.keys())):

                exception_handler: Callable = self.__exception_handlers[type(err)]
                argspec: FullArgSpec = getfullargspec(exception_handler)

                kwargs: dict = {}
                if 'event' in argspec.args:
                    kwargs['event'] = event
                if 'caller' in argspec.args:
                    kwargs['caller'] = caller
                if 'err' in argspec.args:
                    kwargs['err'] = err

                exception_handler(**kwargs) 
            else:
                raise err


    def __trigger_event(self, event: Event, caller: object) -> None:

        if not event.trigger in self.__event_handlers:
            raise EventNotRegisteredError
        
        event_handler: Callable = self.__event_handlers[event.trigger]
        argspec: FullArgSpec = getfullargspec(event_handler)

        kwargs: dict = {}
        if 'event' in argspec.args:
            kwargs['event'] = event
        if 'caller' in argspec.args:
            kwargs['caller'] = caller

        event_handler(**kwargs)


    @overwrite_protection
    def register_event_handler(self, trigger: Hashable, handler: Callable) -> Exception:
    
        err: Exception = None
        if trigger in self.__event_handlers and self.__event_handlers[trigger] is not None:
            err = PermissionError

        self.__event_handlers[trigger] = handler
        return err


    @overwrite_protection
    def register_exception_handler(self, exception: Exception, handler: Callable) -> Exception:
        
        err: Exception = None
        if exception in self.__exception_handlers and self.__exception_handlers[exception] is not None:
            err = PermissionError

        self.__exception_handlers[exception] = handler
        return err



    



