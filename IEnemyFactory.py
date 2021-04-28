from IEnemy import IEnemy


class IEnemyFactory:
    def create(self) -> IEnemy:
        pass

    def get_name(self) -> str:
        pass