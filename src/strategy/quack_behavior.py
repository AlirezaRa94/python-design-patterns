from abc import ABC, abstractmethod


class QuackBehavior(ABC):
    """
    The interface that all quacking behavior classes implement
    """
    @abstractmethod
    def quack(self):
        pass
