
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2024-08-17 11:53:08
# @Author  : Your Name (you@example.org)
# @Link    : link
# @Version : 1.0.0


"""
Controller

handles event specific registration between controllers and controllables


"""

from architecture.event.EventListener import EventListener, EventNotRegisteredError
from architecture.event.EventManager import EventManager

from .Controllable import Controllable
from .Model import Model
from .View import View

from architecture.misc import overwrite_protection

from abc import abstractmethod
from typing import Any, Callable, Hashable



class i_Controller:


    @property
    @abstractmethod
    def model(self) -> Model:
        """
        
        """


    @property
    @abstractmethod
    def view(self) -> View:
        """
        
        """

    @property
    @abstractmethod
    def event_listener(self) -> EventListener:
        """
        
        """

    @property
    @abstractmethod
    def parent(self) -> 'Controller':
        """
        
        """


    @overwrite_protection
    @abstractmethod
    def register_controllable(self, controllable: Controllable) -> Exception:
        """
        
        """



class Controller(i_Controller, Controllable):

    def __init__(self) -> None:

        self.__parent: Controller = None

        self.__event_listener: EventListener = EventListener()        

        self.__event_manager: EventManager = EventManager()
        self.__event_manager.register_listener(listener=self.__event_listener)

        self.__model: Model = None
        self.__view:  View = None


    @property
    def model(self) -> Model:
        return self.__model


    @property
    def view(self) -> View:
        return self.__view


    @property
    def event_listener(self) -> EventListener:
        return self.__event_listener


    @property
    def parent(self) -> 'Controller':
        return self.__parent


    @overwrite_protection
    def register_controllable(self, controllable: Controllable) -> Exception:

        err: Exception = None
        
        if isinstance(controllable, Model):
            err = self.__register_model(model=controllable)

        elif isinstance(controllable, View):
            err = self.__register_view(view=controllable)

        elif isinstance(controllable, Controller):
            err = self.__register_controller(controller=controllable)

        else:
            raise ValueError

        return err


    def __register_model(self, model: Model) -> Exception:
        
        err: Exception = None
        if self.__model:
            err = PermissionError

        self.__model = model
        self.__model.event_dispatcher.register_manager(manager=self.__event_manager)
        return err
            

    def __register_view(self, view: View) -> Exception:

        err: Exception = None
        if self.__view:
            err = PermissionError

        self.__view = view
        self.__view.event_dispatcher.register_manager(manager=self.__event_manager)
        return err
    

    def __register_controller(self, controller: 'Controller') -> Exception:

        err: Exception = None
        if controller.parent:
            err = PermissionError

        Controllable.__init__(controller)
        controller.__parent = self
        controller.event_dispatcher.register_manager(manager=self.__event_manager)

        controller.event_listener.register_exception_handler(
            exception=EventNotRegisteredError, handler=lambda event, caller:
            self.event_listener.trigger_event(event=event, caller=caller)
        )
        return err



