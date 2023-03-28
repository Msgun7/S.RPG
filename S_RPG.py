import random
from random import choice
import time


# 모든 캐릭터의 모체가 되는 클래스
class Character:
    def __init__(self, name, hp, mp, power):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.mp = mp
        self.power = power

# #플레이어와 몬스터의 통상공격 >> 각자의 이름에 색깔을 씌우기 위해 모체에서 서브 클래스로 각각 배분하는것으로 이동
#     def attack(self, enemy):
#         damage = random.randint(self.power - 2, self.power + 2)
#         enemy.hp = max(enemy.hp - damage, 0)
#         print(f"{self.name}의" + "\033[96m{통상공격}\033[0m 으로"+f"{enemy.name}에게 {damage}의 데미지를 입혔습니다.")
#         if enemy.hp == 0:
#             print(f"{enemy.name}가(이) 쓰러졌습니다.")

# #공통적으로 출력할 플레이어와 몬스터의 상태 체크 >> 이름을 씌우기 위해
#     def show_status(self):
#         print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp}")

# 플레이어 클래스


class Player(Character):
    def __init__(self, name, hp, mp, power, mpower):
        super().__init__(name, hp, mp, power)
        self.mpower = mpower
        self.mp_max = mp

    # 플레이어의 통상공격
    def attack(self, enemy):
        damage = random.randint(self.power - 20, self.power + 20)
        enemy.hp = max(enemy.hp - damage, 0)
        print(f"\033[32m{player_name}\033[0m의" + "\033[96m{통상공격}\033[0m 으로" +
              f"\033[31m{devil.name}\033[0m에게 \033[95m{damage}\033[0m의 데미지를 입혔습니다.")
        if enemy.hp == 0:
            print(f"\033[31m{devil.name}\033[0m가(이) 쓰러졌습니다.")

# 플레이어의 마법공격
    def mattack(self, enemy):
        if self.mp == 0:
            print("마나가 부족하여" + f"\033[32m{self.name}\033[0m" +
                  "님의 "+"\033[93m{마법공격}\033[0m이 사용불가능합니다.")
            return

        self.mp = self.mp - 40
        damage = random.randint(self.mpower - 200, self.mpower + 400)
        enemy.hp = max(enemy.hp - damage, 0)
        print(f"\033[32m{self.name}\033[0m" + "의 \033[93m{마법공격}\033[0m ! " +
              f"\033[31m{enemy.name}\033[0m" + f"에게 \033[95m{damage}\033[0m의 마법 데미지를 입혔습니다.")
        if enemy.hp == 0:
            print(f"\033[31m{enemy.name}\033[0m" + "이(가) 쓰러졌습니다.")
        if self.mp <= 0:
            print("MP를 모두 사용하셨습니다.")

    def show_status(self):
        print(
            f"\033[32m{player.name}\033[0m의 상태: HP \033[91m{self.hp}\033[0m/\033[91m{self.max_hp}\033[0m")

    # 부모 클래스에 존재하는 status_check 메소드를 overriding 합니다.
    def status_check(self):
        print(f"\033[32m{player.name}\033[0m" + f"님의 HP : \033[91m{self.hp}\033[0m/ " +
              f"\033[32m{player.name}\033[0m" + f"님의 MP : \033[34m{self.mp}\033[0m")


# 몬스터 클래스입니다.
class Monster(Character):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, 0, power)

    # 몬스터의 통상공격
    def attack(self, enemy):
        damage = random.randint(self.power - 20, self.power + 20)
        enemy.hp = max(enemy.hp - damage, 0)
        print(f"\033[31m{devil.name}\033[0m의" + "\033[96m{통상공격}\033[0m 으로" +
              f"\033[32m{player_name}\033[0m" + f"에게 \033[95m{damage}\033[0m의 데미지를 입혔습니다.")
        if enemy.hp == 0:
            print(f"\033[32m{player_name}\033[0m가(이) 쓰러졌습니다.")

    def show_status(self):
        print(
            f"\033[31m{devil.name}\033[0m 의 상태: HP \033[91m{self.hp}\033[0m/\033[91m{self.max_hp}\033[0m")

    def status_check(self):
        print(f"\033[31m{devil.name}\033[0m 의 HP" +
              f" : \033[91m{self.hp}\033[0m")


# 캐릭터와 몬스터를 생성합니다. 플레이어의 캐릭터는 이름을 입력받고 몬스터는 랜덤 초이스로 리스트에서 랜덤하게 생성됩니다.
player_name = input("캐릭터를 생성합니다. 이름을 입력하십시오. : ")
print(f"하느님 감사합니다, 드디어 돌아오셨군요! " +
      f"\033[32m{player_name}\033[0m" + "님 당신이 떠난 후로 많은 게 변했습니다. ")
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
print("불타오르는 대지 그 너머 당신의 눈 앞에 힘의 문양이 떠올랐습니다.")
# print(player.name + "님 당신이 맞설 상대는 군주라 불리는 악마인 " + "\033[31m" + devil.name + "\033[0m" + "입니다. 너무 늦기 전에 그 차원문을 타고 가서  "+ "\033[31m" + devil.name + "\033[0m" + "를 쓰러트려 주십시오!")
print(f"\033[32m{player.name}\033[0m" + "님 당신이 맞설 상대는 군주라 불리는 악마인 " + f"\033[31m{devil.name}\033[0m" +
      "입니다. 너무 늦기 전에 그 차원문을 타고 가서  " + f"\033[31m{devil.name}\033[0m" + "를 쓰러트려 주십시오!")
# 반복문으로 들어가기 전 각자의 체력 상태를 확인
print("각자의 현재 체력 상태입니다. 주의하세요.")
Player.show_status(player)
Monster.show_status(devil)

while True:
    # 공격 방식 선택
    print("공격 방법을 선택해주세요.")
    select_attack = int(
        input("1."+"\033[96m{통상공격}\033[0m" + "2." + "\033[93m{마법공격}\033[0m"))

    # #공격후 스테이터스 확인
    if select_attack == 1:
        player.attack(devil)
    elif select_attack == 2:
        player.mattack(devil)
        print(f"\033[32m{player.name}\033[0m" + "의 잔여MP : " +
              f"\033[34m{player.mp}\033[0m" + "/" + f"\033[34m{player.mp_max}\033[0m")

    else:
        print("잘못 선택하셨습니다.")
        continue
    devil.attack(player)

    Player.status_check(player)
    Monster.status_check(devil)

    time.sleep(1)

    if devil.hp == 0:
        print(f"\033[31m{devil.name}\033[0m" +
              "이(가) 쓰러졌습니다. 당신의 승리입니다. 저희는 구원받을 것입니다.")
        print("Game clear")
        break
    elif player.hp == 0:
        print(f"\033[32m{player.name}\033[0m" +
              "이(가) 쓰러졌습니다. 당신의 죽음으로 인해 악마는 지옥을 벗어나 지상으로 향합니다.")
        print("You die")
        break
