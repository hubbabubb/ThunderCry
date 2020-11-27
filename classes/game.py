from classes.magic import Spells
from classes.inventory import Collectables

import random
import pickle


class LevelItem:
    def __init__(self, icon, name, on, pos_x=0, pos_y=0):
        self.icon = icon
        self.name = name
        self.on = on
        self.pos_x = pos_x
        self.pos_y = pos_y

    def is_close(self, board, player):
        if self.pos_x - 1 == player.pos_x and self.pos_y == player.pos_y or self.pos_x + 1 == player.pos_x and self.pos_y == player.pos_y or self.pos_x == player.pos_x and self.pos_y - 1 == player.pos_y or self.pos_x == player.pos_x and self.pos_y + 1 == player.pos_y:
            return True
        else:
            return False

    def turn_off(self, board):
        board[self.pos_x][self.pos_y] = '  '
        self.on = False

    def turn_on(self, board):
        board[self.pos_x][self.pos_y] = self.icon
        self.on = True


class CharacterTypes:
    wizzard_him = '🧙🏻‍♂️'
    wizzard_her = '🧙‍♀️'
    elf_him = '🧝‍♂️'
    elf_her = '🧝🏽‍♀️'
    zombie_him = '🧟‍♂️'
    zombie_her = '🧟‍♀️'


class TextFormat:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[39m'
    BRIGHT = '\033[1m'
    DIM = '\033[2m'
    NORMAL = '\033[22m'
    RESET_ALL = '\033[0m'
    Bold = "\x1b[1m"
    Dim = "\x1b[2m"
    Italic = "\x1b[3m"
    Underlined = "\x1b[4m"
    LIGHT_GRAY = "\x1b[37m"
    DARK_GRAY = "\x1b[90m"


class TextBackground:
    LIGHT_GRAY = "\x1b[47m"
    DARK_GRAY = "\x1b[100m"
    BLACK = '\033[40m'
    RED = '\033[41m'
    GREEN = '\033[42m'
    YELLOW = '\033[43m'
    BLUE = '\033[44m'
    MAGENTA = '\033[45m'
    CYAN = '\033[46m'
    WHITE = '\033[47m'
    what = '\033[48m'
    RESET = '\033[49m'
    B_LightGray = "\x1b[47m"
    B_DarkGray = "\x1b[100m"


class Person:
    def __init__(self, icon, name, hp, mp, atk, df, spell_list, items, tools=[], level=0, pos_x=0, pos_y=0, on=True):
        self.icon = icon
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atk = atk
        self.maxatk = atk
        self.df = df
        self.maxdf = df
        self.spell_list = spell_list
        self.items = items
        self.action = ["Attack " + str(atk), "Magic (overwrite shield)", "Use item"]
        self.tools = tools
        self.level = level
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.on = on

    def generate_damage(self):
        return random.randrange(self.atk - 15, self.atk + 15)

    def take_damage(self, dmg):
        self.hp -= dmg
        self.hp = max(0, self.hp)
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def manna(self, dmg):
        self.mp += dmg
        if self.mp > self.maxmp:
            self.mp = self.maxmp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def generate_df(self):
        return random.randrange(1, 4)

    def get_item(self, item, quantity):
        if item.type != 'tool':
            for index, current_item in enumerate(self.items):
                if current_item['item'].name == item.name:
                    self.items[index]['quantity'] += quantity
                    return quantity
            self.items.append({'item': item, 'quantity': quantity})
        else:
            self.tools.append(item)

    def print_action(self):
        print(TextFormat.Bold + "  │  Actions: " + TextFormat.RESET_ALL)
        for index, item in enumerate(self.action):
            print(f"  │ {index+1}: {item}")

    def print_magic(self):
        print(TextFormat.Bold + "  │  Magic: " + TextFormat.RESET_ALL)
        print("  │ -- 0. cancel")
        for index, spell in enumerate(self.spell_list):
            print(f"  │ -- {index+1}: {spell.name}" + TextFormat.CYAN + f" (cost: {spell.cost}, dmg: {spell.dmg})" + TextFormat.RESET_ALL)

    def print_items(self):
        print(TextFormat.Bold + "  │  Items: " + TextFormat.RESET_ALL)
        print("  │ -- 0. cancel")
        i = 0
        for item in self.items:
            if item['item'].type != 'tool':
                print(f"  │ -- {i+1}: {item['item'].name}" + TextFormat.BLUE + f" ({item['item'].description}) x{item['quantity']}" + TextFormat.RESET_ALL)
                i += 1

    def get_random_move(self, board):
        board[self.pos_x][self.pos_y] = '  '
        x = [6, 7, 8, 9]
        y = [35, 34, 33, 32]
        self.pos_x = random.choice(x)
        self.pos_y = random.choice(y)
        board[self.pos_x][self.pos_y] = self.icon

    def move_right(self, board, step_cell='  '):
        if board[self.pos_x][self.pos_y + 1] == step_cell:
            board[self.pos_x][self.pos_y] = step_cell
            board[self.pos_x][self.pos_y + 1] = self.icon
            self.pos_y += 1

    def move_left(self, board, step_cell='  '):
        if board[self.pos_x][self.pos_y - 1] == step_cell:
            board[self.pos_x][self.pos_y] = step_cell
            board[self.pos_x][self.pos_y - 1] = self.icon
            self.pos_y -= 1

    def move_up(self, board, step_cell='  '):
        if board[self.pos_x - 1][self.pos_y] == step_cell:
            board[self.pos_x][self.pos_y] = step_cell
            board[self.pos_x - 1][self.pos_y] = self.icon
            self.pos_x -= 1

    def move_down(self, board, step_cell='  '):
        if board[self.pos_x + 1][self.pos_y] == step_cell:
            board[self.pos_x][self.pos_y] = step_cell
            board[self.pos_x + 1][self.pos_y] = self.icon
            self.pos_x += 1

    def is_close(self, board, player):
        if self.pos_x - 1 == player.pos_x and self.pos_y == player.pos_y or self.pos_x + 1 == player.pos_x and self.pos_y == player.pos_y or self.pos_x == player.pos_x and self.pos_y - 1 == player.pos_y or self.pos_x == player.pos_x and self.pos_y + 1 == player.pos_y:
            return True
        else:
            return False

    def turn_off(self, board):
        board[self.pos_x][self.pos_y] = '  '
        self.on = False

    def turn_on(self, board):
        board[self.pos_x][self.pos_y] = self.icon
        self.on = True


class Enemies:
    # WONDER FIELD
    pig = Person('🐗', 'The Tusker', 600, 1, 100, 7, [], [{'item': Collectables.tusk, 'quantity': 2}], pos_x=10, pos_y=28)
    crocodile = Person('🐊', 'Cocodrillo', 400, 1, 110, 13, [], [], pos_x=6, pos_y=13)
    crocodile2 = Person('🐊', 'Crocodrillo', 420, 1, 105, 12, [], [], pos_x=4, pos_y=18)
    goblin = Person('👹', 'goblin', 800, 70, 120, 5, [Spells.fire], [{'item': Collectables.knife, 'quantity': 3},
                                                                     {'item': Collectables.mushroom, 'quantity': 1}], pos_x=5, pos_y=37)
    # WILD WILDS
    peasant = Person('️👨🏼‍🌾', 'Peasant', 1000, 1, 105, 5, [], [{'item': Collectables.knife, 'quantity': 1}, {'item': Collectables.mushroom, 'quantity': 1}], pos_x=2, pos_y=20)
    goblin1 = Person('👹', 'Joe', 650, 70, 120, 5, [Spells.fire], [{'item': Collectables.knife, 'quantity': 1}, {'item': Collectables.mushroom, 'quantity': 1}], pos_x=5, pos_y=6)
    goblin2 = Person('👹', 'Joey', 750, 105, 120, 10, [Spells.fire], [{'item': Collectables.knife, 'quantity': 2}, {'item': Collectables.mushroom, 'quantity': 1}], pos_x=5, pos_y=10)
    goblin3 = Person('👹', 'Jose', 850, 140, 120, 15, [Spells.fire], [{'item': Collectables.knife, 'quantity': 3}, {'item': Collectables.mushroom, 'quantity': 2}], pos_x=9, pos_y=8)
    mustache = Person('👺', 'Mustache', 1200, 1, 125, 5, [], [{'item': Collectables.hammer, 'quantity': 3}, {'item': Collectables.wolf, 'quantity': 1}], pos_x=14, pos_y=25)
    guard1 = Person('️💂🏿‍', '💂🏿 Guards', 1000, 1, 115, 50, [], [{'item': Collectables.sword, 'quantity': 3}, {'item': Collectables.double_sword, 'quantity': 1}], pos_x=17, pos_y=27, on=True)
    guard2 = Person('️💂🏿‍‍', 'Guard', 1000, 1, 115, 50, [], [{'item': Collectables.sword, 'quantity': 3}, {'item': Collectables.double_sword, 'quantity': 1}], pos_x=17, pos_y=28)

    # MAIN HALL
    vampire = Person('🧛🏻‍♂️', 'Vampire', 1550, 110, 150, 15, [Spells.curse_of_weakness, Spells.vampire_bite], [], pos_x=2, pos_y=34)
    guard1_1 = Person('️💂🏿‍‍', 'Guard', 1000, 1, 200, 50, [], [{'item': Collectables.sword, 'quantity': 3}, {'item': Collectables.double_sword, 'quantity': 1}], pos_x=6, pos_y=6)
    guard2_1 = Person('️💂🏿‍‍', 'Guard', 1000, 1, 200, 50, [], [{'item': Collectables.sword, 'quantity': 3}, {'item': Collectables.double_sword, 'quantity': 1}], pos_x=10, pos_y=10)
    guard3 = Person('️💂🏿‍‍', 'EliteGuard', 1400, 1, 270, 60, [], [{'item': Collectables.sword, 'quantity': 3}, {'item': Collectables.double_sword, 'quantity': 1}, {'item': Collectables.bow, 'quantity': 1},
                                                               {'item': Collectables.bomb, 'quantity': 3}], pos_x=6, pos_y=14)
    guard4 = Person('️💂🏿‍‍', 'Guard', 1000, 1, 200, 50, [], [{'item': Collectables.sword, 'quantity': 3},
                                                          {'item': Collectables.double_sword, 'quantity': 1}], pos_x=10, pos_y=18)
    guard5 = Person('️💂🏿‍‍', 'Guard', 1000, 1, 220, 50, [], [{'item': Collectables.sword, 'quantity': 3},
                                                          {'item': Collectables.double_sword, 'quantity': 1}], pos_x=6, pos_y=22)
    guard6 = Person('️💂🏿‍‍', 'Guard', 1000, 1, 200, 50, [], [{'item': Collectables.sword, 'quantity': 3},
                                                          {'item': Collectables.double_sword, 'quantity': 1}], pos_x=10, pos_y=26)
    thief = Person('👳🏻', 'Thief', 650, 70, 350, 5, [Spells.fire], [{'item': Collectables.grenade, 'quantity': 3},
                                                                   {'item': Collectables.spider, 'quantity': 3},
                                                                   {'item': Collectables.knife, 'quantity': 3}], pos_x=2, pos_y=6)

    # BASEMENT
    MadBot = Person('🤖', 'The_M@dBot', 2000, 210, 250, 25, [Spells.electricity, Spells.repair],
                    [{'item': Collectables.gear, 'quantity': 3},
                     {'item': Collectables.CD, 'quantity': 3}], pos_x=14, pos_y=3)
    virus1 = Person('👾', 'virus', 1350, 80, 230, 25, [Spells.electricity], [{'item': Collectables.CD, 'quantity': 3}], pos_x=12, pos_y=26)
    virus2 = Person('👾', 'vir_s', 1350, 80, 230, 25, [Spells.electricity], [{'item': Collectables.CD, 'quantity': 3}], pos_x=4, pos_y=35)
    alien = Person('👽', 'CreepyFace', 1500, 160, 285, 5, [Spells.electricity], [{'item': Collectables.CD, 'quantity': 3}], pos_x=15, pos_y=34)

    # MAIN HALL 2
    twins = Person('🎎', 'The Twins', 2500, 250, 250, 25, [Spells.hurricane, Spells.thunder, Spells.blizzard],
                    [{'item': Collectables.bomb, 'quantity': 1},
                     {'item': Collectables.double_sword, 'quantity': 2}], pos_x=8, pos_y=33)
    ghost1 = Person('👻', 'Joe BOO', 1500, 1, 350, 50, [], [], pos_x=2, pos_y=6)
    ghost2 = Person('👻', 'Joey BOO', 1500, 1, 350, 50, [], [], pos_x=14, pos_y=3)
    ghost3 = Person('👻', 'Jose BOO', 1500, 1, 350, 50, [], [], pos_x=14, pos_y=35)

    # TOWER
    eye = Person('👁 ', 'The Big Orb', 4000, 1000, 250, 25, [Spells.hurricane, Spells.blizzard, Spells.curse_of_weakness, Spells.meteor],
                 [{'item': Collectables.bomb, 'quantity': 5}])
    # OUTRO
    king = Person('🤴🏼', 'Thunder King', 1500, 1, 285, 5, [], [], pos_x=8, pos_y=17)


def read_save_file(file_name):
    try:
        with open(file_name, 'rb') as input:
            return pickle.load(input)
    except:
        return []


def write_save_file(file_name, table):
    with open(file_name, 'wb') as output:
        pickle.dump(table, output, pickle.HIGHEST_PROTOCOL)
