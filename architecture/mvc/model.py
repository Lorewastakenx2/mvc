
from architecture.mvc.controllable import Controllable
from logs import mvc_logger as logger

from abc import abstractmethod



class i_Model:
    pass



class Model(i_Model, Controllable):
    
    def __init__(self) -> None:
        logger.debug(
            msg=f'*** initializing Model *** model={self}'
        )
        Controllable.__init__(self)