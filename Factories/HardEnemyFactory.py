from Enemies.Bloodsucker import Bloodsucker
from Enemies.Dog import Dog
from Enemies.Stalker import Stalker
from IEnemy import IEnemy
from IEnemyFactory import IEnemyFactory


class HardEnemyFactory(IEnemyFactory):
    def __init__(self):
        self.__enemy_count = 0

    def create(self) -> IEnemy:

        self.__enemy_count += 1
        if self.__enemy_count <= 5:
            return Bloodsucker()
        if self.__enemy_count <= 10:
            return Stalker()
        else:
            return Dog()

    def get_name(self) -> str:
        return 'Hard level'
