from tic_tac_toe.Game import Game
from tic_tac_toe.Controller import Controller
from tic_tac_toe.TerminalView import TerminalView


def main():
    game = Game()
    controller = Controller(game)
    view = TerminalView(controller, game)
    game.start_game()


if __name__ == "__main__":
    main()
