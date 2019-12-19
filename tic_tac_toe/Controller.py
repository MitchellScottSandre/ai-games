from interfaces import IController, IGame


class Controller(IController):

    def __init__(self, game: IGame):
        super(Controller, self).__init__(game)
