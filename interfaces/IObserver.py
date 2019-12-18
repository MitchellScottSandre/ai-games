from abc import ABC, abstractmethod
from . import IEvent


class IObserver(ABC):
    @abstractmethod
    def get_notified(self, e: IEvent):
        pass
