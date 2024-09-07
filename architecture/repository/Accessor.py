

class Accessor:

    def __init__(self) -> None:
        self.__id = id(self)

    def __hash__(self) -> int:
        return self.__id