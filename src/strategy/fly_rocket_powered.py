from src.strategy.fly_behavior import FlyBehavior


class FlyRocketPowered(FlyBehavior):
    """
    Flying behavior implementation for ducks that fly with a rocket!
    """
    def fly(self):
        print("I'm flying with a rocket!")
