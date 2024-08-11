
from architecture.mvc.model import Model
from architecture.mvc.view import View
from architecture.mvc.controller import Controller


import tkinter as tk





if __name__ == '__main__':

    root: tk.Tk = tk.Tk()
    root.title('MVC')
    root.geometry('700x500')
    App: Controller = Controller()
    App.set_toplevel()
    App.register_controllable(controllable=Model())
    App.register_controllable(controllable=View())

    root.mainloop()