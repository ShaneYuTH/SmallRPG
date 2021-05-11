from combat import Combat
from character import UserGen, MonGen, GolemGen, WitchGen, Change_Stat, Get_Stat


class DeepestForest(object):
    """docstring for ."""

    def __init__(self, user):
        self.user = user
        self.first_Time = True

    def print_func(self):
        if self.first_Time:
            print(f"""
Hello {Get_Stat(self.user).get_name()}, you wake up on a prairie, you look at your surroundings,
There seems to be a vague feeling of deja vu, but it may also be the sequelae of a long sleep. nice weather,
The breeze slowly gives people the warmth of spring. You see an old man approaching you hurriedly.

"Warrior! Save our princess, a group of orcs stormed into the castle to the southeast of us,
Now the princess has also become their captive! "

You look at the old man, a little at a loss, but you still decide to explore here first.
The north and the west seem to be an endless grassland, which does not seem to be the target direction.
The east and the south seem to be passable.

(East: E South: S West: W North: N)
(Use VIEW STATS to view your own attribute value)
                   """)
            self.first_Time = False
        else:
            print("""
Here is a large grassland, the north and west are covered by deep grass, growing higher and higher,
It gradually became difficult to settle, and the east and the south seemed to be passable.
The old man seemed to have fled into the distance and disappeared.

(East: E South: S West: W North: N)
(Use VIEW STATS to view your own attribute value)
                  """)


class ForestTop(object):
    """docstring for ."""

    def __init__(self, user):
        self.user = user
        self.monster = MonGen()
        self.first_Time = True

    def print_func(self):
        if self.first_Time:
            print("""
Here is a lush grassland, where you see the first wild flowers and flying butterflies,
The north is covered by deep grass, making it difficult to pass. The east and south are shrouded by flourishing trees.

Suddenly you feel a strong wind blowing from behind, it seems that someone is attacking from behind,
You turned around quickly, stepped aside, and found that it was an ugly troll.
To deal with such a behemoth, maybe seizing the opportunity is a good way to fight?

A. Preemptive strike
B. Back slowly
                  """)
            choice = input("> ")
            while choice != "A" and choice != "B":
                print("""
The input is incorrect, please re-enter.

A. Preemptive strike
B. Back slowly
                      """)
                choice = input("> ")
            if choice == "A":
                self.user.view_stat()
                self.monster.view_stat()
                Combat(self.user, self.monster).combat_start()
                if Get_Stat(self.user).get_health() == 0:
                    print("""
You're already dead.
                          """)
                    quit()
                    # 需要研究死法
                else:
                    print("""
You have some doubts why the trolls don’t seem to have a strong fighting spirit.
But this is just convenient for you to kill him, and you have strengthened your confidence in saving the princess!
                          """)
                    Change_Stat(self.user).change_killcount()
            if choice == "B":
                if Get_Stat(self.user).get_trans_stat():
                    print("""
You didn't choose to fight, staring into the eyes of the troll, you started to back away slowly,
But the troll didn't attack you, but was babbling in a language you didn't understand.

Because of the brooch, the troll's words seemed understandable.
The troll looks at you,

"Please help me! I used to live here, but one day I woke up and became like this!
Help me! I don't know how to turn back into a human being, maybe my compatriots will know.
Please ask them! "

You are a little confused and don't know who to trust.
                          """)
                if not Get_Stat(self.user).get_trans_stat():
                    print("""
You didn't choose to fight, staring into the eyes of the troll, you started to back away slowly,
But you find that the troll is not attacking you, but is babbling in a language you don’t understand.
You spread out your hands with a confused expression,
The troll also showed a confused expression and spread his hands.

You can only leave first.
                          """)
            self.first_Time = False
        else:
            print("""
Here is a lush grassland, where you see the first wild flowers and flying butterflies,
The north is covered by thick grass, making it difficult to pass.""")
            if Get_Stat(self.monster).get_health() == 0:
                print("""
Lying on the grass is the corpse of a troll,
The broken loincloth tried to maintain the final dignity of the dead troll.
                      """)
            else:
                if Get_Stat(self.user).get_trans_stat():
                    print("""
The troll didn't attack you, but was babbling in a language you didn't understand.

Because of the brooch, the troll's words seemed understandable.
The troll looks at you,

"Please help me! I used to live here, but one day I woke up and became like this!
Help me! I don't know how to turn back into a human being, maybe my compatriots will know.
Please ask them! "

You are a little confused and don't know who to trust.
                          """)
                if not Get_Stat(self.user).get_trans_stat():
                    print("""
The troll is babbling, speaking a language you don't understand.

You can only leave first.
                         """)


class PrairieTop(object):
    """docstring for ."""

    def __init__(self, user):
        self.user = user
        self.first_Time = True
        self.bird_life = True

    def print_func(self):
        if self.first_Time:
            print("""
Here trees began to grow vigorously, and the outside of the grassland seemed to be a forest.
The trees in the northern part of the forest gradually became denser and looked difficult to pass.
The trees in the east and south seemed to grow gradually sparse, with the sound of running water,
It sounds that the place farther away is bordered by a swift river.

The forest birds are singing and flowers are fragrant, and you are interrupted by bursts of rapid bird calls.
You found a bird’s nest on the tree, you tiptoed and probed your head and found a few fledgling chicks inside.
Chirping with his mouth open. Looks a little hungry. Maybe I should do something?""")
            if Get_Stat(self.user).get_feed_stat():
                print("""
A. Let the birds shut their mouths, kill the chicks, and return the forest to peace
B. Respect nature, retreat in place, and let mother bird feed chicks
C. Love and earnestly, feed the chicks, and use the bait that has been obtained
                      """)
                choice = input("> ")
                while choice != "A" and choice != "B" and choice != "C":
                    print("""
The input is incorrect, please re-enter.

A. Let the birds shut their mouths, kill the chicks, and return the forest to peace
B. Respect nature, retreat in place, and let mother bird feed chicks
C. Love and earnestly, feed the chicks, and use the bait that has been obtained
                          """)
                    choice = input("> ")
            else:
                print("""
A. Let the birds shut their mouths, kill the chicks, and return the forest to peace
B. Respect nature, retreat in place, and let mother bird feed chicks
                      """)
                choice = input("> ")
                while choice != "A" and choice != "B":
                    print("""
The input is incorrect, please re-enter.

A. Let the birds shut their mouths, kill the chicks, and return the forest to peace
B. Respect nature, retreat in place, and let mother bird feed chicks
                          """)
                    choice = input("> ")
            if choice == "A":
                print("""
You brutally killed all the chicks, without the annoying sound of birds, you enjoy a brief peace,
Until the mother bird who came back from the predator found it.
It attacked you fiercely.

Life: -20
                      """)
                Change_Stat(self.user).change_health(-20)
                self.bird_life = False
            elif choice == "B":
                print("""
You choose to respect nature, creatures have their own way of living. 
After a short break, you decide to continue on the road.
                      """)
            else:
                print("""
You took out the insect bait from your pocket and fed it to the hungry chicks.
The chicks were very happy. One of the chicks moved around, revealing a shiny brooch under him.

Obtained: shiny brooch (seems to understand the language of different creatures)
                      """)
                Change_Stat(self.user).change_trans_stat()
                self.bird_life = False
            self.first_Time = False

        else:
            print("""
Here trees began to grow vigorously, and the outside of the grassland seemed to be a forest.
The trees in the northern part of the forest gradually became denser and looked difficult to pass.
The trees in the east and south seemed to grow gradually sparse, with the sound of running water,
It sounds that the place farther away is bordered by a swift river.""")
            if not self.bird_life:
                print("""
The forest is quiet.
                      """)
            else:
                print("""
A burst of rapid bird calls continued. It seems that the mother bird has not returned from predation.
Maybe I should do something?""")
                if Get_Stat(self.user).get_feed_stat():
                    print("""
A. Let the birds shut their mouths, kill the chicks, and return the forest to peace
B. Respect nature, retreat in place, and let mother bird feed chicks
C. Love and earnestly, feed the chicks, and use the bait that has been obtained
                          """)
                    choice = input("> ")
                    while choice != "A" and choice != "B" and choice != "C":
                        print("""
The input is incorrect, please re-enter.

A. Let the birds shut their mouths, kill the chicks, and return the forest to peace
B. Respect nature, retreat in place, and let mother bird feed chicks
C. Love and earnestly, feed the chicks, and use the bait that has been obtained
                              """)
                        choice = input("> ")
                else:
                    print("""
A. Let the birds shut their mouths, kill the chicks, and return the forest to peace
B. Respect nature, retreat in place, and let mother bird feed chicks
                          """)
                    choice = input("> ")
                    while choice != "A" and choice != "B":
                        print("""
The input is incorrect, please re-enter.

A. Let the birds shut their mouths, kill the chicks, and return the forest to peace
B. Respect nature, retreat in place, and let mother bird feed chicks
                              """)
                        choice = input("> ")
                if choice == "A":
                    print("""
You brutally killed all the chicks, without the annoying sound of birds, you enjoy a brief peace,
Until the mother bird who came back from the predator found it.
It attacked you fiercely.

Life: -20
                          """)
                    Change_Stat(self.user).change_health(-20)
                    self.bird_life = False
                elif choice == "B":
                    print("""
You choose to respect nature, creatures have their own way of living. 
After a short break, you decide to continue on the road.
                          """)
                else:
                    print("""
You took out the insect bait from your pocket and fed it to the hungry chicks.
The chicks were very happy. One of the chicks moved around, revealing a shiny brooch under him.

Obtained: shiny brooch (seems to understand the language of different creatures)
                          """)
                    self.bird_life = False
                    Change_Stat(self.user).change_trans_stat()


class RiverBankTop(object):
    """docstring for ."""

    def __init__(self, user):
        self.user = user
        self.monster = MonGen()
        self.first_Time = 1

    def print_func(self):
        if self.first_Time == 1:
            print("""
Here is the periphery of the forest, the land is gradually covered by low vegetation, there are also scattered trees,
But the view is much wider than when in the forest.
You can already see the river flowing through the east and south surrounding this area,
In the swampy area bordering the waters in the north, it seems that some crocodiles snorkeling and impassable.
There is a bridge in the south that connects the back door of a towering castle.""")
            if Get_Stat(self.user).get_trans_stat():
                print("""
You find a troll muttering to himself, walking towards the river,

"I don't know if the secret of a mysterious cave in the south of the forest will be discovered."

You overheard the secrets of the cave, maybe it's worth exploring.
                      """)
                Change_Stat(self.user).change_cavesecret_stat()
            if not Get_Stat(self.user).get_trans_stat():
                print("""
You find a troll muttering, walking towards the river,
Babbling and babbling things you don't understand.
                     """)
            print("""Because the troll did not find you, you were able to avoid this potential battle.
                  """)
            self.first_Time = 2
        elif self.first_Time == 2:
            print("""
Here is the periphery of the forest, the land is gradually covered by low vegetation, there are also scattered trees,
But the view is much wider than when in the forest.
You can already see the river flowing through the east and south surrounding this area,
In the swampy area bordering the waters in the north, it seems that some crocodiles snorkeling and impassable.
There is a bridge in the south that connects the back door of a towering castle.

The troll who drank the water before found you now. Against such a behemoth,
Perhaps seizing the opportunity is a good way to fight? Or should I stay calm and watch the changes?

A. Preemptive strike
B. Respond calmly
                  """)
            choice_1 = input("> ")
            while choice_1 != "A" and choice_1 != "B":
                print("""
The input is incorrect, please re-enter.

A. Preemptive strike
B. Respond calmly
                      """)
                choice_1 = input("> ")
            if choice_1 == "A":
                self.user.view_stat()
                self.monster.view_stat()
                Combat(self.user, self.monster).combat_start()
                if Get_Stat(self.user).get_health() == 0:
                    print("""
You're already dead.
                          """)
                    quit()
                    # 需要研究死法
                else:
                    if Get_Stat(self.user).get_trans_stat():
                        print("""
The troll shouted:
"Please don't kill me, I can tell you a secret!"

A. Kill the troll
B. spare his life
                              """)
                        choice = input("> ")
                        while choice != "A" and choice != "B":
                            print("""
The input is incorrect, please re-enter.

A. Kill the troll
B. spare his life
                                  """)
                            choice = input("> ")
                        if choice == "A":
                            print("""
You are not interested in the secrets of the trolls, you gave the trolls a joy,
And kicked his body into the rushing water.
                                  """)
                            Change_Stat(self.user).change_killcount()
                        if choice == "B":
                            print("""
"I have the key to the back door of the castle! Please don't kill me!
There are countless treasures of gold and silver in the castle! You can get it whatever you want! "

The troll looks at you in horror, hoping you can spare him his life.
You took the key to the back door of the castle and spared the life of the troll.
The troll was grateful for Dade and ran away quickly.
                                  """)
                            Change_Stat(self.user).change_key_stat()
                    if not Get_Stat(self.user).get_trans_stat():
                        print("""
The troll babbled at you, and you gave the troll a good time.
And kicked his body into the rushing water.
                              """)
                        Change_Stat(self.user).change_killcount()
            if choice_1 == "B":
                print("""
You didn't attack blindly, but stood still.
The troll saw you from a distance and left here quickly.
                      """)
            self.first_Time = 3
        else:
            print("""
Here is the periphery of the forest, the land is gradually covered by low vegetation, there are also scattered trees,
But the view is much wider than when in the forest.
You can already see the river flowing through the east and south surrounding this area,
In the swampy area bordering the waters in the north, it seems that some crocodiles snorkeling and impassable.
There is a bridge in the south that connects the back door of a towering castle.
                  """)


class RiverTop(object):
    """docstring for ."""

    def __init__(self, user):
        self.user = user

    @staticmethod
    def print_func():
        print("""
This is a section of a spacious river with relatively gentle water flow.
You walk into the water and feel a hint of coolness. 
There is a danger of drowning if you go further. Can only be returned.
              """)


class ForestBottom(object):
    """docstring for ."""

    def __init__(self, user):
        self.user = user
        self.monster = MonGen()
        self.first_Time = True

    def print_func(self):
        if self.first_Time:
            print("""
Here is a lush grassland, where you see the first wild flowers and flying butterflies,
The west is covered by deep grass, making it difficult to pass.
A lone troll wandering the grassland found you and rushed towards you quickly.
To deal with such a behemoth, maybe seizing the opportunity is a good way to fight?

A. Preemptive strike
B. Waiting in place
                  """)
            choice = input("> ")
            while choice != "A" and choice != "B":
                print("""
The input is incorrect, please re-enter.

A. Preemptive strike
B. Waiting in place
                      """)
                choice = input("> ")
            if choice == "A":
                self.user.view_stat()
                self.monster.view_stat()
                Combat(self.user, self.monster).combat_start()
                if Get_Stat(self.user).get_health() == 0:
                    print("""
You're already dead.
                          """)
                    quit()
                    # 需要研究死法
                else:
                    print("""
Phew, this troll was finally killed!
You have some doubts why the trolls don’t seem to have a strong fighting spirit.
But this is just convenient for you to kill him, and you have strengthened your confidence in saving the princess!
                          """)
                    Change_Stat(self.user).change_killcount()
            if choice == "B":
                if Get_Stat(self.user).get_trans_stat():
                    print("""
You didn't choose to fight, watching the trolls rushing over, you stood there and waited,
But the troll didn't attack you, but was babbling in a language you didn't understand.

Because of the brooch, the troll's words seemed understandable.
The troll looks at you,

"Please help me! I used to live here, but one day I woke up and became like this!
Help me! I don't know how to turn back into a human being, maybe my compatriots will know.
Please ask them! "

You are a little confused and don't know who to trust.
                          """)
                else:
                    print("""
You didn't choose to fight, watching the trolls rushing over, you stood there and waited,
But the troll didn't attack you, but babbled in a language you didn’t understand.
You spread out your hands with a confused expression,
The troll also showed a confused expression and spread his hands.

You can only leave first.
                          """)
            self.first_Time = False
        else:
            print("""
Here is a lush grassland, where you see the first wild flowers and flying butterflies,
The west is covered by deep grass, making it difficult to pass.""")
            if Get_Stat(self.monster).get_health() == 0:
                print("""
On the grass lies the body of a troll,
The broken loincloth tried to maintain the final dignity of the dead troll.
                      """)
            else:
                if Get_Stat(self.user).get_trans_stat():
                    print("""
The troll didn't attack you, but was babbling in a language you didn't understand.

Because of the brooch, the troll's words seemed understandable.
The troll looks at you,

"Please help me! I used to live here, but one day I woke up and became like this!
Help me! I don't know how to turn back into a human being, maybe my compatriots will know.
Please ask them! "

You are a little confused and don't know who to trust.
                          """)
                else:
                    print("""
The troll is babbling and speaking in a language you don’t understand,

You can only leave first.
                          """)


class PrairieMiddle(object):
    """docstring for ."""

    def __init__(self, user):
        self.user = user
        self.first_Time = True

    def print_func(self):
        if self.first_Time:
            print("""
Here trees began to grow vigorously, and the outside of the grassland seemed to be a forest.
The river in the distance flows through the southern part of the forest. 
There is a bridge that allows you to cross the river.
The trees in the east seemed to gradually sparse, and there was the sound of running water, 
which sounded to be bordered by a turbulent river.
The forest birds and flowers are fragrant. 
You follow the birds and you find a small pond hidden in the depths of the forest.
Trees and shrubs envelop this pond, and a few rays of sunlight shine through the treetops on the lake.
It seems that the dust in the air can be seen dancing under the light.
It seems safe here? Or is there a huge danger hidden under the calm surface?

A. Drinking water
B. Lie down and rest
C. Observe calmly
                  """)
            choice = input("> ")
            while choice != "A" and choice != "B" and choice != "C":
                print("""
The input is incorrect, please re-enter.

A. Drinking water
B. Lie down and rest
C. Observe calmly
                      """)
                choice = input("> ")
            if choice == "A":
                print("""
You are lying on the edge of the pond, the water here seems to be very pure,
You reached into the pond and drank a few handfuls of water.

Health: +10
                      """)
                Change_Stat(self.user).change_health(10)
            elif choice == "B":
                print("""
You are very satisfied with the quiet environment here and decide to lie down and have a nap.

Health: +20
                      """)
                Change_Stat(self.user).change_health(20)
            else:
                print("""
You lie on the edge of the pond and observe it calmly for a while, and still can’t tell whether it’s dangerous or safe.
But you have found many small insects that are suitable as bait.
The survival instinct allows you to pick up a few small bugs and put them in your backpack in case of accidents.
Otherwise, you have no more useful discoveries.
You decide to leave here first.

Obtained: Ordinary bait (can be fed to people in need or other animals)
                      """)
                Change_Stat(self.user).change_feed_stat()
            self.first_Time = False
        else:
            print("""
Here trees began to grow vigorously, and the outside of the grassland seemed to be a forest.
The river in the distance flows through the southern part of the forest. 
There is a bridge that allows you to cross the river.
The trees in the east seemed to gradually sparse, and there was the sound of running water, 
which sounded to be bordered by a turbulent river.
                  """)


class RiverBankBottom(object):
    """docstring for ."""

    def __init__(self, user):
        self.user = user

    @staticmethod
    def print_func():
        print("""
Here is the periphery of the forest, the land is gradually covered by low vegetation,
There are also scattered trees, but the view is much wider than when in the forest.
You can already see the river flowing through the east and south surrounding this area, 
and the turbulent currents seem impassable.
The north is a forest.
The towering and dignified castle is located on the opposite bank of the river, with the doors and windows closed, 
making it impossible to see the internal conditions.
The steeple of the castle stands tall and eye-catching.
              """)


class CastleOutskirtBackDoor(object):
    """docstring for ."""

    def __init__(self, user):
        self.user = user
        self.door_open = False

    def print_func(self):
        print("""
This is outside the back door of the castle, surrounded by rivers on all sides, 
and only a bridge connects the other bank.""")
        if self.door_open:
            print("""
The back door of the castle was vacant, allowing you to enter and exit at will.
Type "BACKDOOR" to enter the castle from the back door.
                      """)
        else:
            print("""
You explored the surroundings carefully, it seems that there is no way to enter the castle,
There is a keyhole on the door, and it seems that the key can be obtained to open the door.""")
            if Get_Stat(self.user).get_key_stat():
                print("""
You took out the key you got from the troll, and quietly opened the back door of the castle.
Type "BACKDOOR" to enter the castle from the back door.
                          """)
                self.door_open = True
            else:
                print("""
You have no way to pass here, you can only return first.
                      """)

    def get_door_stat(self):
        return self.door_open


class CastleTower(object):
    """docstring for ."""

    def __init__(self, user):
        self.user = user
        self.witch = WitchGen()

    def print_func(self):
        print("""
You climbed up the narrow spiral staircase and finally entered the top of the spire, 
where the princess sat quietly on the top of the tower.

"Warrior! You finally came to save me. I have been trapped on the top of the tower for a long time.
Those orcs wanted to take me away, but fortunately, I used a puppet to guard the tower, so take me away!\"""")
        if Get_Stat(self.user).get_truth_stat():
            print("""
You should confront the princess,

"You witch, the orcs told me everything you did. I came on this trip to stop your evil deeds."

The witch stood up, lowered her head and smiled, and when she raised her head again, 
her eyes were full of fierceness and a trace of disdain.

"You can't stop me, but since you already know this, I don't mind getting rid of a mouse that is an eyesore."

You are ready to fight, it's time to end it all.
                  """)
            self.user.view_stat()
            self.witch.view_stat()
            Combat(self.user, self.witch).combat_start()
            if Get_Stat(self.user).get_health() == 0:
                print("""
You're already dead.
                      """)
                quit()
                # 需要研究死法
            else:
                print("""
You worked so hard and finally defeated the Princess witch.
Seeing the witch fell to the ground, her eyes gradually lost focus, and you collapsed to the ground.

"Hope everything I do can put an end to the witch's vicious curse."

As you think in your heart, you gradually lose consciousness.

After not knowing how long, a strange young man shakes you up,

"Warrior! Warrior! Wake up!"

You open your eyes, look around, and find that there are still a few people around.
When they saw you awake, they celebrated loudly.
The young man continued,

"Thank you warrior! You killed the witch and helped us to lift the curse!
The other villagers and I have all turned back into humans! "

You struggled to stand up, looking out the window from the spire, a lot of people gathered in the square of the castle,
Seeing you poking out your head, everyone cheered in unison!

"Thank you warrior!"

You feel relieved that your hard work has not been in vain.
The feeling of being a beloved warrior is really great!

The End
                      """)
        else:
            print(f"""
You looked at the beautiful face of the princess and said,

"I'm {Get_Stat(self.user).get_name()}, I am here to save you!
Please don't be afraid, come with me, I will protect you!"

The princess smiled slyly, holding your hand, and walking down the tower that bound the princess with you.

THE END
                  """)


class PrairieBottom(object):
    """docstring for ."""

    def __init__(self, user):
        self.user = user
        self.first_Time = True

    def print_func(self):
        if self.first_Time:
            print("""
Here trees began to grow vigorously, and the outside of the grassland seemed to be a forest.
The trees in the western part of the forest are becoming denser, and it seems difficult to pass.
The river in the distance flows through the eastern part of the forest, 
and the turbulent currents seem to be impassable for people to pass.
The forest is still extending south.

In the distance, an injured figure was vaguely seen lying on the ground,
That person seems to have found you too, is crawling towards you step by step, and seems to be eager to approach you.

A. Run immediately to check the situation
B. Keep calm and approach slowly
                  """)
            choice = input("> ")
            while choice != "A" and choice != "B":
                print("""
The input is incorrect, please re-enter.

A. Run immediately to check the situation
B. Keep calm and approach slowly
                      """)
                choice = input("> ")
            if choice == "A":
                print("""
You ran over quickly, and saw him dressed in good clothes with castle symbol embroidered on it.
But the blood has soaked his clothes, and some places have already turned black.
He raised his head and raised his hand, as if he wanted to grab you.

"Help me...
Princess... Fake...
Deep... Pass through..."

He was talking intermittently, his eyes gradually lost his spirit, and his head dropped to the ground, motionless.

You look at the direction he is coming from, it seems to come from deeper in the forest further south.
What was the situation inside the castle, and how did he escape here.
You are lost in thought.
                      """)
                Change_Stat(self.user).change_cave2castle_stat()
            if choice == "B":
                print("""
You walked over slowly, maintaining a high degree of vigilance.
He seemed to have lost his breath, his eyes lost his focus, and his head dropped to the ground, motionless.
He is dressed in decent clothes, with the coat of arms of the castle embroidered on his chest,
But the blood has soaked his clothes, and some places have turned black.
                      """)
            self.first_Time = False
        else:
            print("""
Here trees began to grow vigorously, and the outside of the grassland seemed to be a forest.
The trees in the western part of the forest are becoming denser, and it seems difficult to pass.
The river in the distance flows through the eastern part of the forest, 
and the turbulent currents seem to be impassable for people to pass.
The forest is still extending south.

A blood-soaked corpse lying in the middle of the forest seemed to have begun to stiffen.
                  """)


class CastlePlaza(object):
    """docstring for ."""

    def __init__(self, user):
        self.user = user
        self.monster = MonGen()
        self.first_Time = True

    def print_func(self):
        if self.first_Time:
            print("""
This is the square in front of the castle. The huge square no more represents its hustle and bustle of the past.
Gives a feeling of depression.
When you look across the square, the castle gate seems to be tightly closed.
The majestic castle behind the gate does not seem to welcome you as an outsider.

There is a troll standing opposite you in the middle of the square, and he has spotted you.

A. Stand up and fight
B. Face it calmly
                  """)
            choice = input("> ")
            while choice != "A" and choice != "B":
                print("""
The input is incorrect, please re-enter.

A. Face to face
B. Face it calmly
                      """)
                choice = input("> ")
            if choice == "A":
                self.user.view_stat()
                self.monster.view_stat()
                Combat(self.user, self.monster).combat_start()
                if Get_Stat(self.user).get_health() == 0:
                    print("""
You're already dead.
                          """)
                    quit()
                    # 需要研究死法
                else:
                    print("""
Phew, you finally killed this troll,
You have some doubts why the trolls don’t seem to have a strong fighting spirit.
But this is just convenient for you to kill him, and you have strengthened your confidence in saving the princess!
                          """)
            if choice == "B":
                if Get_Stat(self.user).get_killcount() == 0:
                    if Get_Stat(self.user).get_trans_stat():
                        print("""
You didn't choose to fight, the troll came to you.

Because of the brooch, the troll's words seemed understandable.

The troll looks at you,

"Please save us, we are human beings who have lived in this land for generations,
Because we offended people in the big castle, the princess of the castle cursed us, and we have become the trolls!
Please kill the princess and our curse will be lifted! "

What should I do?
                              """)
                        Change_Stat(self.user).change_truth_stat()
                    else:
                        print("""
You didn't choose to fight, the troll came to you.
Listening to the troll babbling and speaking in a language you don’t understand,
You showed a confused expression and spread your hands.
The troll also showed a confused expression and spread his hands.

You can only leave first.
                              """)
                else:
                    if Get_Stat(self.user).get_trans_stat():
                        print("""
You didn't choose to fight, the troll came to you.
Because of the brooch, the troll's words seemed understandable.

The troll looks at you,

"Your body is stained with the blood of my compatriots, and I want to avenge my compatriots."

The battle is unavoidable.
                              """)
                        self.user.view_stat()
                        self.monster.view_stat()
                        Combat(self.user, self.monster).combat_start()
                        if Get_Stat(self.user).get_health() == 0:
                            print("""
You're already dead.
                                  """)
                            quit()
                            # 需要研究死法
                        else:
                            print("""
Phew, this troll was finally killed, and you have strengthened your confidence in saving the princess!
                                  """)
                    else:
                        print("""
You didn't choose to fight, the troll came to you.
Listening to the troll babbling and speaking in a language you don’t understand,
You showed a confused expression and spread your hands.
The troll shook his head and attacked you.

The battle is unavoidable.
                              """)
                        self.user.view_stat()
                        self.monster.view_stat()
                        Combat(self.user, self.monster).combat_start()
                        if Get_Stat(self.user).get_health() == 0:
                            print("""
You're already dead.
                                  """)
                            quit()
                            # 需要研究死法
                        else:
                            print("""
Phew, this troll was finally killed, and you have strengthened your confidence in saving the princess!
                                  """)
            self.first_Time = False
        else:
            print("""
This is the square in front of the castle. The huge square does not return to the bustle of the past.
Gives a feeling of depression. When you look across the square, the castle gate seems to be tightly closed.
The majestic castle behind the gate does not seem to welcome you as an outsider.""")
            if Get_Stat(self.monster).get_health() == 0:
                print("""
In the center of the square lies the corpse of a troll, 
and the broken loincloth tries to maintain the final dignity of the dead troll.
                      """)
            else:
                if Get_Stat(self.user).get_killcount() == 0:
                    if Get_Stat(self.user).get_trans_stat():
                        print("""
Because of the brooch, the troll's words seemed understandable.

The troll looks at you,

"Please save us, we are human beings who have lived in this land for generations,
Because we offended the adults in the castle, were princesses in the castle,
That is, the witch cursed us and turned us all into trolls!
Please kill the princess and our curse will be lifted! "

What should I do?
                              """)
                        Change_Stat(self.user).change_truth_stat()
                    else:
                        print("""
The troll is babbling, saying things you don't understand.

You can only leave first.
                              """)
                else:
                    if Get_Stat(self.user).get_trans_stat():
                        print("""
Because of the brooch, the troll's words seemed understandable.

The troll looks at you,

"Your body is stained with the blood of my compatriots, and I want to avenge my compatriots."

The battle is unavoidable.
                              """)
                        self.user.view_stat()
                        self.monster.view_stat()
                        Combat(self.user, self.monster).combat_start()
                        if Get_Stat(self.user).get_health() == 0:
                            print("""
You're already dead.
                                  """)
                            quit()
                            # 需要研究死法
                        else:
                            print("""
Phew, this troll was finally killed, and you have strengthened your confidence in saving the princess!
                                  """)
                    else:
                        print("""
The troll babbled and uttered a language you didn't understand, and attacked you.

The battle is unavoidable.
                              """)
                        self.user.view_stat()
                        self.monster.view_stat()
                        Combat(self.user, self.monster).combat_start()
                        if Get_Stat(self.user).get_health() == 0:
                            print("""
You're already dead.
                                  """)
                            quit()
                            # 需要研究死法
                        else:
                            print("""
Phew, this troll was finally killed, and you have strengthened your confidence in saving the princess!
                                  """)


class CastleFrontDoor(object):
    """docstring for ."""

    def __init__(self, user):
        self.user = user
        self.golem = GolemGen()
        self.first_Time = True

    def print_func(self):
        if self.first_Time:
            print("""
This is the main entrance of the castle, connecting the castle and the square in front of the castle.

You walked to the door and checked it carefully, and found that the door didn't seem to be closed, but was hidden.
With all your strength, you pushed open the gate of the castle, and what you saw was a huge magic puppet.
Seeing your arrival, the eyes of the magic puppet turned red, and this battle seemed inevitable.

Fight head-on!
                  """)
            self.user.view_stat()
            self.golem.view_stat()
            Combat(self.user, self.golem).combat_start()
            if Get_Stat(self.user).get_health() == 0:
                print("""
You're already dead.
                      """)
                quit()
                # 需要研究死法
            else:
                print("""
You have defeated the puppet guard, and the gate of the castle has been opened for you.

Type "PLAZA" to leave the castle
Type "ATRIUM" to enter the castle atrium
                      """)
            self.first_Time = False
        else:
            print("""
This is the main entrance of the castle, and it seems that you can enter/leave the castle from here.

The fragments of the puppet were scattered on the ground, suggesting a fierce battle taking place here.

Type "PLAZA" to leave the castle
Type "ATRIUM" to enter the castle atrium
                  """)


class CastleAtrium(object):
    """docstring for ."""

    def __init__(self, user):
        self.user = user
        self.first_Time = True
        self.fountain = True
        self.door_open = False

    def print_func(self):
        if self.first_Time:
            print("""
This is the atrium of the castle, and the gorgeous castle also reveals a gloomy atmosphere at this time.
There is a corridor connecting the back door of the castle.
The front of the atrium is the direction of the castle's main entrance, 
and the rear is connected to the steeple entrance deep in the castle.

There is a fountain in the middle of the atrium,
The fountain wrapped in pure white marble looks out of place in the castle at this time.
The sun shines on the fountain through the window, and there seems to be a rainbow light faintly emerging.
You decide to approach the fountain to find out.

When you walked to the fountain, there seemed to be a voice flashing in your ear:

"The princess is at the top of the castle tower, do what you think is worthwhile.
Drinking water from the fountain can make you energized. "

your choice:

A. Drink water
B. Leave
                  """)
            choice = input("> ")
            while choice != "A" and choice != "B":
                print("""
The input is incorrect, please re-enter.

A. Drink water
B. Leave
                      """)
                choice = input("> ")
            if choice == 'A':
                print("""
You choose to drink the water from the fountain, and the rainbow light of the fountain becomes dimmed.

Health: +50
                      """)
                Change_Stat(self.user).change_health(50)
                self.fountain = False
            if choice == 'B':
                print("""
Suspicious of the whispers in your ear, you left the fountain.
                      """)
            print("""Type "FRONTDOOR" to go to the main gate of the castle
Type "BACKDOOR" to leave the castle from the back door
Type "DEEP" to go to the depths of the castle
                  """)
            if Get_Stat(self.user).get_key_stat():
                self.door_open = True
            self.first_Time = False
        else:
            print("""
This is the atrium of the castle, and the gorgeous old castle also reveals a gloomy atmosphere at this time.
There is a corridor connecting the back door of the castle.
The front of the atrium is the direction of the castle's main entrance, 
and the rear is connected to the steeple entrance in the depths of the castle.""")
            if not self.fountain:
                print("""
The rainbow light of the fountain has dimmed, and it seems that it can no longer replenish your vitality.        
                      """)
            else:
                print("""
Do you still vaguely remember the whisper in your ear, are you trying to drink the spring water?

A. Drink water
B. Leave
                      """)
                choice = input("> ")
                while choice != "A" and choice != "B":
                    print("""
The input is incorrect, please re-enter.

A. Drink water
B. Leave
                          """)
                    choice = input("> ")
                if choice == 'A':
                    print("""
You choose to drink the water from the fountain, and the rainbow light of the fountain becomes dimmed.

Health: +50
                          """)
                    Change_Stat(self.user).change_health(50)
                    self.fountain = False
                if choice == 'B':
                    print("""
Suspicious of the whispers in your ear, you left the fountain.
                          """)
            print("""Type "FRONTDOOR" to go to the main gate of the castle
Type "BACKDOOR" to leave the castle from the back door
Type "DEEP" to go to the depths of the castle
                      """)
            if Get_Stat(self.user).get_key_stat():
                self.door_open = True

    def get_door_stat(self):
        return self.door_open


class CastleDeep(object):
    """docstring for ."""

    def __init__(self, user):
        self.user = user
        self.golem = GolemGen()
        self.first_Time = True
        self.cave = False

    def print_func(self):
        if self.first_Time:
            print("""
This is the depths of the castle, and the top of the castle spire is entered from here.
The stairs leading to the top of the tower are guarded by a magic puppet, seeing you appear,
The eyes of the puppet guard gradually turned red and rushed towards you! There is no other way but to fight!
                  """)
            self.user.view_stat()
            self.golem.view_stat()
            Combat(self.user, self.golem).combat_start()
            if Get_Stat(self.user).get_health() == 0:
                print("""
You're already dead.
                      """)
                quit()
                # 需要研究死法
            else:
                if Get_Stat(self.user).get_cave2castle_stat() and Get_Stat(self.user).get_cavecount() == 4:
                    print("""
You defeated the puppet guard, and the castle spire is now passable.

Type "TOWER" to enter the castle spire
Type "ATRIUM" to enter the castle atrium
Type "CAVE" to enter the cave secret path
                      """)
                    self.cave = True
                else:
                    print("""
You defeated the puppet guard, and the castle spire is now passable.

Type "TOWER" to enter the castle spire
Type "ATRIUM" to enter the castle atrium
                          """)
            self.first_Time = False
        else:
            if self.cave:
                print("""
This is the depths of the castle, and the top of the castle spire is entered from here.
The fragments of the puppet were scattered on the ground, suggesting a fierce battle taking place here.

Type "TOWER" to enter the castle spire
Type "ATRIUM" to enter the castle atrium
Type "CAVE" to enter the cave secret path
                      """)
            else:
                print("""
This is the depths of the castle, and the top of the castle spire is entered from here.
The fragments of the puppet were scattered on the ground, suggesting a fierce battle taking place here.

Type "TOWER" to enter the castle spire
Type "ATRIUM" to enter the castle atrium
                      """)

    def change_cave_stat(self):
        self.cave = True

    def get_cave_stat(self):
        return self.cave


class RiverBottom(object):
    """docstring for ."""

    def __init__(self, user):
        self.user = user
        self.first_Time = True
        self.cave = False

    def print_func(self):
        if self.first_Time:
            print("""
The trees here are gradually growing vigorously and seem to have reached the end of the forest.
The trees in the western part of the forest gradually became denser, making it difficult to pass through.
The river in the distance flows through the east and south of the forest,
Converging into a larger river, there was a deafening sound of water hitting the rock.
The turbulent current seemed impossible for people to pass through.""")
            if Get_Stat(self.user).get_cavecount() == 4:
                print("""
You came out of the cave.

Type "CAVE" to enter the cave
                      """)
                self.cave = True
            else:
                if Get_Stat(self.user).get_cavesecret_stat():
                    self.cave = True
                    print("""
You remembered what the orcs had said before, and began to look carefully,
Finally, a low hole was found under the cover of a few stones and leaves.
It was pitch black inside, and it seemed to swallow everything.
Facing the unknown in the cave, you are caught in a dilemma.

A. Enter
B. Return
                          """)
                    choice = input("> ")
                    while choice != "A" and choice != "B":
                        print("""
The input is incorrect, please re-enter.

A. Enter
B. Return
                              """)
                        choice = input("> ")
                    if choice == 'A':
                        print("""
The best way to eliminate fear is to face fear, persistence is victory! With a smile on your face, you enter the cave.

Type "CAVE" to enter the cave
                              """)
                    if choice == 'B':
                        print("""
In the face of unpredictable danger, rationality defeated sensibility. You did not choose to enter the cave.
                              """)
                else:
                    print("""
There is only the sound of surging water.
                          """)
            self.first_Time = False
        else:
            print("""
The trees here are gradually growing vigorously and seem to have reached the end of the forest.
The trees in the western part of the forest gradually became denser, making it difficult to pass through.
The river in the distance flows through the east and south of the forest and joins into a larger river,
There was a deafening sound of water hitting the rock.
The turbulent current seemed impossible for people to pass through.""")
            if self.cave:
                print("""
Type "CAVE" to enter the cave
                      """)
            else:
                if Get_Stat(self.user).get_cavesecret_stat():
                    self.cave = True
                    print("""
You remembered what the orcs had said before, and began to look carefully,
Finally, a low hole was found under the cover of a few stones and leaves.
It was pitch black inside, and it seemed to swallow everything.
Facing the unknown in the cave, you are caught in a dilemma.

A. Enter
B. Return
                          """)
                    choice = input("> ")
                    while choice != "A" and choice != "B":
                        print("""
The input is incorrect, please re-enter.

A. Enter
B. Return
                              """)
                        choice = input("> ")
                    if choice == 'A':
                        print("""
The best way to eliminate fear is to face fear, persistence is victory! With a smile on your face, you enter the cave.

Type "CAVE" to enter the cave
                              """)
                    if choice == 'B':
                        print("""
In the face of unpredictable danger, rationality defeated sensibility. You did not choose to enter the cave.
                              """)
                else:
                    print("""
There is only the sound of surging water.
                          """)


class CaveEntrance(object):
    """docstring for ."""

    def __init__(self, user):
        self.user = user
        self.first_Time = True

    def print_func(self):
        if self.first_Time:
            print("""
This place is close to the exit of the cave, with the light coming in from the entrance of the cave,
You can still vaguely see the road around you.
You can choose to continue deep into the cave or return to the ground.

Type "DEEP" to enter the depths of the cave
Type "OUT" to return to the hole
                  """)
            Change_Stat(self.user).change_cavecount()
            self.first_Time = False
        else:
            print("""
This place is close to the exit of the cave, with the light coming in from the entrance of the cave,
You can still vaguely see the road around you.
You can choose to continue deep into the cave or return to the ground.

Type "DEEP" to enter the depths of the cave
Type "OUT" to return to the hole
                  """)


class CaveOne(object):
    """docstring for ."""

    def __init__(self, user):
        self.user = user
        self.first_Time = True

    def print_func(self):
        if self.first_Time:
            print("""
It’s far from the entrance of the cave, and it’s dark in sight,
I can no longer see the surrounding roads. Can only groped the wall forward.

Type "DEEP" to enter the depths of the cave
Type "OUT" to return to the hole
                  """)
            Change_Stat(self.user).change_cavecount()
            self.first_Time = False
        else:
            print("""
It’s far from the entrance of the cave, and it’s dark in sight,
I can no longer see the surrounding roads. Can only groped the wall forward.

Type "DEEP" to enter the depths of the cave
Type "OUT" to return to the hole
                  """)


class CaveTwo(object):
    """docstring for ."""

    def __init__(self, user):
        self.user = user
        self.first_Time = True

    def print_func(self):
        if self.first_Time:
            print("""
It’s far from the entrance of the cave, and it’s dark in sight,
I can no longer see the surrounding roads. Can only groped the wall forward.

Type "DEEP" to enter the depths of the cave
Type "OUT" to return to the hole
                  """)
            Change_Stat(self.user).change_cavecount()
            self.first_Time = False
        else:
            print("""
It’s far from the entrance of the cave, and it’s dark in sight,
I can no longer see the surrounding roads. Can only groped the wall forward.

Type "DEEP" to enter the depths of the cave
Type "OUT" to return to the hole
                  """)


class CaveThree(object):
    """docstring for ."""

    def __init__(self, user):
        self.user = user
        self.first_Time = True
        self.castle = False

    def print_func(self):
        if self.first_Time:
            if Get_Stat(self.user).get_cavecount() < 4:
                print("""
You walked all the way from the secret road, out of a fireplace and into the depths of the cave.
This is a dark room with simple layout.
The fluorite on the roof of the cave is embedded in the wall, emitting a faint light.
There is a stone table on the ground, and a few stone benches surround the table,
Opposite the fireplace, there is a stone bed next to the wall in the distance.

Type "CASTLE" to return to the castle
Type "OUT" to return to the hole
                      """)
                self.castle = True
            else:
                print("""
There is a dim light coming from the deepest part of the cave, which is a simple dark room.
The fluorite on the roof of the cave is embedded in the wall, emitting a faint light.
There is a stone table on the ground, and a few stone benches surround the table,
There is a stone bed next to the wall in the distance, facing a fireplace,
There was only charcoal in it, and it seemed that it hadn't been burned in a long time.""")
                if Get_Stat(self.user).get_cave2castle_stat():
                    print("""
Through the dim light, you begin to calm down.
The various events I have seen before are constantly connected in my mind. 
If the dying person I saw before comes from the castle,and the forest is impassable in three directions, 
so he can only come from this cave.
You start to explore this secret room carefully, and you see a few dried blood stains on the ground.
Little by little it goes back to the extinguished fireplace.

You looked closely at the fireplace and found a secret door inside that seemed to lead to the castle.

Type "CASTLE" to return to the castle
Type "OUT" to return to the hole
                          """)
                    self.castle = True
                else:
                    print("""
You thought for a while under the dim light, and didn't have any clues. Maybe we can only leave first.

Type "OUT" to return to the hole
                          """)
            self.first_Time = False
            Change_Stat(self.user).change_cavecount()
        else:
            if self.castle:
                print("""
There is a dim light coming from the deepest part of the cave, which is a simple dark room.
The fluorite on the roof of the cave is embedded in the wall, emitting a faint light.
There is a stone table on the ground, and a few stone benches surround the table,
There is a stone bed next to the wall in the distance, facing a fireplace,
There was only charcoal in it, and it seemed that it hadn't been burned in a long time.

Type "CASTLE" to return to the castle
Type "OUT" to return to the hole
                      """)
            else:
                print("""
There is a dim light coming from the deepest part of the cave, which is a simple dark room.
The fluorite on the roof of the cave is embedded in the wall, emitting a faint light.
There is a stone table on the ground, a few stone benches around the table, 
and a stone bed next to the wall in the distance.
Facing a fireplace, there was only charcoal in it, and it seemed that it hadn't been burned for a long time.

There is no place to explore here. Perhaps leaving is the best policy.

Type "OUT" to return to the hole
                      """)

    def change_castle_stat(self):
        self.castle = True

    def get_castle_stat(self):
        return self.castle


class Map(object):
    map_num = [
        [0, 1, 2, 3, 4],
        [10, 11, 12, 13, 14],
        [20, 21, 22, 23, 24],
        [30, 31, 32, 33, 34]
    ]

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.start_num = self.map_num[a][b]
        self.user = UserGen()
        self.scenes = {
            0: DeepestForest(self.user),
            1: ForestTop(self.user),
            2: PrairieTop(self.user),
            3: RiverBankTop(self.user),
            4: RiverTop(self.user),
            10: ForestBottom(self.user),
            11: PrairieMiddle(self.user),
            12: RiverBankBottom(self.user),
            13: CastleOutskirtBackDoor(self.user),
            14: CastleTower(self.user),
            20: PrairieBottom(self.user),
            21: CastlePlaza(self.user),
            22: CastleFrontDoor(self.user),
            23: CastleAtrium(self.user),
            24: CastleDeep(self.user),
            30: RiverBottom(self.user),
            31: CaveEntrance(self.user),
            32: CaveOne(self.user),
            33: CaveTwo(self.user),
            34: CaveThree(self.user)
        }
        # print(self.start_num)

    def next_num(self, action):
        new_a = self.a
        new_b = self.b

        if self.a == 0 and self.b == 4:
            if action == 'W':
                new_b -= 1
            elif action == 'N' or action == 'S' or action == 'E':
                print("""
The icy river is getting deeper and is harder to pass.""")
            elif action == 'VIEW STATS':
                self.user.view_stat()
            else:
                print("""
The input is incorrect, please re-enter.""")

        elif self.a == 1 and self.b == 2:
            if action == 'N':
                new_a -= 1
            elif action == 'W':
                new_b -= 1
            elif action == 'S' or action == 'E':
                print("""
The icy river is getting deeper and is harder to pass.""")
            elif action == 'VIEW STATS':
                self.user.view_stat()
            else:
                print("""
The input is incorrect, please re-enter.""")

        elif self.a == 1 and self.b == 3:
            if action == 'BACKDOOR' and self.scenes.get(13).get_door_stat():
                new_a += 1
            elif action == 'BACKDOOR' and not self.scenes.get(13).get_door_stat():
                print("""
You push the door, it seems that only a key can be used to open it.""")
            elif action == 'N':
                new_a -= 1
            elif action == 'S' or action == 'W' or action == 'E':
                print("""
It is surrounded by water on three sides, and only the northern bridge allows you to return.""")
            elif action == 'VIEW STATS':
                self.user.view_stat()
            else:
                print("""
The input is incorrect, please re-enter.""")

        elif self.a == 2 and self.b == 0:
            if action == 'N':
                new_a -= 1
            elif action == 'S':
                new_a += 1
            elif action == 'W':
                print("""
It is blocked by obstacles and difficult to pass.""")
            elif action == 'E':
                print("""
The icy river is getting deeper and is harder to pass.""")
            elif action == 'VIEW STATS':
                self.user.view_stat()
            else:
                print("""
The input is incorrect, please re-enter.""")

        elif self.a == 2 and self.b == 1:
            if action == 'N':
                new_a -= 1
            elif action == 'S':
                print("""
It is blocked by obstacles and difficult to pass.""")
            elif action == 'W':
                print("""
The icy river is getting deeper and is harder to pass.""")
            elif action == 'E':
                new_b += 1
            elif action == 'VIEW STATS':
                self.user.view_stat()
            else:
                print("""
The input is incorrect, please re-enter.""")

        elif self.a == 2 and self.b == 2:
            if action == 'ATRIUM':
                new_b += 1
            elif action == 'PLAZA':
                new_b -= 1
            elif action == 'VIEW STATS':
                self.user.view_stat()
            else:
                print("""
The input is incorrect, please re-enter.""")

        elif self.a == 2 and self.b == 3:
            if action == 'BACKDOOR' and self.scenes.get(23).get_door_stat():
                print("""
You used the key to the back door of the castle to open the back door of the castle.
                """)
                new_a -= 1
            elif action == 'BACKDOOR' and not self.scenes.get(23).get_door_stat():
                print("""
You don't have the key to the back door of the castle, and you cannot open the back door of the castle.
                """)
            elif action == 'FRONTDOOR':
                new_b -= 1
            elif action == 'DEEP':
                new_b += 1
            elif action == 'VIEW STATS':
                self.user.view_stat()
            else:
                print("""
The input is incorrect, please re-enter.""")

        elif self.a == 2 and self.b == 4:
            if action == 'TOWER':
                new_a -= 1
            elif action == 'ATRIUM':
                new_b -= 1
            elif action == 'CAVE' and self.scenes.get(24).get_cave_stat():
                self.scenes.get(34).change_castle_stat()
                new_a += 1
            elif action == 'CAVE' and not self.scenes.get(24).get_cave_stat():
                print("""
You seem to know this well and discovered the secret tunnel of the cave.

Entered the cave from the secret path.""")
                self.scenes.get(34).change_castle_stat()
                new_a += 1
            elif action == 'VIEW STATS':
                self.user.view_stat()
            else:
                print("""
The input is incorrect, please re-enter.""")

        elif self.a == 3 and self.b == 0:
            if action == 'CAVE':
                new_b += 1
            elif action == 'N':
                new_a -= 1
            elif action == 'S' or action == 'E':
                print("""
The icy river is getting deeper and is harder to pass.""")
            elif action == 'W':
                print("""
The icy river is getting deeper and is harder to pass.""")
            elif action == 'VIEW STATS':
                self.user.view_stat()
            else:
                print("""
The input is incorrect, please re-enter.""")

        elif self.a == 3 and self.b == 1:
            if action == 'OUT':
                print("""
In the face of unpredictable danger, rationality defeated sensibility. You did not choose to go deep into the cave.""")
                new_b -= 1
            elif action == 'DEEP':
                print("""
You go deeper. The darkness has swallowed you.""")
                new_b += 1
            elif action == 'VIEW STATS':
                self.user.view_stat()
            else:
                print("""
The input is incorrect, please re-enter.""")

        elif self.a == 3 and self.b == 2:
            if action == 'OUT':
                print("""
In the face of unpredictable danger, rationality defeated sensibility. You did not choose to go deep into the cave.""")
                new_b -= 1
            elif action == 'DEEP':
                print("""
You go deeper. The darkness has swallowed you.""")
                new_b += 1
            elif action == 'VIEW STATS':
                self.user.view_stat()
            else:
                print("""
The input is incorrect, please re-enter.""")

        elif self.a == 3 and self.b == 3:
            if action == 'OUT':
                print("""
In the face of unpredictable danger, rationality defeated sensibility. You did not choose to go deep into the cave.""")
                new_b -= 1
            elif action == 'DEEP':
                print("""
You go deeper. There seems to be some light in front.""")
                new_b += 1
            elif action == 'VIEW STATS':
                self.user.view_stat()
            else:
                print("""
The input is incorrect, please re-enter.""")

        elif self.a == 3 and self.b == 4:
            if action == 'OUT':
                new_b -= 1
            elif action == 'CASTLE' and self.scenes.get(34).get_castle_stat():
                print("""
You seem to know this well, and you have discovered the secret passage that leads to the castle hidden in the fireplace.

Entered the castle from the secret road.""")
                self.scenes.get(24).change_cave_stat()
                new_a -= 1
            elif action == 'VIEW STATS':
                self.user.view_stat()
            else:
                print("""
The input is incorrect, please re-enter.""")

        elif action == 'VIEW STATS':
            self.user.view_stat()

        else:
            if action == 'N':
                new_a -= 1
            elif action == 'S':
                new_a += 1
            elif action == 'W':
                new_b -= 1
            elif action == 'E':
                new_b += 1
            else:
                print("""
The input is incorrect, please re-enter.""")

        if new_a < 0 or new_a > 4 or new_b < 0 or new_b > 4:
            print("""
It is blocked by obstacles and difficult to pass.""")
            return self.map_num[self.a][self.b]

        self.a = new_a
        self.b = new_b
        val = self.map_num[self.a][self.b]

        return val

    def opening_num(self):
        val = self.start_num
        return val

    def last_num(self, a, b):
        val = self.map_num[a][b]
        return val
