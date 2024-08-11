
from architecture.mvc.controllable import Controllable

from abc import abstractmethod



class i_Model:
    pass



class Model(i_Model, Controllable):
    
    def __init__(self) -> None:
        Controllable.__init__(self)