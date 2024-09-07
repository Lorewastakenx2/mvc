#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2024-08-19 18:11:01
# @Author  : Your Name (you@example.org)
# @Link    : link
# @Version : 1.0.0


"""
DataAccessor
"""

from .DataRepository import DataRepository

from ..misc import overwrite_protection

from abc import abstractmethod
from typing import Any, Callable, Hashable


class i_DataAccessor:

    @overwrite_protection
    @abstractmethod
    def register_repository(self, repository: DataRepository) -> Exception:
        """
        
        """



class DataAccessor(i_DataAccessor):

    def __init__(self) -> None:
        
        self.__repository: DataRepository = None

    @overwrite_protection
    def register_repository(self, repository: DataRepository) -> Exception:

        err: Exception = None
        if self.__repository:
            err = PermissionError

        self.__repository = repository
        return err

