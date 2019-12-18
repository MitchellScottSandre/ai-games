from abc import ABC, abstractmethod
from typing import List
from . import IGameState, IPlayerMove, IPlayer


class IGame(ABC):

    @abstractmethod
    def get_current_player(self) -> IPlayer:
        pass

    @abstractmethod
    def apply_player_move(self, state: IGameState, player_move: IPlayerMove):
        pass

    @abstractmethod
    def get_legal_moves(self, state: IGameState) -> List[IPlayerMove]:
        pass

    @abstractmethod
    def get_winner(self, state: IGameState) -> int:
        pass

    @abstractmethod
    def start_game(self):
        pass

    @abstractmethod
    def end_game(self):
        pass
