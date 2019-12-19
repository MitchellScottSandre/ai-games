from typing import List
from interfaces.IPlayer import IPlayer
from interfaces.IGameState import IGameState
from interfaces.IPlayerMove import IPlayerMove

class Player(IPlayer):
    def __init__(self, id: int):
        super(Player, self).__init__(id)

    def get_legal_moves(self, state: IGameState) -> List[IPlayerMove]:
        return []
