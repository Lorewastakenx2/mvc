
from .Controllable import Controllable


import tkinter as tk
from typing import Callable, Hashable


class View(Controllable):

    class __Binding:

        def __init__(self, context: tk.Widget, sequence: str, func: Callable) -> None:
            
            self.__context: tk.Widget = context
            self.__sequence: str = sequence
            self.__func: Callable = func
            self.__funcid: str = None

        def activate(self) -> None:

            if self.__funcid is None:
                self.__funcid = self.__context.bind(sequence=self.__sequence, func=self.__func)
            
        def deactivate(self) -> None:

            if self.__funcid:
                self.__context.unbind(sequence=self.__sequence, funcid=self.__funcid)
                self.__funcid = None

        def is_active(self) -> bool:
            return (self.__funcid is not None)
        

    def __init__(self, master: tk.Tk | tk.Toplevel | tk.Frame) -> None:
        Controllable.__init__(self)

        self.__frame: tk.Frame = tk.Frame(master=master)
        self.__frame.config(
            padx=0,
            pady=0,
            border=0,
            borderwidth=0
        )

        self.__bindings: dict[Hashable, View.__Binding] = {}

        # initialize default bindings

        self.Binding(context=self.__frame, identifier='EnterView', sequence='<Enter>', func=self._enter)
        self.Binding(context=self.__frame, identifier='LeaveView', sequence='<Leave>', func=self._leave)
        self.Binding(context=self.__frame, identifier='ConfigureView', sequence='<Configure>', func=self._configure)

        for _, binding in self.__bindings.items():
            binding.activate()

        self.__size_x: int = None
        self.__size_y: int = None
        self.__size_w: int = None
        self.__size_h: int = None

    @property
    def view_type(self) -> str:
        return self.__frame.master.__class__.__name__

    @property
    def frame(self) -> tk.Frame:
        return self.__frame
    
    @property
    def bindings(self) -> dict[Hashable, 'View.__Binding']:
        return self.__bindings

    @property
    def size(self) -> tuple:
        return tuple(self.__size_x, self.__size_y, self.__size_w, self.__size_h)


    def _enter(self, tk_event: tk.Event) -> None:
        """
        default binding
        """


    def _leave(self, tk_event: tk.Event) -> None:
        """
        default binding
        """

    def _configure(self, tk_event: tk.Event) -> None:
        """
        default binding
        """

        self.__size_x = tk_event.x
        self.__size_y = tk_event.y
        self.__size_w = tk_event.width
        self.__size_h = tk_event.height

    def Binding(self, context: tk.Widget, identifier: Hashable, sequence: str, func: Callable) -> None:

        if identifier in self.__bindings:
            raise KeyError

        binding: self.__Binding = self.__Binding(context=context, sequence=sequence, func=func)
        self.__bindings[identifier] = binding
