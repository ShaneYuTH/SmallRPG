from random import randint
from textwrap import dedent


class Combat(object):

    def __init__(self, user, monster):
        self.user = user
        self.monster = monster

    def combat_start(self):
        round = 1
        first_move = randint(0, 1)
        if first_move == 0:
            print(dedent(f"""
                 Heads Up, {self.user.name} Go First!
                 """))
        else:
            print(dedent(f"""
                 Tails Up, {self.monster.name} Go First!
                 """))
        while self.monster.health > 0 and self.user.health > 0:
            user_attack = randint(self.user.attack - 2, self.user.attack + 2)
            monster_attack = randint(
                self.monster.attack - 2, self.monster.attack + 2)
            user_attack_minus_defense = user_attack - self.monster.defense
            monster_attack_minus_defense = monster_attack - self.user.defense
            if user_attack_minus_defense <= 0:
                user_attack_minus_defense = 1
            if monster_attack_minus_defense <= 0:
                monster_attack_minus_defense = 1
            if first_move == 0:
                print(f"Round {round}: ")
                self.monster.health -= user_attack_minus_defense
                if self.monster.health <= 0:
                    self.monster.health = 0
                    print(
                        f"{self.user.name} causes {user_attack} damage, {self.monster.name} has {self.monster.health} HP left.")
                    print(f"{self.user.name} Win!")
                    # Combat Finished. User Win
                else:
                    print(
                        f"{self.user.name} causes {user_attack} damage, {self.monster.name} has {self.monster.health} HP left.")
                    self.user.health -= monster_attack_minus_defense
                    if self.user.health <= 0:
                        self.user.health = 0
                        print(
                            f"{self.monster.name} causes {monster_attack} damage, {self.user.name} has {self.user.health} HP left.")
                        print(f"{self.monster.name} Win!")
                        # Combat Finished. Game End
                    else:
                        print(
                            f"{self.monster.name} causes {monster_attack} damage, {self.user.name} has {self.user.health} HP left.")
                        round += 1

            else:
                print(f"Round {round}: ")
                self.user.health -= monster_attack_minus_defense
                if self.user.health <= 0:
                    self.user.health = 0
                    print(
                        f"{self.monster.name} causes {monster_attack} damage, {self.user.name} has {self.user.health} HP left.")
                    print(f"{self.monster.name} Win!")
                    # Combat Finished. Game End

                else:
                    print(
                        f"{self.monster.name} causes {monster_attack} damage, {self.user.name} has {self.user.health} HP left.")
                    self.monster.health -= user_attack_minus_defense
                    if self.monster.health <= 0:
                        self.monster.health = 0
                        print(
                            f"{self.user.name} causes {user_attack} damage, {self.monster.name} has {self.monster.health} HP left.")
                        print(f"{self.user.name} Win!")
                        # Combat Finished. User Win
                    else:
                        print(
                            f"{self.user.name} causes {user_attack} damage, {self.monster.name} has {self.monster.health} HP left.")
                        round += 1
