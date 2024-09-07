
from typing import Any

from architecture.repository.Repository import Repository

from .Controllable import Controllable
from .Model import Model
from .View import View
from .event.Event import Event
from .event.EventListener import EventListener, EventNotRegisteredError
from .event.EventBus import EventBus

"""
trans-controller functionality removed for now.
will be refactored
"""


#class Controller(Controllable):
class Controller:

    def __init__(self) -> None:

        #self.__parent: Controller = None

        self.__model: Model = None
        self.__view:  View = None

        self.__model_view_repository: Repository = Repository()

        self.__event_listener: EventListener = EventListener()
        self.__event_bus: EventBus = EventBus()
        self.__event_bus.add_listener(listener=self.__event_listener)

       
    #@property
    #def parent(self) -> 'Controller':
    #    return self.__parent

    @property
    def model(self) -> Model:
        return self.__model
    
    @property
    def view(self) -> View:
        return self.__view
    
    @property
    def event_listener(self) -> EventListener:
        return self.__event_listener

    def register_controllable(self, controllable: Controllable) -> None:

        controllable.event_dispatcher.register_bus(self.__event_bus)
        controllable.register_model_view_repository(self.__model_view_repository)

        if isinstance(controllable, Model):
            #self.__register_model(model=controllable)
            self.__model = controllable
            

        elif isinstance(controllable, View):
            #self.__register_view(view=controllable)
            self.__view = controllable

        #elif isinstance(controllable, Controller):
        #    self.__register_controller(controller=controllable)

        else:
            raise ValueError('controllable must be of type Model or View')

    #def __register_model(self, model: Model) -> None:

    #    if not self.__model is None:
     #       raise PermissionError
        
    #    self.__model = model
    #    self.__model.event_dispatcher.register_bus(bus=self.__event_bus)

    #def __register_view(self, view: View) -> None:

    #    if not self.__view is None:
    #        raise PermissionError
        
    #    self.__view = view
    #    self.__view.event_dispatcher.register_bus(bus=self.__event_bus)

   #def register_controller(self, controller: 'Controller') -> None:

   #    if not controller.parent is None:
   #        raise PermissionError
   #    
   #    Controllable.__init__(controller)
   #    controller.__parent = self
   #    controller.event_dispatcher.register_manager(manager=self.__event_manager)
   #    controller.event_listener.register_exception_handler(
   #        exception=EventNotRegisteredError, 
   #        handler=self.__bubble_event
   #    )

   #def __bubble_event(self, event: Event, caller: Any) -> None:
   #    self.__event_listener.trigger_event(event=event, caller=caller)