from src.strategy.quack_behavior import QuackBehavior


class Quack(QuackBehavior):
    """
    Quacking behavior implementation for ducks that do quack.
    """
    def quack(self):
        print("Quack!")
