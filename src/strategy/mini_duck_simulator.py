from src.strategy.duck import Duck
from src.strategy.fly_rocket_powered import FlyRocketPowered
from src.strategy.mallard_duck import MallardDuck
from src.strategy.model_duck import ModelDuck

if __name__ == "__main__":
    mallard: Duck = MallardDuck()
    mallard.perform_quack()
    mallard.perform_fly()

    model: Duck = ModelDuck()
    model.perform_fly()
    model.fly_behavior = FlyRocketPowered()
    model.perform_fly()
