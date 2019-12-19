from abc import ABC
from typing import List
from interfaces import IObserver, IEvent


class ISubject(ABC):
    observers: List

    def attach(self, observer: IObserver):
        self.observers = []
        self.observers.append(observer)

    def notify_all(self, e: IEvent):
        for o in self.observers:
            o.get_notified(e)
