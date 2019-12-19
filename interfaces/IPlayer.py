from abc import ABC, abstractmethod
from typing import List
from interfaces import IGameState, IPlayerMove


class IPlayer(ABC):
    id: int

    def __init__(self, id: int):
        self.id = id

    @abstractmethod
    def get_legal_moves(self, state: IGameState) -> List:
        pass

    @abstractmethod
    def play_move(self, game_state: IGameState) -> IGameState:
        pass
