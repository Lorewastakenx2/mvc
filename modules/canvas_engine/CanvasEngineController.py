
from architecture.Controller import Controller
from CanvasEngineModel import CanvasEngineModel
from CanvasEngineView import CanvasEngineView

import tkinter as tk

class CanvasEngineController(Controller):

    def __init__(self, tk_master: tk.Tk | tk.Toplevel | tk.Frame) -> None:
        Controller.__init__(self)

        self.register_controllable(controllable=CanvasEngineModel())
        self.register_controllable(controllable=CanvasEngineView(master=tk_master))

        self.__element_creation_context: type = None


    def set_element_creation_context(self, context: type) -> None:
        self.__element_creation_context = context