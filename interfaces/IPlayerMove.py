from abc import ABC, abstractmethod
from interfaces import IGameState


class IPlayerMove(ABC):
    name: str

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def mutate_game_state(self, game_state: IGameState) -> IGameState:
        pass
