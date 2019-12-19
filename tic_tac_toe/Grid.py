from typing import List
from interfaces.IGameState import IGameState

class Grid(IGameState):
    class Cell:
        EMPTY = -1
        player_id: int

        def __init__(self):
            self.player_id = self.EMPTY

        def assign_val(self, player_id: int):
            self.player_id = player_id

        def get_display_char(self):
            return str(self.player_id)

    width: int
    height: int
    grid_data: List[List[Cell]]  # grid_data[row][column]

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid_data = [[Grid.Cell() for col in range(height)] for row in range(height)]

