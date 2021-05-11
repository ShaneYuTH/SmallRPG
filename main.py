from map import Map


class Engine(object):

    def __init__(self):
        self.map_num = Map(0, 0)

    def play(self):

        current_num = self.map_num.opening_num()
        last_num = self.map_num.last_num(1, 4)

        while current_num != last_num:
            self.map_num.scenes.get(current_num).print_func()
            print("Please enter the direction you want to go: ")
            action = input("> ")
            current_num = self.map_num.next_num(action)

        self.map_num.scenes.get(current_num).print_func()


print("""
Welcome to play my game, this is the BETA version.
Drawing out the map while playing is strongly recommended.
This game is translated into English from Chinese by Google Translate.
      """)
a_game = Engine()
a_game.play()

print("""
特别感谢Peter Zhan对我写码遇到的困难提供带力帮助！
特别感谢Grace Zhao试玩我的游戏！
      """)
