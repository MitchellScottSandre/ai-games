from interfaces.IController import IController
from interfaces.IGame import IGame


class Controller(IController):

    def __init__(self, game: IGame):
        super(Controller, self).__init__(game)
