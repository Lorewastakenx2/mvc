
from architecture.Model import Model
from architecture.View import View
from architecture.Controller import Controller
from architecture.repository.Repository import Repository
from architecture.repository.Field import Field
from architecture.event.Event import Event


repository = Repository()

model = Model()
model.register_repository(repository)

view = View()

controller = Controller()
controller.register_controllable(model)
controller.register_controllable(view)

toplevel = Controller(name='ToplevelController')
toplevel.register_controllable(controller)

controller.event_listener.register_event_handler('local', lambda event, caller: print(event, caller))
toplevel.event_listener.register_event_handler('toplevel', lambda event, caller: print(event, caller))

model.event_dispatcher.dispatch_event(event=Event('local', payload={1}))
view.event_dispatcher.dispatch_event(event=Event('toplevel', payload={2}))

import tkinter as tk

root = tk.Tk()
root.geometry('700x500')

view.initialize(master=root)
view.frame.pack()

model.counter = 0
model._fields['counter'] = Field(rvalue=model.counter)


button = tk.Button(master=view.frame)
button.config(command=lambda: view.event_dispatcher.dispatch_event('button click'))

controller.event_listener.register_event_handler('button click', lambda: )

label = tk.Label(master=view.frame)

root.mainloop()