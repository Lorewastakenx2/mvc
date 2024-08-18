
from architecture.event.Event import Event


from architecture.mvc.Model import *
from architecture.mvc.View import *
from architecture.mvc.Controller import *


if __name__ == '__main__':

    toplevel = Controller()

    model = Model()
    view = View()
    controller = Controller()

    toplevel.register_controllable(controllable=controller)
    toplevel.event_listener.register_event_handler(trigger='toplevel_event', handler=lambda event, caller: print(event, caller))

    controller.register_controllable(controllable=model)
    controller.register_controllable(controllable=view)
    controller.event_listener.register_event_handler(trigger='model_event', handler=lambda event, caller: print(event, caller))
    controller.event_listener.register_event_handler(trigger='view_event', handler=lambda event, caller: print(event, caller))

    controller.view.event_dispatcher.dispatch_event(event=Event(trigger='view_event'))
    controller.model.event_dispatcher.dispatch_event(event=Event(trigger='model_event'))
    controller.model.event_dispatcher.dispatch_event(event=Event(trigger='toplevel_event'))

    



    




