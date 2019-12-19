from abc import ABC, abstractmethod
from interfaces import IEvent


class IObserver(ABC):
    @abstractmethod
    def get_notified(self, e: IEvent):
        pass
