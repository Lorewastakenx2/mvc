
from architecture.mvc.model import Model
from architecture.mvc.view import View
from architecture.mvc.controller import Controller
from architecture.event.event import Event

import logging
import tkinter as tk



if __name__ == '__main__':

    logging.basicConfig(
        level=logging.DEBUG, 
        format='%(asctime)s - %(levelname)s - %(message)s'
    )


    root: tk.Tk = tk.Tk()
    root.title('MVC')
    root.geometry('700x500')
    App: Controller = Controller()
    App.register_controllable(controllable=Model())
    App.register_controllable(controllable=View())

    App.initialize_view_frames_tk(master=root)

    App.register_event(event='id_only', callback=lambda: print('id_only event fired'))
    App.register_event(event=Event(identification='full_event'), callback=lambda: print('full_event event fired'))

    App.view.dispatch_event(event='id_only')
    App.view.dispatch_event(event=Event(identification='full_event'))




    #root.mainloop()

    print('... done')