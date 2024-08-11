

import logging
from abc import abstractmethod


"""
TODO:

fix so that 

set-, get-, and is_toplevel are class methods

"""


class i_Hierarchy:

    @abstractmethod
    def set_toplevel(self) -> None:
        """
        
        """

    @abstractmethod
    def get_toplevel(self) -> object:
        """
        
        """

    @abstractmethod
    def is_toplevel(self) -> bool:
        """
        
        """

    @abstractmethod
    def register_parent(self, parent: object) -> None:
        """
        
        """

    @abstractmethod
    def _register_child(self, child: object) -> None:
        """
        should not be used.
        is used while registering parent.
        """

    @property
    @abstractmethod
    def parent(self) -> object:
        """
        
        """

    @property
    @abstractmethod
    def children(self) -> list:
        """
        
        """


class Hierarchy(i_Hierarchy):

    __toplevel: i_Hierarchy = None

    def __init__(self) -> None:
        logging.log(
            level=logging.DEBUG,
            msg=f'*** initializing Hierarchy *** instance={self}'
        )

        if self.get_toplevel() is None:
            self.set_toplevel()

        self.__parent: i_Hierarchy = None
        self.__children: list = []

    @property
    def parent(self) -> i_Hierarchy:
        return self.__parent
    
    @property
    def children(self) -> i_Hierarchy:
        return self.__children

    def register_parent(self, parent: i_Hierarchy) -> None:
        
        if self.__parent:
            raise PermissionError
        
        if self.is_toplevel():
            raise PermissionError
        
        self.__parent = parent
        self.__parent._register_child(child=self)

        logging.log(
            level=logging.DEBUG,
            msg=f'*** parent registered *** parent={parent}, child={self}'
        )


    def _register_child(self, child: i_Hierarchy) -> None:
        self.__children.append(child)


    def set_toplevel(self) -> None:
        
        if self.__class__.__toplevel:
            raise PermissionError
        
        self.__class__.__toplevel = self

        logging.log(
            level=logging.DEBUG,
            msg=f'*** toplevel set *** cls={self.__class__}, toplevel={self}'
        )

    def get_toplevel(self) -> i_Hierarchy:
        return self.__class__.__toplevel


    def is_toplevel(self) -> bool:
        return self is self.__class__.__toplevel