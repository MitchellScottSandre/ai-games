from interfaces import IGameState
from tic_tac_toe.Player import Player


class HumanPlayer(Player):
    def __init__(self, id: int):
        super(HumanPlayer, self).__init__(id)

    def play_move(self, game_state: IGameState) -> IGameState:
        pass
