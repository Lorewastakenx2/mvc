#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2024-08-17 13:00:39
# @Author  : Your Name (you@example.org)
# @Link    : link
# @Version : 1.0.0


"""
InteractiveCanvas
"""

from architecture.event.Event import Event

from architecture.event.EventManager import EventManager

from architecture.mvc.Model import Model
from architecture.mvc.View import View
from architecture.mvc.Controller import Controller

import tkinter as tk

from abc import abstractmethod
from typing import Any, Callable, Hashable



class i_InteractiveCanvas():
    pass



class _InteractiveCanvasModel(Model):

    def __init__(self) -> None:
        super().__init__()



class _InteractiveCanvasView(View):
    
    def __init__(self) -> None:
        super().__init__()

        self.__canvas: tk.Canvas = None


    def initialize(self, master: tk.Tk | tk.Toplevel | tk.Frame) -> None:
        super().initialize(master=master)

        self.__canvas = tk.Canvas(master=self.frame)
        self.__canvas.pack(expand=True, fill=tk.BOTH)

        self.__canvas.bind(
            sequence='<Button-1>', func=lambda tk_event:
            self.event_dispatcher.dispatch_event(event=Event(trigger='left_click', payload={'tk_event': tk_event}))
        )
        self.__canvas.bind(
            sequence='<Button-3>', func=lambda tk_event: 
            self.event_dispatcher.dispatch_event(event=Event(trigger='right_click', payload={'tk_event': tk_event}))
        )





class InteractiveCanvas(i_InteractiveCanvas, Controller):

    def __init__(self) -> None:
        Controller.__init__(self)

        self.register_controllable(controllable=_InteractiveCanvasModel())
        self.register_controllable(controllable=_InteractiveCanvasView())

        self.event_listener.register_event_handler(trigger='left_click', handler=lambda event, caller: print(event, caller))
        self.event_listener.register_event_handler(trigger='right_click', handler=lambda event, caller: print(event, caller))


        