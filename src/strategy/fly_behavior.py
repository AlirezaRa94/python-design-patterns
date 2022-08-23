from abc import ABC, abstractmethod


class FlyBehavior(ABC):
    """
    The interface that all flying behavior classes implement
    """
    @abstractmethod
    def fly(self):
        pass
