from Factories.EasilyEnemyFactory import EasilyEnemyFactory
from Factories.HardEnemyFactory import HardEnemyFactory
from Factories.MiddleEnemyFactory import MiddleEnemyFactory
from Game import Game

if __name__ == '__main__':

    levels = [EasilyEnemyFactory(), MiddleEnemyFactory(), HardEnemyFactory()]

    level = 1
    while True:
        try:
            level: int = int(input("Select difficulty level:\n1. Easily\n2. Middle\n3. Hard\n>  "))
            if 1 <= level <= 3:
                break
        except:
            pass

    game = Game(levels[level-1])
    game.run()
    game.shut_down()
