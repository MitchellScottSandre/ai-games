from interfaces. IGameStateEvaluator import IGameStateEvaluator
from . import Grid


class GridEvaluator(IGameStateEvaluator):
    @staticmethod
    def evaluate(self, game_state: Grid) -> float:
        return 0
