
from architecture.mvc.controllable import Controllable
from logs import mvc_logger as logger

from abc import abstractmethod
from typing import Union
import tkinter as tk

t_Master = Union[tk.Tk, tk.Toplevel, tk.Frame]


class errors:

    class FrameNotInitializedError(Exception):
        def __init__(self, *args: object) -> None:
            super().__init__(*args)


class i_View:
    
    @property
    @abstractmethod
    def frame(self) -> tk.Frame:
        """
        the main frame of the view        
        """

    @abstractmethod
    def initialize_frame(self, master: t_Master) -> None:
        """
        
        """



class View(i_View, Controllable):
    
    def __init__(self) -> None:
        logger.debug(
            msg=f'*** initializing View *** view={self}'
        )

        Controllable.__init__(self)

        self.__frame: tk.Frame = None

    @property
    def frame(self) -> None:
        
        if self.frame is None:
            raise errors.FrameNotInitializedError
        
        return self.__frame
    
    def initialize_frame(self, master: t_Master) -> None:
        
        if self.__frame:
            raise PermissionError
                
        self.__frame = tk.Frame(master=master)


