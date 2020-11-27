from classes.game import TextFormat, TextBackground, Enemies, Person, LevelItem
from classes.inventory import Collectables
from classes.magic import Spells
import time
import util
import engine
import random
import main
import pygame


def cheat_mode(player):
    key = util.key_pressed()

    if key == 'i':
        key = util.key_pressed()
        if key == 'd':
            key = util.key_pressed()
            if key == 'd':
                key = util.key_pressed()
                if key == 'q':
                    key = util.key_pressed()
                    if key == 'd':
                        player.get_item(Collectables.noob, 99)
                        player.get_item(Collectables.teleport, 1)
                        return player
                    else:
                        print("Missed the last one :)")
                        return player
                else:
                    print("Missed cheat")
                    return player
            else:
                print("Missed cheat")
                return player
        else:
            print("Missed cheat")
            return player
    elif key == 'u':
        for index, undo_cheat in enumerate(player.tools):
            if undo_cheat == '🖲 teleport':
                player.tools.pop(index)
            return player
    else:
        print("Missed cheat")
        return player


def quit_game():
    quit_choice = input("*** Are you sure you wants to quit (Y/N)? ")
    if quit_choice == 'Y' or quit_choice == 'y' or quit_choice == 'yes':
        print("*** See you next  time ***")
        exit()
    else:
        print("*** Nice! ***")
        time.sleep(1)
        return False


def print_player_statics(player):
    percent_hp = (int(player.get_hp())/player.maxhp) * 100
    percent_mp = (int(player.get_mp())/player.maxmp) * 100
    life_percent = int(int(25 * percent_hp) / 100)
    magic_percent = int(int(10 * percent_mp) / 100)
    print('  │ ' + TextFormat.Underlined + '   Name                   ' + TextFormat.BLUE + 'HP                            '
          + TextFormat.CYAN + 'MP           ' + TextFormat.YELLOW + '  🛡 ' + TextFormat.RESET_ALL + " │ ")
    print(f'  │ {player.icon} {player.name}' + ' ' * (16-(len(player.name))) + ' ' * (7 - (len(str(player.get_hp())))) + str(player.get_hp())
          + TextBackground.BLUE + '◼︎' * life_percent + TextBackground.RESET + ' ' * (25 - life_percent)
          + ' ' * (5 - (len(str(player.get_mp())))) + TextBackground.RESET + str(player.get_mp())
          + TextBackground.CYAN + '◼︎' * magic_percent + TextBackground.RESET + TextFormat.YELLOW
          + ' ' * (13 - magic_percent) + str(player.df) + TextFormat.RESET_ALL + ' ' * (5 - len(str(player.df))) + '│ ')


def print_enemy_statics(enemy):
    percent_hp = (int(enemy.get_hp()) / enemy.maxhp) * 100
    percent_mp = (int(enemy.get_mp()) / enemy.maxmp) * 100
    life_percent = int(int(25 * percent_hp) / 100)
    magic_percent = int(int(10 * percent_mp) / 100)
    print('  │ ' + TextFormat.Underlined + '   Name                   ' + TextFormat.RED + 'HP                            '
          + TextFormat.MAGENTA + 'MP           ' + TextFormat.YELLOW + '  🛡 ' + TextFormat.RESET_ALL + " │ ")
    print(f'  │ {enemy.icon} {enemy.name}' + ' ' * (16 - (len(enemy.name))) + ' ' * (7 - (len(str(enemy.get_hp())))) + str(enemy.get_hp())
          + TextBackground.RED + '◼︎' * life_percent + TextBackground.RESET + ' ' * (25 - life_percent)
          + ' ' * (5 - (len(str(enemy.get_mp())))) + TextBackground.RESET + str(enemy.get_mp())
          + TextBackground.MAGENTA + '◼︎' * magic_percent + TextBackground.RESET + TextFormat.YELLOW
          + ' ' * (13 - magic_percent) + str(enemy.df) + TextFormat.RESET_ALL + ' ' * (5 - len(str(enemy.df))) + '│ ')


def battle(player, enemy):
    battle_on = True
    poison_on_player = {'on': False, 'dmg': 0, 'round': 0}
    poison_on_enemy = {'on': False, 'dmg': 0, 'round': 0}
    curse_on_player = {'on': False, 'dmg': 0, 'round': 0}
    curse_on_enemy = {'on': False, 'dmg': 0, 'round': 0}

    while battle_on:
        # FIGHT OVER - ENEMY WINS?
        if player.get_hp() == 0:

            print(TextBackground.RED + TextFormat.BLACK + f"  │ ☠️  {enemy.icon}{enemy.name} killed you!  ☠️" + TextFormat.RESET_ALL)
            input("  │ Press ENTER to load from the last checkpoint...")
            return 0, player

        util.clear_screen()
        print("  ┌───────────────────────────────────────────────────────────────────────────┐")
        print_player_statics(player)
        if poison_on_player['on'] and curse_on_player['on']:
            dot = f' Poisoned: {poison_on_player["dmg"]}% /{poison_on_player["round"]} rounds and cursed for {curse_on_player["round"]} rounds.'
            print('  │ ' + TextFormat.RED + dot.center(72) + TextFormat.RESET_ALL + ' │')
        elif poison_on_player['on'] and not curse_on_player['on']:
            dot = f' Poisoned: {poison_on_player["dmg"]}% /{poison_on_player["round"]} rounds.'
            print('  │ ' + TextFormat.RED + dot.center(72) + TextFormat.RESET_ALL + ' │')
        elif not poison_on_player['on'] and curse_on_player['on']:
            dot = f' Cursed for {curse_on_player["round"]} rounds.'
            print('  │ ' + TextFormat.RED + dot.center(72) + TextFormat.RESET_ALL + ' │')
        else:
            print('  │                                                                           │')
        print("  ├───────────────────────────────────────────────────────────────────────────┘ ")
        print("  ├───────────────────────────────────────────────────────────────────────────┐")
        print_enemy_statics(enemy)
        if poison_on_enemy['on'] and curse_on_enemy['on']:
            dot_b = f' Poisoned: {poison_on_enemy["dmg"]}% /{poison_on_enemy["round"]} rounds and cursed for {curse_on_enemy["round"]} rounds.'
            print('  │ ' + TextFormat.RED + dot_b.center(73) + TextFormat.RESET_ALL + ' │ ')
        elif poison_on_enemy['on'] and not curse_on_enemy['on']:
            dot_b = f' Poisoned: {poison_on_enemy["dmg"]}% /{poison_on_enemy["round"]} rounds.'
            print('  │ ' + TextFormat.RED + dot_b.center(73) + TextFormat.RESET_ALL + ' │ ')
        elif not poison_on_enemy['on'] and curse_on_enemy['on']:
            dot_b = f' Cursed for {curse_on_enemy["round"]} rounds.'
            print('  │ ' + TextFormat.RED + dot_b.center(73) + TextFormat.RESET_ALL + ' │ ')
        else:
            print('  │                                                                           │ ')
        print("  ├───────────────────────────────────────────────────────────────────────────┘ ")
        player.print_action()
        action_choice = input("  │ Choose action: ")
        try:
            action_choice = int(action_choice) - 1
        except ValueError:
            continue

        if action_choice == 0:
            damage = player.generate_damage()
            enemy.take_damage(damage - enemy.df)
            print(TextFormat.BLUE + f"  │ You attacked for {damage - enemy.df}.")
            time.sleep(1)
        elif action_choice == 1:
            player.print_magic()

            magic_choice = input("  │ Choose a magic: ")
            try:
                magic_choice = int(magic_choice) - 1
            except ValueError:
                continue

            if magic_choice > len(player.spell_list) - 1:
                continue

            if magic_choice == -1:
                continue

            spell = player.spell_list[magic_choice]
            magic_damage = spell.generate_damage()

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(TextFormat.YELLOW + "  │ You don't have enough magic points!" + TextFormat.RESET_ALL)
                time.sleep(1)
                continue

            player.reduce_mp(spell.cost)

            if spell.type == 'white':
                player.heal(magic_damage)
                print(TextFormat.BLUE + f"  │ {spell.name} heals you for: {magic_damage} HP." + TextFormat.RESET_ALL)
                time.sleep(1)
            elif spell.type == "black":
                enemy.take_damage(magic_damage)
                print(TextFormat.RED + f"  │ {spell.name} take {magic_damage} HP from enemy." + TextFormat.RESET_ALL)
                time.sleep(1)
            elif spell.type == "zombie":
                enemy.take_damage(magic_damage)
                player.heal(magic_damage)
                print(TextFormat.RED + f"  │ {spell.name} take {magic_damage} HP from enemy and heals you." + TextFormat.RESET_ALL)
            elif spell.type == "curse":
                curse_on_enemy["on"] = True
                curse_on_enemy["dmg"] = spell.dmg
                curse_on_enemy["round"] = 4
            elif spell.type == "bless":
                poison_on_player['on'] = False
                curse_on_player['on'] = False
                player.atk = player.maxatk
                player.df = player.maxdf
                for reduced_item in player.items:
                    reduced_item['item'].prop = reduced_item['item'].maxprop
                for reduced_magic in player.spell_list:
                    reduced_magic.dmg = reduced_magic.maxdmg
        elif action_choice == 2:
            player.print_items()

            item_choice = input("  │ Choose an item from your inventory: ")
            try:
                item_choice = int(item_choice) - 1
            except ValueError:
                continue

            if item_choice == -1 or item_choice > len(player.items) - 1:
                continue

            quantity_choice = int(input('  │ Quantity (max 3): '))
            if quantity_choice > 3:
                print(TextFormat.YELLOW + "You can use maximum 3 items per round!" + TextFormat.RESET_ALL)
                time.sleep(1)
                continue

            item = player.items[item_choice]['item']
            quantity = int(player.items[item_choice]['quantity'])

            if quantity >= quantity_choice:
                player.items[item_choice]['quantity'] -= quantity_choice
            else:
                print(TextFormat.YELLOW + "  │ You can't afford that" + TextFormat.RESET_ALL)
                time.sleep(1)
                continue

            if player.items[item_choice]['quantity'] == 0:
                player.items.pop(item_choice)

            if item.type == 'potion':
                player.heal(item.prop * quantity_choice)
                print(TextFormat.BLUE + f"  │ {item.name} heals you for: {item.prop * quantity_choice} HP." + TextFormat.RESET_ALL)
                time.sleep(1)
            elif item.type == "elixir":
                player.manna(item.prop * quantity_choice)
                print(TextFormat.BLUE + f"  │ {item.name} recharge your MP with {item.prop * quantity_choice}." + TextFormat.RESET_ALL)
                time.sleep(1)
            elif item.type == "attack":
                enemy.take_damage((item.prop * quantity_choice) - enemy.df)
                print(TextFormat.RED + f"  │ {item.name} take {item.prop * quantity_choice - enemy.df} HP from enemy" + TextFormat.RESET_ALL)
                time.sleep(1)
            elif item.type == "poison":
                poison_on_enemy['on'] = True
                poison_on_enemy['dmg'] += item.prop
                poison_on_enemy['round'] = 3
            elif item.type == "vaccine":
                poison_on_player['on'] = False
                player.heal(item.prop * quantity_choice)
                curse_on_player['on'] = False
                player.atk = player.maxatk
                player.df = player.maxdf
                for reduced_item in player.items:
                    reduced_item['item'].prop = reduced_item['item'].maxprop
                for reduced_magic in player.spell_list:
                    reduced_magic.dmg = reduced_magic.maxdmg
            else:
                continue
        elif action_choice == 4:
            exit()
        else:
            continue

        # DAMAGE OVER TIME ON ENEMY
        if poison_on_enemy['on'] and poison_on_enemy['round'] != 0:
            poison_on_enemy['round'] -= 1
            percent = (enemy.maxhp * poison_on_enemy['dmg']) // 100
            enemy.take_damage(int(percent))
            print(TextFormat.RED + f'  │ Poison hits enemy {percent} HP.' + TextFormat.RESET_ALL)
            time.sleep(1)
        if poison_on_enemy['round'] == 0:
            poison_on_enemy['on'] = False

        # CURSE OVER TIME ON ENEMY
        if curse_on_enemy["on"] and curse_on_enemy["round"] != 0:
            enemy.atk = int(enemy.atk // 1.2)
            for reduced_magic in enemy.spell_list:
                reduced_magic.dmg = int(reduced_magic.dmg // 1.2)
            for reduced_item in enemy.items:
                reduced_item['item'].prop = int(reduced_item['item'].prop // 1.2)
            curse_on_enemy["round"] -= 1
            print(TextFormat.RED + f"  │ {enemy.name}'s attributes and items are cursed." + TextFormat.RESET_ALL)
            time.sleep(1)
        if curse_on_enemy["round"] == 0:
            curse_on_enemy["on"] = False
            enemy.atk = enemy.maxatk
            for reduced_item in enemy.items:
                reduced_item['item'].prop = reduced_item['item'].maxprop
            for reduced_magic in enemy.spell_list:
                reduced_magic.dmg = reduced_magic.maxdmg

        # FIGHT OVER - PLAYER WINS?
        if enemy.get_hp() == 0:
            print(TextBackground.GREEN + TextFormat.WHITE + "  │ You win the fight!" + TextFormat.RESET_ALL)
            time.sleep(1)
            return 1

        # ENEMY ATTACK CHOICE
        enemy_move_list = [1]
        if len(enemy.items) != 0:
            enemy_move_list.append(2)
        if len(enemy.spell_list) != 0:
            enemy_move_list.append(3)
        random_attack = random.choice(enemy_move_list)
        # ENEMY ATTACK WITH ITEM
        if random_attack == 2:
            item = enemy.items[0]['item']
            enemy.items[0]['quantity'] -= 1
            if item.type == "attack":
                player.take_damage(item.prop - player.df)
                print(TextFormat.RED + f"  │ Enemy attack with {item.name} take {item.prop - player.df} HP from you" + TextFormat.RESET_ALL)
            elif item.type == "elixir":
                enemy.heal(item.prop)
                enemy.manna(item.prop)
                print(TextFormat.RED + f"  │ {item.name} recharge enemy HP and MP for {item.prop}" + TextFormat.RESET_ALL)
            elif item.type == "poison":
                poison_on_player['on'] = True
                poison_on_player['dmg'] += item.prop
                poison_on_player['round'] = 3

            if enemy.items[0]['quantity'] == 0:
                enemy.items.pop(0)

            time.sleep(1)
        # ENEMY ATTACK WITH MAGIC
        elif random_attack == 3:
            spell = enemy.spell_list[random.randrange(0, len(enemy.spell_list))]
            magic_damage = spell.generate_damage()
            current_mp = enemy.get_mp()

            if spell.cost > current_mp:
                enemy_damage = enemy.generate_damage()
                player.take_damage(enemy_damage - player.df)
                print(TextFormat.RED + f"  │ The enemy attacked you for {enemy_damage - player.df}." + TextFormat.RESET_ALL)
                continue

            enemy.reduce_mp(spell.cost)
            
            if spell.type == "black":
                player.take_damage(magic_damage)
                print(TextFormat.RED + f"  │ {spell.name} take {magic_damage} HP from you." + TextFormat.RESET_ALL)
            elif spell.type == 'white':
                enemy.heal(magic_damage)
                print(TextFormat.BLUE + f"  │ {spell.name} heals {enemy.name} for: {magic_damage} HP." + TextFormat.RESET_ALL)
            elif spell.type == 'zombie':
                player.take_damage(magic_damage)
                enemy.heal(magic_damage)
                print(TextFormat.BLUE + f"  │ {spell.name} heals {enemy.name} and damages You for: {magic_damage} HP." + TextFormat.RESET_ALL)
            elif spell.type == "curse":
                curse_on_player["on"] = True
                curse_on_player["dmg"] = spell.dmg
                curse_on_player["round"] = 4
                time.sleep(1)

            time.sleep(1)
        # ENEMY SIMPLE ATTACK
        else:
            enemy_damage = enemy.generate_damage()
            player.take_damage(enemy_damage - player.df)
            print(TextFormat.RED + f"  │ The enemy attacked you for {enemy_damage - player.df}." + TextFormat.RESET_ALL)

        # DAMAGE OVER TIME ON PLAYER
        if poison_on_player['on']:
            poison_on_player['round'] -= 1
            percent = (player.maxhp * poison_on_player['dmg']) / 100
            player.take_damage(int(percent))
            print(TextFormat.RED + f'  │ Poison hits you for {percent} HP.' + TextFormat.RESET_ALL)
            if poison_on_player['round'] == 0:
                poison_on_player['on'] = False
            time.sleep(1)
        
        # CURSE OVER TIME ON PLAYER
        if curse_on_player["on"] and curse_on_player["round"] != 0:
            player.atk = int(player.atk // 1.2)
            for reduced_magic in player.spell_list:
                reduced_magic.dmg = int(reduced_magic.dmg // 1.2)
            for reduced_item in player.items:
                reduced_item["item"].prop = int(reduced_item["item"].prop // 1.2)
            curse_on_player["round"] -= 1
            print(TextFormat.RED + f"  │ {player.name}'s attributes and items are cursed." + TextFormat.RESET_ALL)
            time.sleep(1)
        if curse_on_player["round"] == 0:
            curse_on_player["on"] = False
            player.atk = player.maxatk
            for reduced_item in player.items:
                reduced_item["item"].prop = reduced_item["item"].maxprop
            for reduced_magic in player.spell_list:
                reduced_magic.dmg = reduced_magic.maxdmg

        time.sleep(2)


def player_recover(player):
    add_heal = int(player.maxhp / 2)
    player.heal(add_heal)
    print(TextFormat.BLUE + f'  │ +{add_heal} health added.' + TextFormat.RESET_ALL)
    time.sleep(1)
    add_manna = int((player.maxmp * 70) / 100)
    player.manna(add_manna)
    print(TextFormat.CYAN + f'  │ +{add_manna} magic points added.' + TextFormat.RESET_ALL)
    time.sleep(1)
    random_df = player.generate_df()
    player.df += random_df
    print(TextFormat.YELLOW + f'  │ 🛡 +{random_df} shield strength added.' + TextFormat.RESET_ALL)


def power_up_player(player):
    hp_up_percent = int((player.maxhp * 20) / 100)
    player.maxhp += hp_up_percent
    mp_up_percent = int((player.maxmp * 20) / 100)
    player.maxmp += mp_up_percent
    player.df += 8
    atk_up_percent = int((player.maxatk * 20) / 100)
    player.maxatk += atk_up_percent

    for power_spell in player.spell_list:
        power_spell.maxdmg += int((power_spell.maxdmg * 10) / 100)
        power_spell.dmg = power_spell.maxdmg

    player.hp = player.maxhp
    player.mp = player.maxmp
    player.atk = player.maxatk
    player.action = ["Attack " + str(player.maxatk), "Magic (overwrite shield)", "Use item"]


def enchanted_garden(board, player):
    # s = pygame.mixer.Sound("level.wav")
    # s.play(-1)
    print_method = 5

    bag = LevelItem('💰', 'bag', True, 11, 20)
    rock = LevelItem('🏔 ', 'rock', True, 11, 19)
    engine.put_player_on_board(board, player)

    level = True
    top = "Enchanted Garden"
    message = "Info"
    while level:
        util.clear_screen()
        main.print_level(board, message, player, print_method, top)
        key = util.key_pressed()
        top = "Enchanted Garden"
        # MAIN CONTROL
        if key == 'q':
            quit_game()
        elif key == "d":
            if player.pos_x == 5 and player.pos_y == 36 and not Enemies.goblin.on:
                return 1, player
            player.move_right(board)
            player.move_right(board, '▒▒')
            if board[player.pos_x][player.pos_y + 1] == '╦═':
                board[player.pos_x][player.pos_y] = '  '
                board[player.pos_x][player.pos_y + 3] = player.icon
                player.pos_y += 3
        elif key == "s":
            player.move_down(board)
            player.move_down(board, '▒▒')
        elif key == "w":
            player.move_up(board)
            player.move_up(board, '▒▒')
        elif key == "a":
            player.move_left(board)
            player.move_left(board, '▒▒')
            if board[player.pos_x][player.pos_y - 1] == '═╦':
                board[player.pos_x][player.pos_y] = '  '
                board[player.pos_x][player.pos_y - 3] = player.icon
                player.pos_y -= 3
        elif key == "t":
            tool_msg = "   (0): back (T)ools: "
            for tool in player.tools:
                tool_msg += tool.name + ' '
            t_pressed = True
            while t_pressed:
                util.clear_screen()
                main.print_level(board, message, player, print_method, tool_msg)
                key = util.key_pressed()
                if key == '0':
                    t_pressed = False
                elif key == 't':
                    teleport = True
                    for index, tool in enumerate(player.tools):
                        if tool.name == '⛏ Pick':
                            if rock.is_close(board, player) and rock.on:
                                rock.turn_off(board)
                                player.tools.pop(index)
                                t_pressed = False
                                teleport = False
                                break
                    for index, tool in enumerate(player.tools):
                        if tool.name == '🖲 teleport' and teleport:
                            return 1, player
                else:
                    continue
        elif key == "i":
            main.print_character(player, " character")
        elif key == "c":
            player = cheat_mode(player)

        # OTHER CONTROLS
        elif key == 'f':
            # COCODILLO I
            if Enemies.crocodile.is_close(board, player) and Enemies.crocodile.on:
                win = battle(player, Enemies.crocodile)
                if win == 1:
                    Enemies.crocodile.turn_off(board)
                    winnable_items = [Collectables.food, Collectables.elixir]

                    how_much_items = random.randrange(1, 3)
                    for rounds in range(how_much_items):
                        random_item = random.choice(winnable_items)
                        random_quantity = random.randrange(2, 5)
                        player.get_item(random_item, random_quantity)
                        print(f'  │ You got a new item:  {random_item.name} x{random_quantity}')
                        time.sleep(1)

                    player_recover(player)

                    print('  │')
                    input('  │ Press ENTER to continue...')
                else:
                    return 0, player
            # COCODILLO II
            elif Enemies.crocodile2.is_close(board, player) and Enemies.crocodile2.on:
                win = battle(player, Enemies.crocodile2)
                if win == 1:
                    Enemies.crocodile2.turn_off(board)

                    winnable_items = [Collectables.food, Collectables.elixir]
                    how_much_items = random.randrange(1, 3)
                    for rounds in range(how_much_items):
                        random_item = random.choice(winnable_items)
                        random_quantity = random.randrange(2, 5)
                        player.get_item(random_item, random_quantity)
                        print(f'  │ You got a new item:  {random_item.name} x{random_quantity}')
                        time.sleep(1)

                    player_recover(player)

                    print('  │')
                    input('  │ Press ENTER to continue...')
                else:
                    return 0, player
            # THE TUSKER
            elif Enemies.pig.is_close(board, player) and Enemies.pig.on:
                win = battle(player, Enemies.pig)
                if win == 1:
                    Enemies.pig.turn_off(board)

                    player.get_item(Collectables.pick, 1)
                    print(TextFormat.Bold + "  │ You have got a ⛏ pick tool" + TextFormat.RESET_ALL)
                    time.sleep(1)

                    player_recover(player)

                    print('  │')
                    input('  │ Press ENTER to continue...')
                else:
                    return 0, player
            # GOBLIN
            elif Enemies.goblin.is_close(board, player) and Enemies.goblin.on:
                win = battle(player, Enemies.goblin)
                if win == 1:
                    Enemies.goblin.turn_off(board)

                    winnable_items = [Collectables.food, Collectables.elixir, Collectables.bow, Collectables.mushroom]
                    how_much_items = random.randrange(1, 4)
                    for rounds in range(how_much_items):
                        random_item = random.choice(winnable_items)
                        random_quantity = random.randrange(1, 3)
                        player.get_item(random_item, random_quantity)
                        print(f'  │ You got a new item:  {random_item.name} x{random_quantity}')
                        time.sleep(1)

                    player.get_item(Collectables.knife, 1)
                    print(f'  │ You got a new item:  {Collectables.knife.name} x1')
                    time.sleep(1)

                    player_recover(player)

                    print('  │')
                    input('  │ Press ENTER to continue...')
                else:
                    return 0, player
            # BAG
            elif bag.is_close(board, player) and bag.on:
                bag.turn_off(board)

                player.get_item(Collectables.magic_drink_1, 1)
                player.get_item(Collectables.sword, 1)
                player.get_item(Collectables.mega_elixir, 2)
                main.print_message(["You got:", "", f"1x {Collectables.magic_drink_1.name}",
                                   f"1x {Collectables.sword.name}"])
            # MESSAGE
            elif player.pos_x == 2 and player.pos_y == 5 or player.pos_x == 3 and player.pos_y == 6:
                main.print_message(["We present you the Enchanted Garden-et!", "", f"Head to the forest brave {player.name}.",
                                    "Looking for some treasures?", "'The Tusker' can help you!"])

        # POSITION CHECKER
        if player.pos_x == 2 and player.pos_y == 5 or player.pos_x == 3 and player.pos_y == 6:
            message = "Letter"
        elif Enemies.crocodile.is_close(board, player) and Enemies.crocodile.on:
            message = f'{Enemies.crocodile.icon} {Enemies.crocodile.name} press F to fight!'
        elif Enemies.crocodile2.is_close(board, player) and Enemies.crocodile2.on:
            message = f'{Enemies.crocodile2.icon} {Enemies.crocodile2.name} press F to fight!'
        elif Enemies.pig.is_close(board, player) and Enemies.pig.on:
            message = f'{Enemies.pig.icon} {Enemies.pig.name} press F to fight!'
        elif Enemies.goblin.is_close(board, player) and Enemies.goblin.on:
            message = '👹∿ Ha-ha! You can not beat me!!! Press F to face it anyway...'
        else:
            message = 'Info'


def wild_wilds(board, player):
    print_method = 6

    engine.put_player_on_board(board, player)
    power_up = LevelItem('🕋', 'Power Up', False, 6, 5)

    level = True
    message = "Info"
    top = "Wild Wilds"
    while level:
        if not Enemies.goblin1.on and not Enemies.goblin2.on and not Enemies.goblin3.on and power_up.name == 'Power Up':
            power_up.turn_on(board)

        util.clear_screen()
        main.print_level(board, message, player, print_method, top)
        key = util.key_pressed()

        # MAIN CONTROL
        if key == 'q':
            quit_game()
        elif key == "d":
            player.move_right(board)
            player.move_right(board, '▒▒')
            if board[player.pos_x][player.pos_y + 1] == '╦═':
                board[player.pos_x][player.pos_y] = '  '
                board[player.pos_x][player.pos_y + 4] = player.icon
                player.pos_y += 4
        elif key == "s":
            player.move_down(board)
            player.move_down(board, '▒▒')
        elif key == "w":
            player.move_up(board)
            player.move_up(board, '▒▒')
        elif key == "a":
            player.move_left(board)
            player.move_left(board, '▒▒')
            if board[player.pos_x][player.pos_y - 1] == '═╦':
                board[player.pos_x][player.pos_y] = '  '
                board[player.pos_x][player.pos_y - 4] = player.icon
                player.pos_y -= 4
        elif key == "t":
            if Enemies.peasant.is_close(board, player) and Enemies.peasant.on and not Collectables.boots.on:
                main.print_message([f"Hey-a {player.name}", "This goblin...Jose...stol-a-me boots.", "Me-a never let anyone-a go-tru...🖕🏻", "...gimme back my boots-a, and me-a let you-tru."])
                continue
            elif Enemies.peasant.is_close(board, player) and Enemies.peasant.on and Collectables.boots.on:
                main.print_message([f"Wooooow {player.name}", "You got-a me-a..its my sisters-a boots.", "I let you in-a now-a tru.", "Byeeeeeee"])
                Enemies.peasant.turn_off(board)
                for index, tool in enumerate(player.tools):
                    if tool.name == '👢 Boots-a':
                        player.tools.pop(index)
                continue

            tool_msg = "   (0): back (T)ools: "
            for tool in player.tools:
                tool_msg += tool.name + ' '
            t_pressed = True
            while t_pressed:
                util.clear_screen()
                main.print_level(board, message, player, print_method, tool_msg)
                t_key = util.key_pressed()
                if t_key == '0':
                    t_pressed = False
                elif t_key == 't':
                    for index, tool in enumerate(player.tools):
                        if tool.name == '🖲 teleport':
                            return 1, player
                else:
                    continue
        elif key == "i":
            main.print_character(player, " character")
        elif key == "c":
            player = cheat_mode(player)

        # OTHER CONTROLS
        elif key == 'f':
            # PEASANT
            if Enemies.peasant.is_close(board, player) and Enemies.peasant.on:
                win = battle(player, Enemies.peasant)
                if win == 1:
                    Enemies.peasant.turn_off(board)

                    winnable_items = [Collectables.potion, Collectables.elixir, Collectables.hi_potion, Collectables.magic_drink_2, Collectables.mega_elixir]
                    how_much_items = random.randrange(2, 4)
                    for rounds in range(how_much_items):
                        random_item = random.choice(winnable_items)
                        random_quantity = random.randrange(1, 3)
                        player.get_item(random_item, random_quantity)
                        print(f'  │ You got a new item:  {random_item.name} x{random_quantity}')
                        time.sleep(1)

                    player_recover(player)

                    print('  │')
                    input('  │ Press ENTER to continue...')
                else:
                    return 0, player
            # JOE
            elif Enemies.goblin1.is_close(board, player) and Enemies.goblin1.on:
                win = battle(player, Enemies.goblin1)
                if win == 1:
                    Enemies.goblin1.turn_off(board)

                    winnable_items = [Collectables.food, Collectables.elixir, Collectables.bow, Collectables.knife]
                    how_much_items = random.randrange(1, 4)
                    for rounds in range(how_much_items):
                        random_item = random.choice(winnable_items)
                        random_quantity = random.randrange(1, 3)
                        player.get_item(random_item, random_quantity)
                        print(f'  │ You got a new item:  {random_item.name} x{random_quantity}')
                        time.sleep(1)

                    player_recover(player)

                    print('  │')
                    input('  │ Press ENTER to continue...')
                else:
                    return 0, player
            # JOEY
            elif Enemies.goblin2.is_close(board, player) and Enemies.goblin2.on:
                win = battle(player, Enemies.goblin2)
                if win == 1:
                    Enemies.goblin2.turn_off(board)

                    winnable_items = [Collectables.food, Collectables.elixir, Collectables.bow, Collectables.knife]
                    how_much_items = random.randrange(1, 4)
                    for rounds in range(how_much_items):
                        random_item = random.choice(winnable_items)
                        random_quantity = random.randrange(1, 3)
                        player.get_item(random_item, random_quantity)
                        print(f'  │ You got a new item:  {random_item.name} x{random_quantity}')
                        time.sleep(1)

                    player_recover(player)

                    print('  │')
                    input('  │ Press ENTER to continue...')
                else:
                    return 0, player
            # JOSE
            elif Enemies.goblin3.is_close(board, player) and Enemies.goblin3.on:
                win = battle(player, Enemies.goblin3)
                if win == 1:
                    Enemies.goblin3.turn_off(board)
                    Collectables.boots.on = True
                    winnable_items = [Collectables.food, Collectables.elixir, Collectables.bow, Collectables.knife]
                    how_much_items = random.randrange(1, 4)
                    for rounds in range(how_much_items):
                        random_item = random.choice(winnable_items)
                        random_quantity = random.randrange(1, 3)
                        player.get_item(random_item, random_quantity)
                        print(f'  │ You got a new item:  {random_item.name} x{random_quantity}')
                        time.sleep(1)

                    player.get_item(Collectables.boots, 1)
                    print(TextFormat.Bold + "  │ You have got the 👢 Boots-a" + TextFormat.RESET_ALL)
                    time.sleep(1)
                    boot_on = 1

                    player_recover(player)

                    print('  │')
                    input('  │ Press ENTER to continue...')
                else:
                    return 0, player
            # MUSTACHE
            elif Enemies.mustache.is_close(board, player) and Enemies.mustache.on:
                win = battle(player, Enemies.mustache)
                if win == 1:
                    Enemies.mustache.turn_off(board)

                    player.get_item(Collectables.wolf, 2)
                    print("  │ You have got a 🐺 Wolf-bite ")
                    time.sleep(1)

                    player_recover(player)

                    print('  │')
                    input('  │ Press ENTER to continue...')
                else:
                    return 0, player
            # GUARDS
            elif player.pos_x == 16 and player.pos_y == 27 and Enemies.guard1.on or player.pos_x == 16 and player.pos_y == 28 and Enemies.guard1.on:
                win = battle(player, Enemies.guard1)
                if win == 1:
                    winnable_items = [Collectables.hi_potion, Collectables.mega_elixir, Collectables.sword]
                    how_much_items = random.randrange(2, 4)
                    for rounds in range(how_much_items):
                        random_item = random.choice(winnable_items)
                        random_quantity = random.randrange(1, 4)
                        player.get_item(random_item, random_quantity)
                        print(f'  │ You got a new item:  {random_item.name} x{random_quantity}')
                        time.sleep(1)

                    player.get_item(Collectables.double_sword, 1)
                    print(f'  │ You got a new item: ⚔️ Double Sword')

                    player_recover(player)

                    input('  │ Press ENTER to continue fighting with the other guard!')
                    win = battle(player, Enemies.guard2)
                    if win == 1:
                        Enemies.guard1.turn_off(board)
                        Enemies.guard2.turn_off(board)

                        winnable_items = [Collectables.hi_potion, Collectables.mega_elixir, Collectables.sword, Collectables.bow]
                        how_much_items = random.randrange(2, 4)
                        for rounds in range(how_much_items):
                            random_item = random.choice(winnable_items)
                            random_quantity = random.randrange(1, 3)
                            player.get_item(random_item, random_quantity)
                            print(f'  │ You got a new item:  {random_item.name} x{random_quantity}')
                            time.sleep(1)

                        player.get_item(Collectables.sword, 1)
                        player.get_item(Collectables.magic_drink_3, 2)
                        player.get_item(Collectables.vaccine, 2)
                        print("  │ You have got 🍺 Walter's Beer ")
                        time.sleep(1)
                        print("  │ You have got 💉 Vaccine")
                        time.sleep(1)
                        print("  │ You have got 🗡 Sword")
                        time.sleep(1)

                        player_recover(player)

                        print('  │')
                        input('  │ Press ENTER to continue...')
                    else:
                        return 0, player
                else:
                    return 0, player

            # POWER UP
            elif power_up.is_close(board, player) and power_up.on:
                power_up.turn_off(board)
                power_up.name = 'Power Down'

                power_up_player(player)

                player.get_item(Collectables.knife, 3)
                player.get_item(Collectables.mushroom, 2)
                player.spell_list.append(Spells.thunder)
                main.print_message(["You found a mystical power up!", '', "Your Maximum Health Points,", "Magic Points, Defence and Attack", "has been increased!", '', 'You got also knifes and Toxic Mushrooms.', '', 'Magic Unlocked: Thunder'])

            # THE LETTER
            elif player.pos_x == 4 and player.pos_y == 4:
                main.print_message(['You have reached Wild Wilds, the woody and windy woods...', '', 'So you get closer to the Towers, just watch out,', "two guards waits for you, that's", 'perfectly the double of one!!',
                                    "The Thunder King with his last magic energy", "spread out mystical boxes.", "These are hidden, but with some tricks you can unlock them.", "Good luck on your way, mind the goblins! :)"])
            elif player.pos_x == 17 and player.pos_y == 28 and not Enemies.guard1.on:
                return 1, player

        # POSITION CHECKER
        if Enemies.peasant.is_close(board, player) and Enemies.peasant.on:
            message = "Press T to talk or F to fight"
        elif Enemies.goblin1.is_close(board, player) and Enemies.goblin1.on:
            message = f"{Enemies.goblin1.icon} {Enemies.goblin1.name} , press F to fight."
        elif Enemies.goblin2.is_close(board, player) and Enemies.goblin2.on:
            message = f"{Enemies.goblin2.icon} {Enemies.goblin2.name} , press F to fight."
        elif Enemies.goblin3.is_close(board, player) and Enemies.goblin3.on:
            message = f"{Enemies.goblin3.icon} {Enemies.goblin3.name}∿ Te no puedes tener mi nueva Boots-a. Press F to fight."
        elif Enemies.mustache.is_close(board, player) and Enemies.mustache.on:
            message = f"{Enemies.mustache.icon} {Enemies.mustache.name}∿ Prepare yourself for some wolf bite ha-ha!, Press F to fight"
        elif player.pos_x == 16 and player.pos_y == 27 and Enemies.guard1.on or player.pos_x == 16 and player.pos_y == 28 and Enemies.guard1.on:
            message = f"{Enemies.guard1.icon}∿ No trespass! Press F to trespass."
        elif power_up.is_close(board, player) and power_up.name == "Power Up":
            message = "Press F to power up!!!"
        elif player.pos_x == 17 and player.pos_y == 28 and not Enemies.guard1.on:
            message = "Press F to enter the Demon Towers!!!"
        elif player.pos_x == 4 and player.pos_y == 4:
            message = "Press F to read the letter!"
        else:
            message = 'Info'


def castle_main_hall(board, player):
    print_method = 7

    scientist = LevelItem('👨🏼‍🔬', 'Scientist', True, 14, 1)
    wall = LevelItem(" ░", "wall", True, 14, 5)
    door1 = LevelItem("🚪", "basement door", True, 5, 14)
    door2 = LevelItem("🚪", "tower door", True, 8, 34)
    power_up = LevelItem('🕋', 'Power Up', True, 2, 35)

    util.clear_screen()
    engine.put_player_on_board(board, player)
    level = True
    top = "The Daemon Towers - Main Hall"
    message = "Info"
    while level:
        util.clear_screen()
        main.print_level(board, message, player, print_method, top)
        key = util.key_pressed()

        # MAIN CONTROL
        if key == 'q':
            quit_game()
        elif key == "d":
            player.move_right(board)
        elif key == "s":
            player.move_down(board)
        elif key == "w":
            player.move_up(board)
        elif key == "a":
            player.move_left(board)
        elif key == "t" and scientist.is_close(board, player) and scientist.on:
            main.print_message([f"Ahh {player.name}!!", "", "Have mercy on me! I'm just a Scientist...", "You have to go to the basement first i got the key for it!", "There you can get the tower key!"])
            continue
        elif key == "t":
            tool_msg = "   (0): back (T)ools: "
            for tool in player.tools:
                tool_msg += tool.name + ' '
            t_pressed = True
            while t_pressed:
                util.clear_screen()
                main.print_level(board, message, player, print_method, tool_msg)
                key = util.key_pressed()
                if key == '0':
                    t_pressed = False
                elif key == 't':
                    teleport = True
                    for index, tool in enumerate(player.tools):
                        if tool.name == '⛏ Pick':
                            if wall.is_close(board, player) and wall.on:
                                wall.turn_off(board)
                                t_pressed = False
                                continue
                            else:
                                t_pressed = False
                        elif tool.name == '🗝 Key':
                            if door1.is_close(board, player) and door1.on:
                                player.tools.pop(index)
                                return 1, player
                            else:
                                t_pressed = False
                    for index, tool in enumerate(player.tools):
                        if tool.name == '🖲 teleport' and teleport:
                            return 1, player
                else:
                    continue
        elif key == "i":
            main.print_character(player, " character")
        elif key == "c":
            player = cheat_mode(player)

        # OTHER CONTROLS / FIGHTS
        elif key == 'f':
            # GUARD1
            if Enemies.guard1_1.is_close(board, player) and Enemies.guard1_1.on:
                win = battle(player, Enemies.guard1_1)
                if win == 1:
                    Enemies.guard1_1.turn_off(board)

                    winnable_items = [Collectables.hi_potion, Collectables.mega_elixir, Collectables.sword, Collectables.bow]
                    how_much_items = random.randrange(2, 5)
                    for rounds in range(how_much_items):
                        random_item = random.choice(winnable_items)
                        random_quantity = random.randrange(2, 4)
                        player.get_item(random_item, random_quantity)
                        print(f'  │ You got a new item:  {random_item.name} x{random_quantity}')
                        time.sleep(1)

                    player.get_item(Collectables.magic_drink_4, 1)
                    print("  │ You have got 🥃 Whiskey on the rocks ")
                    time.sleep(1)

                    player_recover(player)

                    print('  │')
                    input('  │ Press ENTER to continue...')
                else:
                    return 0, player
            # GUARD2
            elif Enemies.guard2_1.is_close(board, player) and Enemies.guard2_1.on:
                win = battle(player, Enemies.guard2_1)
                if win == 1:
                    Enemies.guard2_1.turn_off(board)

                    winnable_items = [Collectables.hi_potion, Collectables.mega_elixir, Collectables.sword, Collectables.bow, Collectables.double_sword]
                    how_much_items = random.randrange(2, 5)
                    for rounds in range(how_much_items):
                        random_item = random.choice(winnable_items)
                        random_quantity = random.randrange(2, 3)
                        player.get_item(random_item, random_quantity)
                        print(f'  │ You got a new item:  {random_item.name} x{random_quantity}')
                        time.sleep(1)

                    player.get_item(Collectables.magic_drink_5, 1)
                    print("  │ You have got 🍹 Long Island")
                    time.sleep(1)

                    player_recover(player)

                    print('  │')
                    input('  │ Press ENTER to continue...')
                else:
                    return 0, player
            # GUARD3 ELITE
            elif Enemies.guard3.is_close(board, player) and Enemies.guard3.on:
                win = battle(player, Enemies.guard3)
                if win == 1:
                    Enemies.guard3.turn_off(board)

                    winnable_items = [Collectables.super_elixir, Collectables.sword,
                                      Collectables.bow, Collectables.double_sword, Collectables.grenade]
                    how_much_items = random.randrange(2, 5)
                    for rounds in range(how_much_items):
                        random_item = random.choice(winnable_items)
                        random_quantity = random.randrange(2, 4)
                        player.get_item(random_item, random_quantity)
                        print(f'  │ You got a new item:  {random_item.name} x{random_quantity}')
                        time.sleep(1)

                    player.get_item(Collectables.bow, 5)
                    print("  │ You have got 🏹 Bow x5")
                    time.sleep(1)

                    player_recover(player)

                    print('  │')
                    input('  │ Press ENTER to continue...')
                else:
                    return 0, player
            # GUARD4
            elif Enemies.guard4.is_close(board, player) and Enemies.guard4.on:
                win = battle(player, Enemies.guard4)
                if win == 1:
                    Enemies.guard4.turn_off(board)

                    winnable_items = [Collectables.magic_drink_3, Collectables.super_elixir,
                                      Collectables.sword, Collectables.bow]
                    how_much_items = random.randrange(2, 5)
                    for rounds in range(how_much_items):
                        random_item = random.choice(winnable_items)
                        random_quantity = random.randrange(2, 4)
                        player.get_item(random_item, random_quantity)
                        print(f'  │ You got a new item:  {random_item.name} x{random_quantity}')
                        time.sleep(1)

                    player_recover(player)

                    random_df = player.generate_df()
                    player.df += random_df
                    print(TextFormat.YELLOW + f'  │ 🛡 +{random_df} shield strength added.' + TextFormat.RESET_ALL)
                    print('  │')
                    input('  │ Press ENTER to continue...')
                else:
                    return 0, player
            # GUARD5
            elif Enemies.guard5.is_close(board, player) and Enemies.guard5.on:
                win = battle(player, Enemies.guard5)
                if win == 1:
                    Enemies.guard5.turn_off(board)

                    winnable_items = [Collectables.magic_drink_3,
                                      Collectables.super_elixir, Collectables.sword,
                                      Collectables.bow]
                    how_much_items = random.randrange(3, 4)
                    for rounds in range(how_much_items):
                        random_item = random.choice(winnable_items)
                        random_quantity = random.randrange(2, 4)
                        player.get_item(random_item, random_quantity)
                        print(f'  │ You got a new item:  {random_item.name} x{random_quantity}')
                        time.sleep(1)

                    player_recover(player)

                    print('  │')
                    input('  │ Press ENTER to continue...')
                else:
                    return 0, player
            # GUARD6
            elif Enemies.guard6.is_close(board, player) and Enemies.guard6.on:
                win = battle(player, Enemies.guard6)
                if win == 1:
                    Enemies.guard6.turn_off(board)

                    winnable_items = [Collectables.magic_drink_3,
                                      Collectables.super_elixir, Collectables.sword,
                                      Collectables.bow]
                    how_much_items = random.randrange(2, 4)
                    for rounds in range(how_much_items):
                        random_item = random.choice(winnable_items)
                        random_quantity = random.randrange(2, 4)
                        player.get_item(random_item, random_quantity)
                        print(f'  │ You got a new item:  {random_item.name} x{random_quantity}')
                        time.sleep(1)

                    player_recover(player)

                    print('  │')
                    input('  │ Press ENTER to continue...')
                else:
                    return 0, player
            # THIEF
            elif Enemies.thief.is_close(board, player) and Enemies.thief.on:
                win = battle(player, Enemies.thief)
                if win == 1:
                    Enemies.thief.turn_off(board)

                    winnable_items = [Collectables.magic_drink_5,
                                      Collectables.super_elixir, Collectables.knife,
                                      Collectables.bow, Collectables.spider,
                                      Collectables.vaccine, Collectables.bomb]
                    how_much_items = random.randrange(2, 6)
                    for rounds in range(how_much_items):
                        random_item = random.choice(winnable_items)
                        random_quantity = random.randrange(1, 3)
                        player.get_item(random_item, random_quantity)
                        print(f'  │ You got a new item:  {random_item.name} x{random_quantity}')
                        time.sleep(1)

                    player.get_item(Collectables.magic_drink_5, 1)
                    print("  │ You have got 🍹 Long Island")
                    time.sleep(1)
                    player.get_item(Collectables.deadly_poison, 1)
                    print("  │ You have got 💀 Deadly poison")
                    time.sleep(1)
                    player.get_item(Collectables.pick, 1)
                    print(TextFormat.Bold + "  │ You have got a ⛏ pick tool" + TextFormat.RESET_ALL)
                    time.sleep(1)

                    player_recover(player)

                    print('  │')
                    input('  │ Press ENTER to continue...')
                else:
                    return 0, player
            # VAMPIRE
            elif Enemies.vampire.is_close(board, player) and Enemies.vampire.on:
                win = battle(player, Enemies.vampire)
                if win == 1:
                    Enemies.vampire.turn_off(board)

                    winnable_items = [Collectables.magic_drink_3,
                                      Collectables.super_elixir,
                                      Collectables.spider,
                                      Collectables.vaccine]
                    how_much_items = random.randrange(2, 4)
                    for rounds in range(how_much_items):
                        random_item = random.choice(winnable_items)
                        random_quantity = random.randrange(1, 3)
                        player.get_item(random_item, random_quantity)
                        print(f'  │ You got a new item:  {random_item.name} x{random_quantity}')
                        time.sleep(1)

                    player.get_item(Collectables.magic_drink_6, 2)
                    print("  │ You have got 🥤 Bloody Mary")
                    time.sleep(1)
                    player.get_item(Collectables.magic_drink_3, 1)
                    print("  │ You have got 🍺 Walter's beer")
                    time.sleep(1)

                    player_recover(player)

                    print('  │')
                    input('  │ Press ENTER to continue...')
                else:
                    return 0, player
            # SCIENTOLOGIST
            elif scientist.is_close(board, player) and scientist.on:
                scientist.turn_off(board)
                player.get_item(Collectables.old_key, 1)
            # POWER UP
            elif power_up.is_close(board, player) and power_up.on:
                power_up.turn_off(board)

                power_up_player(player)

                player.get_item(Collectables.knife, 6)
                player.get_item(Collectables.spider, 1)
                player.spell_list.append(Spells.curse_of_weakness)

                main.print_message(["You found a mystical power up!", '', "Your Maximum Health Points,", "Magic Points, Defence and Attack", "has been increased!", '', 'You got also lots of knifes and 🕷 Spiders.', '', 'Magic Unlocked: Curse of Weakness'])
            # THE LETTER
            elif player.pos_x == 12 and player.pos_y == 2:
                main.print_message(['You did it! You are inside...', '...but can you defeat that blood sucker? :O', "The Demon Towers guards are corrupted too, be careful,", "but first visit hte other intruder."])

        # POSITION CHECKER
        if Enemies.guard1_1.is_close(board, player) and Enemies.guard1_1.on:
            message = f"{Enemies.guard1_1.icon} No trespass! Press F to trespass."
        elif Enemies.guard2_1.is_close(board, player) and Enemies.guard2_1.on:
            message = f"{Enemies.guard2_1.icon} No trespass! Press F to trespass."
        elif Enemies.guard3.is_close(board, player) and Enemies.guard3.on:
            message = f"{Enemies.guard3.icon} Ahh! The intruder! You won't survive this (F)ight!"
        elif Enemies.guard4.is_close(board, player) and Enemies.guard4.on:
            message = f"{Enemies.guard4.icon} No trespass! Press F to trespass."
        elif Enemies.guard5.is_close(board, player) and Enemies.guard5.on:
            message = f"{Enemies.guard5.icon} No trespass! Press F to trespass."
        elif Enemies.guard6.is_close(board, player) and Enemies.guard6.on:
            message = f"{Enemies.guard6.icon} No trespass! Press F to trespass."
        elif Enemies.thief.is_close(board, player) and Enemies.thief.on:
            message = f"{Enemies.thief.icon} You come for my treasure? Prepare to die! Press F."
        elif Enemies.vampire.is_close(board, player) and Enemies.vampire.on:
            message = f"{Enemies.vampire.icon} I will suck your blood out ha-ha-ha!"
        elif door1.is_close(board, player) and door1.on:
            message = "🚪 Basement door is locked!"
        elif door2.is_close(board, player) and door2.on:
            message = "🚪 Tower door is locked!"
        elif scientist.is_close(board, player) and scientist.on:
            message = "Press (T)alk or (F)ight...(talk before)"
        elif scientist.is_close(board, player) and not scientist.on:
            message = "You got the 🗝 Basement Key"
        elif player.pos_x == 12 and player.pos_y == 2:
            message = "F to read the letter!"
        else:
            message = "Info"


def castle_basement(board, player):
    lit_range = 4
    print_method = 4

    engine.put_player_on_board(board, player)
    light1 = LevelItem('🕯 ', 'light', True, 2, 2)
    light2 = LevelItem('🕯 ', 'light', True, 2, 28)
    light3 = LevelItem('🕯 ', 'light', True, 10, 26)
    power_up = LevelItem('🕋', 'power_up', True, 15, 35)
    cd_tool = LevelItem('💿', 'cd_tool', True, 15, 3)

    level = True
    top = "Castle Basement"
    message = "Info"
    while level:
        util.clear_screen()
        main.print_level(board, message, player, print_method, top, lit_range)
        key = util.key_pressed()

        # MAIN CONTROL
        if key == 'q':
            quit_game()
        elif key == "d":
            player.move_right(board)
        elif key == "s":
            # TELEPORT 2
            if player.pos_x == 14 and player.pos_y == 29:
                board[player.pos_x][player.pos_y] = '  '
                board[12][32] = player.icon
                player.pos_x = 12
                player.pos_y = 32
            else:
                player.move_down(board)
        elif key == "w":
            # TELEPORT 1
            if player.pos_x == 3 and player.pos_y == 8:
                board[player.pos_x][player.pos_y] = '  '
                board[3][35] = player.icon
                player.pos_y = 35
            # TELEPORT 1
            elif player.pos_x == 3 and player.pos_y == 35:
                board[player.pos_x][player.pos_y] = '  '
                board[3][8] = player.icon
                player.pos_y = 8
            # TELEPORT 2
            elif player.pos_x == 12 and player.pos_y == 32:
                board[player.pos_x][player.pos_y] = '  '
                board[14][29] = player.icon
                player.pos_x = 14
                player.pos_y = 29
            elif player.pos_x == 2 and player.pos_y == 17:
                return 1, player
            else:
                player.move_up(board)
        elif key == "a":
            player.move_left(board)
        elif key == "t":
            tool_msg = "   (0): back (T)ools: "
            for tool in player.tools:
                tool_msg += tool.name + ' '
            t_pressed = True
            while t_pressed:
                util.clear_screen()
                main.print_level(board, message, player, print_method, tool_msg, lit_range)
                key = util.key_pressed()
                if key == '0':
                    t_pressed = False
                elif key == 't':
                    teleport = True
                    for index, tool in enumerate(player.tools):
                        if tool.name == "💾 floppy":
                            if player.pos_x == 11 and player.pos_y == 29:
                                board[12][29] = '  '
                                player.tools.pop(index)
                                t_pressed = False
                                teleport = False
                                break
                        elif tool.name == '👢 Boots-a':
                            if player.pos_x == 13 and player.pos_y == 3:
                                Enemies.MadBot.turn_off(board)
                                board[1][17] = '  '
                                player.tools.pop(index)
                                t_pressed = False
                                main.print_message([f'OH MY MAKER!! {player.name}!', '', 'You have @ __real__ italian boots??', 'I always wants___that.', 'Now I can dance like _a_ real man!', 'Here t@ke this 🗝 Tower key.'])
                                player.get_item(Collectables.old_key, 1)
                                teleport = False
                                break
                    for index, tool in enumerate(player.tools):
                        if tool.name == '🖲 teleport' and teleport:
                            return 1, player
                else:
                    continue
        elif key == "i":
            main.print_character(player, " character")
        elif key == "c":
            player = cheat_mode(player)

        # OTHER CONTROLS
        elif key == "f":
            # VIRUS 1
            if Enemies.virus1.is_close(board, player) and Enemies.virus1.on:
                win = battle(player, Enemies.virus1)
                if win == 1:
                    Enemies.virus1.turn_off(board)

                    winnable_items = [Collectables.gear, Collectables.super_elixir, Collectables.magic_drink_5]
                    how_much_items = random.randrange(2, 4)
                    for rounds in range(how_much_items):
                        random_item = random.choice(winnable_items)
                        random_quantity = random.randrange(1, 5)
                        player.get_item(random_item, random_quantity)
                        print(f'  │ You got a new item:  {random_item.name} x{random_quantity}')
                        time.sleep(1)

                    player_recover(player)

                    print('  │')
                    input('  │ Press ENTER to continue...')
                else:
                    return 0, player
            # VIRUS 2
            elif Enemies.virus2.is_close(board, player) and Enemies.virus2.on:
                win = battle(player, Enemies.virus2)
                if win == 1:
                    Enemies.virus2.turn_off(board)

                    winnable_items = [Collectables.gear, Collectables.super_elixir, Collectables.magic_drink_6]
                    how_much_items = random.randrange(2, 4)
                    for rounds in range(how_much_items):
                        random_item = random.choice(winnable_items)
                        random_quantity = random.randrange(1, 5)
                        player.get_item(random_item, random_quantity)
                        print(f'  │ You got a new item:  {random_item.name} x{random_quantity}')
                        time.sleep(1)

                    player_recover(player)

                    print('  │')
                    input('  │ Press ENTER to continue...')
                else:
                    return 0, player
            # ALIEN
            elif Enemies.alien.is_close(board, player) and Enemies.alien.on:
                win = battle(player, Enemies.alien)
                if win == 1:
                    Enemies.alien.turn_off(board)

                    player.get_item(Collectables.deadly_poison, 1)
                    print("  │ You have got the 💀 Deadly poison")
                    time.sleep(1)

                    player_recover(player)

                    print('  │')
                    input('  │ Press ENTER to continue...')
                else:
                    return 0, player
            # MAD_BOT
            elif Enemies.MadBot.is_close(board, player) and Enemies.MadBot.on:
                win = battle(player, Enemies.MadBot)
                if win == 1:
                    Enemies.MadBot.turn_off(board)

                    board[1][17] = '  '
                    winnable_items = [Collectables.gear, Collectables.CD]
                    how_much_items = random.randrange(2, 4)
                    for rounds in range(how_much_items):
                        random_item = random.choice(winnable_items)
                        random_quantity = random.randrange(3, 5)
                        player.get_item(random_item, random_quantity)
                        print(f'  │ You got a new item:  {random_item.name} x{random_quantity}')
                        time.sleep(1)

                    player.get_item(Collectables.old_key, 1)
                    print(TextFormat.Bold + "  │ You have got the 🗝 Tower Key" + TextFormat.RESET_ALL)
                    time.sleep(1)

                    player_recover(player)

                    print('  │')
                    input('  │ Press ENTER to continue...')
                else:
                    return 0, player
            # CD TOOL
            elif player.pos_x == 14 and player.pos_y == 3 and cd_tool.on:
                player.get_item(Collectables.CD_tool, 1)
                cd_tool.turn_off(board)
            # CANDLE 1
            elif light1.is_close(board, player) and light1.on:
                light1.turn_off(board)
                lit_range += 2
            # CANDLE 2
            elif light2.is_close(board, player) and light2.on:
                light2.turn_off(board)
                lit_range += 2
            # CANDLE 3
            elif light3.is_close(board, player) and light3.on:
                light3.turn_off(board)
                lit_range += 2
            # POWER UP
            elif power_up.is_close(board, player) and power_up.on:
                power_up.turn_off(board)

                power_up_player(player)

                player.get_item(Collectables.double_sword, 2)
                player.spell_list.append(Spells.electricity)
                main.print_message(["You found a mystical power up!", '', "Your Maximum Health Points,", "Magic Points, Defence and Attack", "has been increased!", "You have got double sword x2",
                                    "Magic unlocked: Electricity"])

            # THE LETTER
            elif player.pos_x == 4 and player.pos_y == 17:
                main.print_message(['Crazy dark here in the basement.', 'Can you get some extra light please?', '', 'Maybe you do not need violence with that Robot!', 'Oh...and look in the back of that boss!'])

        # POSITION CHECKER
        if Enemies.virus1.is_close(board, player) and Enemies.virus1.on:
            message = "👾 -- just a virus...press F to run antivirus."
        elif Enemies.virus2.is_close(board, player) and Enemies.virus2.on:
            message = "👾 -- just a virus...press F to run antivirus."
        elif Enemies.alien.is_close(board, player) and Enemies.alien.on:
            message = "👽 Press F to hit this creepy alien."
        elif Enemies.MadBot.is_close(board, player) and Enemies.MadBot.on:
            message = "🤖 ∿ I AM A MAD TEST ROBOT... BEEP BEEP. And I h@ve the __tower key__"
        elif light1.is_close(board, player) and light1.on:
            message = "Extra light"
        elif light2.is_close(board, player) and light2.on:
            message = "Extra light"
        elif light3.is_close(board, player) and light3.on:
            message = "Extra light"
        elif player.pos_x == 4 and player.pos_y == 17:
            message = "F to read the letter"
        else:
            message = "Info"


def castle_main_hall_2(board, player):
    lit_range = 6
    print_method = 8
    letter_hall_2 = LevelItem("📜", "Letter", True, 5, 1)
    power_up = LevelItem('🕋', 'Power Up', False, 4, 34)

    engine.put_player_on_board(board, player)
    level = True
    top = "The Daemon Towers - Main Hall"
    message = "Info"
    while level:
        if not Enemies.ghost1.on and not Enemies.ghost2.on and not Enemies.ghost3.on and power_up.name == "Power Up":
            power_up.turn_on(board)

        util.clear_screen()
        main.print_level(board, message, player, print_method, top, lit_range)
        key = util.key_pressed()

        # MAIN CONTROL
        if key == 'q':
            quit_game()
        elif key == "d":
            player.move_right(board)
        elif key == "s":
            player.move_down(board)
        elif key == "w":
            player.move_up(board)
        elif key == "a":
            player.move_left(board)
        elif key == "t":
            tool_msg = "   (0): back (T)ools: "
            for tool in player.tools:
                tool_msg += tool.name + ' '
            t_pressed = True
            while t_pressed:
                util.clear_screen()
                main.print_level(board, message, player, print_method, tool_msg, lit_range)
                key = util.key_pressed()
                if key == '0':
                    t_pressed = False
                elif key == 't':
                    for index, tool in enumerate(player.tools):
                        if tool.name == '🖲 teleport':
                            return 1, player
        elif key == "i":
            main.print_character(player, " character")
        elif key == "c":
            player = cheat_mode(player)

        # OTHER CONTROLS / FIGHTS
        elif key == 'f':
            # The_Twins
            if Enemies.twins.is_close(board, player):
                win = battle(player, Enemies.twins)
                if win == 1:
                    player.get_item(Collectables.super_potion, 1)
                    print("  │ You have got the 💎 Super potion")
                    time.sleep(1)

                    player.get_item(Collectables.mystic, 1)
                    print("  │ You have got the 🔮 Mystic Elixir")
                    time.sleep(1)

                    player.get_item(Collectables.double_sword, 2)
                    print("  │ You have got the ⚔️ Double Sword x2")
                    time.sleep(1)

                    player.get_item(Collectables.grenade, 3)
                    print("  │ You have got the 💣 Grenade x3")
                    time.sleep(1)

                    player_recover(player)

                    print('  │')
                    input('  │ Press ENTER to face the Big Orb!!!')
                    return 1, player
                else:
                    return 0, player
            # GHOST1
            elif Enemies.ghost1.is_close(board, player) and Enemies.ghost1.on:
                win = battle(player, Enemies.ghost1)
                if win == 1:
                    Enemies.ghost1.turn_off(board)

                    player.get_item(Collectables.magic_drink_6, 1)
                    print("  │ You have got the 🥤 Bloody Mary")
                    time.sleep(1)

                    player.get_item(Collectables.bomb, 1)
                    print("  │ You have got the 💣 BOMB")
                    time.sleep(1)

                    player_recover(player)

                    print('  │')
                    input('  │ Press ENTER to continue...')
                else:
                    return 0, player
            # GHOST2
            elif Enemies.ghost2.is_close(board, player) and Enemies.ghost2.on:
                win = battle(player, Enemies.ghost2)
                if win == 1:
                    Enemies.ghost2.turn_off(board)

                    player.get_item(Collectables.magic_drink_6, 1)
                    print("  │ You have got the 🥤 Bloody Mary")
                    time.sleep(1)

                    player.get_item(Collectables.bomb, 1)
                    print("  │ You have got the 💣 BOMB")
                    time.sleep(1)

                    player_recover(player)

                    print('  │')
                    input('  │ Press ENTER to continue...')
                else:
                    return 0, player
            # GHOST3
            elif Enemies.ghost3.is_close(board, player) and Enemies.ghost3.on:
                win = battle(player, Enemies.ghost3)
                if win == 1:
                    Enemies.ghost3.turn_off(board)

                    player.get_item(Collectables.magic_drink_6, 1)
                    print("  │ You have got the 🥤 Bloody Mary")
                    time.sleep(1)

                    player.get_item(Collectables.bomb, 1)
                    print("  │ You have got the 💣 BOMB")
                    time.sleep(1)

                    player_recover(player)

                    print('  │')
                    input('  │ Press ENTER to continue...')
                else:
                    return 0, player
            # POWER UP
            elif power_up.is_close(board, player) and power_up.on:
                power_up.turn_off(board)
                power_up.name = "Power Down"

                power_up_player(player)

                player.get_item(Collectables.bow, 9)
                player.spell_list.append(Spells.bless)
                main.print_message(["You found a mystical power up!", '', "Your Maximum Health Points,", "Magic Points, Defence and Attack", "has been increased!", "You have got Bow 9x",
                                    "Magic unlocked: ☀ Bless of the King,", "what can remove all poison and curse effect on you!"])
            # LETTER
            elif letter_hall_2.is_close(board, player):
                main.print_message(['Remember those three goblins in the woods?', '', 'Try to find them again, and get the power up', 'in the same way!'])

        # POSITION CHECK
        if Enemies.twins.is_close(board, player):
            message = "🎎 We are the Twins! We are creepy. Come and fight with us!"
        elif Enemies.ghost1.is_close(board, player) and Enemies.ghost1.on:
            message = "BOO BOO goblin ghost. Press F to ghosting the ghost..."
        elif Enemies.ghost2.is_close(board, player) and Enemies.ghost2.on:
            message = "BOO BOO goblin ghost. Press F to ghosting the ghost..."
        elif Enemies.ghost3.is_close(board, player) and Enemies.ghost3.on:
            message = "BOO BOO goblin ghost. Press F to ghosting the ghost..."
        elif letter_hall_2.is_close(board, player):
            message = "F to read the letter."
        else:
            message = "Info"


def is_enemy_close(enemy, player, danger_range):

    return (int(enemy.pos_x) - int(player.pos_x)) ** 2 + (int(enemy.pos_y) - int(player.pos_y)) ** 2 <= danger_range ** 2


def tower(board, player):
    print_method = 9

    util.clear_screen()
    engine.put_player_on_board(board, player)
    engine.put_enemy_on_board(board, Enemies.eye)
    holo_clown = LevelItem('🤡', 'Clown', False, Enemies.eye.pos_x, Enemies.eye.pos_y - 1)
    level = True
    top = "The Daemon Towers"
    message = "Info"
    while level:
        Enemies.eye.get_random_move(board)

        if not holo_clown.on:
            holo_clown.pos_x = Enemies.eye.pos_x
            holo_clown.pos_y = Enemies.eye.pos_y - 1
            holo_clown.turn_on(board)

        util.clear_screen()
        main.print_level(board, message, Enemies.eye, print_method, top)
        key = util.key_pressed()

        # CLOWN MOVEMENT
        board[holo_clown.pos_x][holo_clown.pos_y] = '  '
        if player.pos_x < holo_clown.pos_x:
            holo_clown.pos_x -= 1
        elif holo_clown.pos_x < player.pos_x:
            holo_clown.pos_x += 1
        if holo_clown.pos_y < player.pos_y:
            holo_clown.pos_y += 1
        elif player.pos_y < holo_clown.pos_y:
            holo_clown.pos_y -= 1
        board[holo_clown.pos_x][holo_clown.pos_y] = holo_clown.icon
        if holo_clown.is_close(board, player) and holo_clown.on or holo_clown.pos_y == player.pos_y and holo_clown.pos_x == player.pos_x and holo_clown.on:
            win = battle(player, Person('🤡', 'Holo Clown', 1500, 40, 285, 5, [Spells.electricity], [{'item': Collectables.CD, 'quantity': 3}], [], 5))
            if win == 1:
                holo_clown.turn_off(board)
                continue
            else:
                return 0, player

        # MAIN CONTROL
        if key == 'q':
            quit_game()
        elif key == "d":
            player.move_right(board)
        elif key == "s":
            player.move_down(board)
        elif key == "w":
            player.move_up(board)#
        elif key == "a":
            player.move_left(board)
        elif key == "c":
            player = cheat_mode(player)
        elif key == "i":
            main.print_character(player, " character")
        elif key == "t":
            tool_msg = "   (0): back (T)ools: "
            for tool in player.tools:
                tool_msg += tool.name + ' '
            t_pressed = True
            while t_pressed:
                util.clear_screen()
                main.print_level(board, message, Enemies.eye, print_method, tool_msg)
                key = util.key_pressed()
                if key == '0':
                    t_pressed = False
                elif key == 't':
                    for index, tool in enumerate(player.tools):
                        if tool.name == '🖲 teleport':
                            return 1, player

        # OTHER CONTROLS / FIGHTS
        elif key == 'f':
            # EYE
            if is_enemy_close(Enemies.eye, player, 10):
                win = battle(player, Enemies.eye)
                if win == 1:
                    return 1, player
                else:
                    return 0, player

        # POSITION CHECK
        if is_enemy_close(Enemies.eye, player, 10):
            message = "👁 Let's fight, eye-to-eye!"
        else:
            message = "Info"
