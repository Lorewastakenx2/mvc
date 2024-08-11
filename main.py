
from architecture.mvc.model import Model
from architecture.mvc.view import View
from architecture.mvc.controller import Controller
from architecture.event.event import Event

import logging
import tkinter as tk

"""
TODO:

    - register_parent is accessible from controllers, it shouldnt be as its used during register_controllable

"""

if __name__ == '__main__':

    logging.basicConfig(
        level=logging.DEBUG, 
        format='%(asctime)s - %(levelname)s - %(name)s - %(message)s'
    )


    root: tk.Tk = tk.Tk()
    root.title('MVC')
    root.geometry('700x500')
    App: Controller = Controller()
    App.register_controllable(controllable=Model())
    App.register_controllable(controllable=View())

    App.initialize_tk_frames(master=root)

    root.mainloop()

    print('... done')