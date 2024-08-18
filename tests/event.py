

from architecture.event.Event import *
from architecture.event.EventDispatcher import *
from architecture.event.EventListener import *
from architecture.event.EventManager import *


if __name__ == '__main__':

    dispatcher = EventDispatcher()
    listener = EventListener()
    manager = EventManager()

    dispatcher.register_manager(manager=manager)
    manager.register_listener(listener=listener)

    listener.register_event_handler(trigger='test', handler=lambda event, caller: print(event, caller))
    dispatcher.dispatch_event(event=Event(trigger='test', payload={'data': 1}))



