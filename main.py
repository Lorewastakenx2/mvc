
from architecture.mvc.model import Model
from architecture.mvc.view import View
from architecture.mvc.controller import Controller
from architecture.event.event import Event

import logging
import tkinter as tk



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

    widget: Controller = Controller()
    widget.register_controllable(controllable=Model())
    widget.register_controllable(controllable=View())

    App.initialize_view_frames_tk(master=root)
    
    widget.register_event(event='widget_level_event', callback=lambda: None)
    App.register_event(event='toplevel_event', callback=lambda: None)

    widget.view.dispatch_event(event='widget_level_event')
    widget.view.dispatch_event(event='toplevel_event')


    #root.mainloop()

    print('... done')