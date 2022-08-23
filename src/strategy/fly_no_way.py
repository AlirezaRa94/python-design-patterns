from src.strategy.fly_behavior import FlyBehavior


class FlyNoWay(FlyBehavior):
    """
    Flying behavior implementation for ducks that do not fly
    """
    def fly(self):
        print("I can't fly!")
