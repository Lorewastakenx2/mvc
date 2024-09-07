


from abc import ABC


class Naming(ABC):

    __instance_default_name_index: dict = {}

    def __init__(self, name: str=None) -> None:

        self.__name: str = name
        
        if self.__name is None:
  
            class_name: str = self.__class__.__name__
            
            if class_name not in self.__class__.__instance_default_name_index:
                self.__class__.__instance_default_name_index[class_name] = 0
            else:
                self.__class__.__instance_default_name_index[class_name] += 1   
  
            self.__name = f'Default{class_name}{self.__class__.__instance_default_name_index[class_name]}'

    @property
    def name(self) -> str:
        return self.__name