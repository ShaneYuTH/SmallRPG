from random import randint, randrange
from textwrap import dedent


class UserGen(object):

    def __init__(self):
        self.name = input("Please Enter Your Name: \n> ")
        health, attack, defense = self.roll_stat()
        self.health = health
        self.attack = attack
        self.defense = defense
        self.killcount = 0
        self.cavecount = 0
        self.translator = False
        self.feed = False
        self.key = False
        self.truth = False
        self.cavesecret = False
        self.cave2castle = False

    def roll_stat(self):
        reroll = "Y"
        while reroll == "Y":
            health = randrange(50, 100, 10)
            attack = randint(5, 10)
            defense = randint(1, 5)
            lower_bound = attack - 2
            upper_bound = attack + 2
            if lower_bound <= 0:
                lower_bound = 1
            print(dedent(f"""
                 USER STATS
                 Name: {self.name}
                 HP  : {health}
                 ATK : {lower_bound} - {upper_bound}
                 DEF : {defense}
                 """))
            reroll = input("Do You Want to Reroll Your Stats? (Y/N)\n> ")
            while reroll != "Y" and reroll != "N":
                print("Wrong input, please re-enter")
                reroll = input("Do You Want to Reroll Your Stats? (Y/N)\n> ")
        return health, attack, defense

    def view_stat(self):
        lower_bound = self.attack - 2
        upper_bound = self.attack + 2
        if lower_bound <= 0:
            lower_bound = 1
        print(dedent(f"""
             USER STATS
             Name: {self.name}
             HP  : {self.health}
             ATK : {lower_bound} - {upper_bound}
             DEF : {self.defense}
             """))


class MonGen(object):

    adjective_pool = [
        "Aggressive",
        "Arrogant",
        "Boastful",
        "Bossy",
        "Boring",
        "Careless",
        "Clingy",
        "Cruel",
        "Cowardly",
        "Deceitful",
        "Dishonest",
        "Fussy",
        "Greedy",
        "Grumpy",
        "Harsh",
        "Impatient",
        "Impulsive",
        "Jealous",
        "Moody",
        "Narrow-minded",
        "Overcritical",
        "Rude",
        "Selfish",
        "Untrustworthy",
        "Unhappy"

    ]

    name_pool = [
        "Amelia",
        "Olivia",
        "Isla",
        "Emily",
        "Ava",
        "Poppy",
        "Isabella",
        "Jessica",
        "Lily",
        "Sophie",
        "Oliver",
        "Jack",
        "Harry",
        "Jacob",
        "Charlie",
        "Thomas",
        "George",
        "Oscar",
        "James",
        "William"
    ]

    # adj = adjective_pool[randint(0, len(adjective_pool) - 1)]
    # mon_name = name_pool[randint(0, len(name_pool) - 1)]

    def __init__(self):
        self.adj = MonGen.adjective_pool[randint(
            0, len(MonGen.adjective_pool) - 1)]
        self.mon_name = MonGen.name_pool[randint(0, len(MonGen.name_pool) - 1)]
        self.name = "{} Troll {}".format(self.adj, self.mon_name)
        self.health = randrange(5, 15, 5)
        self.attack = randint(1, 5)
        self.defense = randint(1, 5)

    def view_stat(self):
        lower_bound = self.attack - 2
        upper_bound = self.attack + 2
        if lower_bound <= 0:
            lower_bound = 1
        print(dedent(f"""
             Troll STATS
             Name: {self.name}
             HP  : {self.health}
             ATK : {lower_bound} - {upper_bound}
             DEF : {self.defense}
             """))


class GolemGen(object):
    """docstring for GolemGen."""

    def __init__(self):
        self.name = "Magic Golem"
        self.health = randrange(20, 30, 5)
        self.attack = randint(5, 10)
        self.defense = randint(1, 5)

    def view_stat(self):
        lower_bound = self.attack - 2
        upper_bound = self.attack + 2
        if lower_bound <= 0:
            lower_bound = 1
        print(dedent(f"""
             Golem STATS
             Name: {self.name}
             HP  : {self.health}
             ATK : {lower_bound} - {upper_bound}
             DEF : {self.defense}
             """))


class WitchGen(object):
    """docstring for WitchGen."""

    def __init__(self):
        self.name = "Dangerous Princess"
        self.health = randrange(15, 25, 5)
        self.attack = randint(5, 10)
        self.defense = randint(1, 5)

    def view_stat(self):
        lower_bound = self.attack - 2
        upper_bound = self.attack + 2
        if lower_bound <= 0:
            lower_bound = 1
        print(dedent(f"""
             Princess STATS
             Name: {self.name}
             HP  : {self.health}
             ATK : {lower_bound} - {upper_bound}
             DEF : {self.defense}
             """))


class Change_Stat(object):
    # char can be either user or monster
    def __init__(self, char):
        self.char = char

    def change_health(self, value):
        self.char.health += value

    def change_attack(self, value):
        self.char.attack += value

    def change_defense(self, value):
        self.char.defense += value

    def change_killcount(self):
        self.char.killcount += 1

    def change_cavecount(self):
        self.char.cavecount += 1

    def change_trans_stat(self):
        self.char.translator = True

    def change_feed_stat(self):
        self.char.feed = True

    def change_key_stat(self):
        self.char.key = True

    def change_truth_stat(self):
        self.char.truth = True

    def change_cavesecret_stat(self):
        self.char.cavesecret = True

    def change_cave2castle_stat(self):
        self.char.cave2castle = True


class Get_Stat(object):

    def __init__(self, char):
        self.char = char

    def get_name(self):
        return self.char.name

    def get_health(self):
        return self.char.health

    def get_killcount(self):
        return self.char.killcount

    def get_cavecount(self):
        return self.char.cavecount

    def get_trans_stat(self):
        return self.char.translator

    def get_feed_stat(self):
        return self.char.feed

    def get_key_stat(self):
        return self.char.key

    def get_truth_stat(self):
        return self.char.truth

    def get_cavesecret_stat(self):
        return self.char.cavesecret

    def get_cave2castle_stat(self):
        return self.char.cave2castle
