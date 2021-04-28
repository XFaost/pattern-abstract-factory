from Enemies.Skills.Invisibility import Invisibility
from IEnemy import IEnemy


class Bloodsucker(IEnemy):

    def __init__(self):
        self.__invisibility = Invisibility(self)
        self.spawn()

    def spawn(self):
        print(self.get_name() + ' is spawn')
        self.__invisibility.start()

    def kill(self):
        self.__invisibility.stop()
        print(self.get_name() + ' is dead')

    def get_name(self):
        return 'Bloodsucker'
