from IEnemy import IEnemy


class Invisibility(IEnemy):

    def __init__(self, enemy: IEnemy):
        self.__enemy = enemy

    def start(self):
        print(self.__enemy.get_name() + ' is invisibility')

    def stop(self):
        print(self.__enemy.get_name() + ' is not invisibility')