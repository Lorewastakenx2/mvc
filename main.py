
from architecture.Model import Model
from architecture.View import View
from architecture.Controller import Controller
from architecture.repository.Repository import Repository



if __name__ == '__main__':

    repository: Repository = Repository()

    model: Model = Model()
    view: View = View()
    controller: Controller = Controller()

    controller.register_controllable(controllable=model)
    controller.register_controllable(controllable=view)