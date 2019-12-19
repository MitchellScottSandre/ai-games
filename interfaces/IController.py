from abc import ABC
from interfaces import IGame


class IController(ABC):
    game: IGame

    def __init__(self, game: IGame):
        self.game = game
