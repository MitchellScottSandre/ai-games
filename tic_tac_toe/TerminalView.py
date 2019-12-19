from interfaces.IView import IView
from interfaces.IController import IController
from interfaces.IGame import IGame
from interfaces.IEvent import IEvent


class TerminalView(IView):
    def __init__(self, controller: IController, game: IGame):
        super(TerminalView, self).__init__(controller, game)

    def get_notified(self, e: IEvent):
        print("todo")