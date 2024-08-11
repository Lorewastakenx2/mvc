

from abc import abstractmethod



class i_Hierarchy:

    @abstractmethod
    def set_toplevel(self) -> None:
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

    def _register_child(self, child: i_Hierarchy) -> None:
        self.__children.append(child)

    def set_toplevel(self) -> None:
        if self.__class__.__toplevel:
            raise PermissionError
        self.__class__.__toplevel = self

    def is_toplevel(self) -> bool:
        return self is self.__class__.__toplevel