
from architecture.mvc.controllable import Controllable
from architecture.mvc.model import Model
from architecture.mvc.view import View
from architecture.event.event import Event
from architecture.event.event_handler import EventHandler
from architecture.event.event_handler import errors as event_handler_errors
from architecture.hierarchy import Hierarchy


from abc import abstractmethod


class errors:

    class FloatingEventError(Exception):
        def __init__(self, *args: object) -> None:
            super().__init__(*args)



class i_Controller:

    @abstractmethod
    def register_controllable(self, controllable: Controllable) -> None:
        """
        controllables are registered to the controller.
        the controller registers controller related 
        parameters in the controllable.
        """

    @abstractmethod
    def handle_event(self, caller: Controllable, event: Event, ignored_exceptions: tuple=()) -> None:
        """
        wrapper for the controller's owned event handler.

        if the event is not registered to the handler, the
        controller relays the event to its parent.
        this is done with error handling.
        """

    @property
    @abstractmethod
    def model(self) -> Model:
        """
        read only.
        """

    @property
    @abstractmethod
    def view(self) -> View:
        """
        read only.
        """


class Controller(i_Controller, Controllable, Hierarchy):

    def __init__(self) -> None:
        Controllable.__init__(self)
        Hierarchy.__init__(self)

        self.__model: Model = None
        self.__view: View = None
        self.__event_handler: EventHandler = EventHandler()

    @property
    def model(self) -> Model:
        return self.__model
    
    @property
    def view(self) -> View:
        return self.__view

    def register_controllable(self, controllable: Controllable) -> None:
        
        controllable.event_dispatcher.register_event_handler(handler=self.__event_handler)

        # type specific registration

        if isinstance(controllable, Model):
            if self.__view:
                raise PermissionError
            self.__model = controllable
        elif isinstance(controllable, View):
            if self.__view:
                raise PermissionError
            self.__view = controllable
        elif isinstance(controllable, Controller):
            controllable.register_parent(parent=self)
        else:
            raise ValueError
        
    def handle_event(self, caller: Controllable, event: Event, ignored_exceptions: tuple=()) -> None:
        
        try:
            self.__event_handler.handle_event(caller=caller, event=event, ignored_exceptions=ignored_exceptions)
        except Exception as err:

            if isinstance(err, event_handler_errors.EventNotRegisteredError):
                self.__relay_event(caller=caller, event=event, ignored_exceptions=ignored_exceptions)
            else:
                raise err

    def __relay_event(self, caller: Controllable, event: Event, ignored_exceptions: tuple) -> None:
        if self.is_toplevel():
            raise errors.FloatingEventError
        self.event_dispatcher.dispatch_event(caller=caller, event=event, ignored_exceptions=ignored_exceptions)
