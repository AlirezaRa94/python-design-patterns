from src.strategy.quack_behavior import QuackBehavior


class Squeak(QuackBehavior):
    """
    Quacking behavior implementation for ducks that do squeak.
    """
    def quack(self):
        print("Squeak!")
