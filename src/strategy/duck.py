from abc import ABC, abstractmethod

from src.strategy.fly_behavior import FlyBehavior
from src.strategy.quack_behavior import QuackBehavior


class Duck(ABC):
    # two reference properties for the behavior interface types
    def __init__(self):
        self.__quack_behavior = None
        self.__fly_behavior = None

    @property
    def fly_behavior(self) -> FlyBehavior:
        return self.__fly_behavior

    @property
    def quack_behavior(self) -> QuackBehavior:
        return self.__quack_behavior

    @fly_behavior.setter
    def fly_behavior(self, fb: FlyBehavior):
        self.__fly_behavior = fb

    @quack_behavior.setter
    def quack_behavior(self, qb: QuackBehavior):
        self.__quack_behavior = qb

    @abstractmethod
    def display(self):
        pass

    # delegate the FlyBehavior class
    def perform_fly(self):
        self.__fly_behavior.fly()

    # delegate the QuackBehaviour class
    def perform_quack(self):
        self.__quack_behavior.quack()

    @staticmethod
    def swim():
        print("All ducks float; even decoys")
