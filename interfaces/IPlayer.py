from abc import ABC, abstractmethod
from . import IGameState


class IPlayer(ABC):
    id: int

    def __init__(self, id: int):
        self.id = id

    def play_move(self, game_state: IGameState):
        pass
