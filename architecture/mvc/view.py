
from architecture.mvc.controllable import Controllable

from abc import abstractmethod



class i_View:
    pass



class View(i_View, Controllable):
    
    def __init__(self) -> None:
        Controllable.__init__(self)