#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2024-08-17 11:55:04
# @Author  : Your Name (you@example.org)
# @Link    : link
# @Version : 1.0.0


"""
View
"""


from .Controllable import Controllable

import tkinter as tk

from abc import abstractmethod
from typing import Any, Callable, Hashable


class i_View:


    @abstractmethod
    def initialize(self, master: tk.Tk | tk.Toplevel | tk.Frame) -> None:
        """
        
        """

    @property
    @abstractmethod
    def frame(self) -> tk.Frame:
        """
        
        """



class View(i_View, Controllable):
    
    def __init__(self) -> None:
        super().__init__()

        self.__frame: tk.Frame = None


    def initialize(self, master: tk.Tk | tk.Toplevel | tk.Frame) -> None:
        self.__frame = tk.Frame(master=master)


    @property
    def frame(self) -> tk.Frame:
        return self.__frame