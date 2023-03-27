import random
from random import choice


class Character:
    """
    모든 캐릭터의 모체가 되는 클래스
    """

    def __init__(self, name, hp, mp, power):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.mp = mp
        self.power = power

    def attack(self, enemy):
        damage = random.randint(self.power - 2, self.power + 2)
        enemy.hp = max(enemy.hp - damage, 0)
        print(f"{self.name}의 공격! {enemy.name}에게 {damage}의 데미지를 입혔습니다.")
        if enemy.hp == 0:
            print(f"{enemy.name}이(가) 쓰러졌습니다.")

    def show_status(self):
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp}")

# 플레이어에 대한 서브 클래스


class Player(Character):
    def __init__(self, name, hp, mp, power, mpower):
        super().__init__(name, hp, mp, power)
        self.attribute = "player"
        self.mpower = mpower

    # # 플레이어의 스테이터스 랜덤으로 생성
    # def player_status():
    #     player.power = random.randrange(30,50)
    #     player.mpower = random.randrange(100,200)
    # print("공격력과 마력이 갱신되었습니다.")

    # 마법 공격에 대한 코드입니다.
    def mattack(self, enemy):
        damage = random.randint(self.mpower - 2, self.mpower + 2)
        enemy.hp = max(enemy.hp - damage, 0)
        print(f"{self.name}의 마법공격! {enemy.name}에게 {damage}의 마법 데미지를 입혔습니다.")
        if enemy.hp == 0:
            print(f"{enemy.name}이(가) 쓰러졌습니다.")

    # 부모 클래스에 존재하는 status_check 메소드를 overriding 합니다.
    def status_check(self):
        print(f"Player's hp : {self.hp}")


class Monster(Character):
    def __init__(self, name, hp, power):
        super().__init__(self, name, hp, power)

    def status_check(self):
        print(f"devil's hp : {self.hp}")


# 캐릭터와 몬스터를 생성합니다.
player_name = input("캐릭터를 생성합니다. 이름을 입력하십시오. : ")
player = Player(player_name, 300, 200, 50, 200)
devils = [
    Monster("베리알", 30, 3),
    Monster("아즈모단", 50, 5),
    Monster("바알", 100, 10),
    Monster("메피스토", 150, 15),
    Monster("두리엘", 200, 20),
    Monster("안다리엘", 300, 25),
    Monster("디아블로", 400, 30)
]
devil = random.choice(devils)


print(f"{player.name}")
print(f"{devil.name}")
