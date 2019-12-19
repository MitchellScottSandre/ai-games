from interfaces import IView, IController, IGame, IEvent


class TerminalView(IView):
    def __init__(self, controller: IController, game: IGame):
        super(TerminalView, self).__init__(controller, game)

    def get_notified(self, e: IEvent):
        print("todo")