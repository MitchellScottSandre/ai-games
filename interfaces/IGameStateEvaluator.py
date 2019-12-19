from abc import ABC, abstractmethod
from interfaces import IGameState


class IGameStateEvaluator(ABC):

    @staticmethod
    @abstractmethod
    def evaluate(self, game_state: IGameState) -> float:
        pass
