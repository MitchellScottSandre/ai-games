from abc import ABC
from interfaces import IObserver, IController, IGame


class IView(IObserver, ABC):
    controller: IController
    game: IGame

    def __init__(self, controller: IController, game: IGame):
        self.controller = controller
        self.game = game
