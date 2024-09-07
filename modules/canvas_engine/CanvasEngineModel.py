
from architecture.Model import Model
from CanvasEngineView import CanvasElement


class CanvasEngineModel(Model):

    def __init__(self) -> None:
        Model.__init__(self)

        self.__elements_scheduled_for_update: list[CanvasElement] = []
        self.__element_under_construction: CanvasElement
        self.__dynamic_elements: list[CanvasElement] = []
        self.__static_elements: list[CanvasElement] = []

        self.__element_selection