from abc import abstractmethod
from interfaces import ISubject, IGameState, IPlayerMove, IPlayer


class IGame(ISubject):

    @abstractmethod
    def get_current_player(self) -> IPlayer:
        pass

    @abstractmethod
    def apply_player_move(self, state: IGameState, player_move: IPlayerMove):
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
