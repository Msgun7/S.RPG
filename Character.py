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
        super().__init__(name, hp, 0, power)

    def status_check(self):
        print(f"devil's hp : {self.hp}")


# 캐릭터와 몬스터를 생성합니다.
player_name = input("캐릭터를 생성합니다. 이름을 입력하십시오. : ")
print(f"하느님 감사합니다, 드디어 돌아오셨군요! {player_name}님 당신이 떠난 후로 많은 게 변했습니다. ")
player = Player(player_name, 300, 200, 100, 200)
devils = [
    Monster("베리알", 300, 30),
    Monster("아즈모단", 500, 50),
    Monster("바알", 1000, 30),
    Monster("메피스토", 1500, 30),
    Monster("두리엘", 2000, 20),
    Monster("안다리엘", 3000, 25),
    Monster("디아블로", 4000, 30)
]
devil = random.choice(devils)
print(f"{player.name}님 악마 {devil.name}가(이) 소환되었습니다. 전투를 준비하세요.")


while True:

    print(f"{player.name}님의 체력을 확인합니다. : {player.hp}")
    print(f"{devil.name}의 체력을 확인합니다. : {devil.hp} 더러운 악마에게 신의 철퇴를")
    
    player.attack(devil)

    devil.attack(player)

    
    break
    
    