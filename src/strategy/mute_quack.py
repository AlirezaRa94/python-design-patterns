from src.strategy.quack_behavior import QuackBehavior


class MuteQuack(QuackBehavior):
    """
    Quacking behavior implementation for ducks that do not quack.
    """
    def quack(self):
        print("<< silence >>")
