from abc import abstractmethod
from interfaces.IObserver import IObserver
from interfaces.IController import IController
from interfaces.IGame import IGame
from interfaces.IEvent import IEvent


class IView(IObserver):
    controller: IController
    game: IGame

    def __init__(self, controller: IController, game: IGame):
        self.controller = controller
        self.game = game

    @abstractmethod
    def get_notified(self, e: IEvent):
        pass
