from IEnemyFactory import IEnemyFactory


class Game:
    def __init__(self, factory: IEnemyFactory):
        self.__factory = factory
        self.__enemies = []
        self.__num_enemies = 10
        print('\nU have choose a ' + self.__factory.get_name())

    def run(self) -> None:
        print('\nLoading...')

        for i in range(0, self.__num_enemies):
            self.__enemies.append(self.__factory.create())

    def shut_down(self) -> None:
        print('\nShut down...')

        for i in range(0, len(self.__enemies)):
            self.__enemies[i].kill()