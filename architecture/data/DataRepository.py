#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2024-08-19 18:06:25
# @Author  : Your Name (you@example.org)
# @Link    : link
# @Version : 1.0.0


"""
CentralDataRepository
"""


from abc import abstractmethod
from typing import Any, Callable, Hashable




class i_DataRepository:


    @abstractmethod
    def read(self, lvalue: str) -> Any:
        """
        
        """


    @abstractmethod
    def write(self, access_code: Hashable, lvalue: str, rvalue: Any) -> None:
        """
        
        """



class DataRepository(i_DataRepository):

    def __init__(self):

        self.__data: dict = {}
        self.__access_codes: dict = {}




