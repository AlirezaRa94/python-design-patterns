from src.strategy.duck import Duck
from src.strategy.fly_behavior import FlyBehavior
from src.strategy.fly_with_wings import FlyWithWings
from src.strategy.quack import Quack
from src.strategy.quack_behavior import QuackBehavior


class MallardDuck(Duck):
    def __init__(self):
        super().__init__()
        self.quack_behavior: QuackBehavior = Quack()
        self.fly_behavior: FlyBehavior = FlyWithWings()

    def display(self):
        print("I'm a real Mallard duck")
