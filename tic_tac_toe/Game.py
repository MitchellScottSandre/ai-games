from typing import List
from interfaces.IGame import IGame
from interfaces.IGameState import IGameState
from interfaces.IPlayer import IPlayer
from interfaces.IPlayerMove import IPlayerMove
from tic_tac_toe.HumanPlayer import HumanPlayer
from tic_tac_toe.ComputerPlayer import ComputerPlayer
from tic_tac_toe.Grid import Grid


class Game(IGame):
    NO_WINNER = -1

    num_players: int
    curr_player_index: int
    # grid: Grid
    players: List[IPlayer]

    def __init__(self, num_players: int = 2, num_human_players: int = 1, board_width: int = 3, board_height: int = 3):
        self.num_players = num_players
        self.curr_player_index = 0
        self.grid = Grid(board_width, board_height)
        self.players = []
        for i in range(num_human_players):
            self.players.append(HumanPlayer(i))
        for i in range(num_players - num_human_players):
            self.players.append(ComputerPlayer(i + num_human_players))

    def get_current_player(self) -> IPlayer:
        return self.players[self.curr_player_index]

    def apply_player_move(self, state: IGameState, player_move: IPlayerMove):
        print("todo")

    def get_winner(self, state: IGameState) -> int:
        return self.NO_WINNER

    def start_game(self):
        print("todo")

    def end_game(self):
        print("todo")

