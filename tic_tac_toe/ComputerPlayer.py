from interfaces.IGameState import IGameState
from tic_tac_toe.Player import Player


class ComputerPlayer(Player):
    def __init__(self, id: int):
        super(ComputerPlayer, self).__init__(id)

    def play_move(self, game_state: IGameState) -> IGameState:
        pass
