#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2024-08-17 11:54:56
# @Author  : Your Name (you@example.org)
# @Link    : link
# @Version : 1.0.0


"""
Model
"""

from .Controllable import Controllable
from ..cdr.DataRepository import CentralDataRepository
from ..cdr.DataAccessor import DataAccessor
from ..misc import overwrite_protection



from abc import abstractmethod
from typing import Any, Callable, Hashable




class i_Model:
    
    @overwrite_protection
    @abstractmethod
    def register_central_data_repository(self, repository: CentralDataRepository) -> Exception:
        """
        
        """

    @property
    @abstractmethod
    def data_accessor(self) -> DataAccessor:
        """
        
        """


class Model(i_Model, Controllable):

    def __init__(self) -> None:
        super().__init__()

        self.__data_accessor: DataAccessor = None


    @property
    def data_accessor(self) -> DataAccessor:
        return self.__data_accessor


    @overwrite_protection
    def register_central_data_repository(self, repository: CentralDataRepository) -> Exception:
        
        err: Exception = None
        if self.__data_accessor:
            err = PermissionError

        self.__data_accessor = DataAccessor()
        self.__data_accessor.register_central_data_repository(repository=repository)
        return err

    
