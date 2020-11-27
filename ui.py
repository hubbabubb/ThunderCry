from classes.game import TextFormat, TextBackground
import random


def is_point_lit(index1, index2, player, lit_range=0):
    return (int(index1) - int(player.pos_x)) ** 2 + (int(index2) - int(player.pos_y)) ** 2 <= lit_range ** 2


def display_board(board, print_method, player, lit_range=0):
    for index1, row in enumerate(board):
        print("            ", end='')
        for index2, cell in enumerate(row):
            if print_method == 1:
                if cell == '┌' or cell == '──' or cell == '│' or cell == '└' or cell == '─┘' or cell == '─┐' or cell == '─┴' or cell == '─┬' or cell == ' │':
                    print(TextBackground.YELLOW + cell + TextBackground.RESET, end='')
                elif cell == '▒▒▒':
                    print(TextBackground.BLACK + TextFormat.BLACK + '                      ' + TextFormat.RESET_ALL, end='')
                else:
                    print(TextBackground.GREEN + cell + TextBackground.RESET, end='')
            elif print_method == 2:
                if cell == '┌' or cell == '──' or cell == '│' or cell == '└' or cell == '┘' or cell == '┐' or cell == '┴' or cell == '┬':
                    print(TextFormat.BLACK + cell + TextFormat.RESET_ALL, end='')
                elif cell == '▒▒▒':
                    print(TextBackground.RESET + '                      ', end='')
                elif cell == '▒':
                    print(TextBackground.MAGENTA + ' ' + TextBackground.RESET, end='')
                elif cell == '░':
                    print(TextBackground.CYAN + ' ' + TextBackground.RESET, end='')
                elif "C" or cell == "o" or cell == "s" or cell == "e" or cell == "p" or cell == "h" or cell == "a" or cell == "t" or cell == "y" or cell == "-" or cell == ">":
                    print(TextBackground.CYAN + cell + TextBackground.RESET, end='')
                else:
                    print(TextBackground.BLACK + cell, end='')
            elif print_method == 3:
                if cell == '┌' or cell == '──' or cell == '│' or cell == '└' or cell == '┘' or cell == '┐' or cell == '┴' or cell == '┬' or cell == '╞':
                    print(TextFormat.BLACK + TextBackground.WHITE + cell + TextFormat.RESET_ALL, end='')
                elif cell == '▒▒▒':
                    print(TextBackground.RESET + '         ', end='')
                elif cell == '▒▒' or cell == '▒ ':
                    print(TextBackground.GREEN + '  ' + TextBackground.RESET, end='')
                elif cell == '░░' or cell == '░ ':
                    print(TextBackground.MAGENTA + '  ' + TextBackground.RESET, end='')
                elif "C" or cell == "o" or cell == "s" or cell == "e" or cell == "p" or cell == "h" or cell == "a" or cell == "t" or cell == "y" or cell == "-" or cell == ">":
                    print(TextBackground.CYAN + cell + TextBackground.RESET, end='')
                else:
                    print(TextBackground.BLACK + cell, end='')
            elif print_method == 4:
                if is_point_lit(index1, index2, player, lit_range):
                    if cell == '▒▒':
                        print(TextBackground.YELLOW + TextFormat.DARK_GRAY + cell + TextFormat.RESET_ALL, end='')
                    else:
                        print(TextFormat.BLACK + TextBackground.YELLOW + cell, end='')
                else:
                    print(TextFormat.BLACK + '  ' + TextFormat.RESET_ALL, end='')
            elif print_method == 5:
                if cell == '▒▒▒':
                    print(TextBackground.RESET + '', end='')
                elif cell == "░░":
                    rand_wave = ['∿ ', ' ∿']
                    wave = random.choice(rand_wave)
                    print(TextBackground.BLUE + TextFormat.CYAN + wave + TextFormat.RESET_ALL, end='')
                elif cell == '══' or cell == '╦═' or cell == '═╦':
                    print(TextBackground.YELLOW + TextFormat.BLACK + cell + TextFormat.RESET_ALL, end='')
                elif cell == '▒▒' or cell == '👹':
                    print(TextBackground.YELLOW + TextFormat.GREEN + cell + TextFormat.RESET_ALL, end='')
                else:
                    print(TextBackground.GREEN + TextFormat.BLACK + cell + TextFormat.RESET_ALL, end='')
            elif print_method == 6:
                if cell == '▒▒▒':
                    print(TextBackground.RESET + '', end='')
                elif cell == "░░":
                    rand_wave = ['∿ ', ' ∿']
                    wave = random.choice(rand_wave)
                    print(TextBackground.BLUE + TextFormat.CYAN + wave + TextFormat.RESET_ALL, end='')
                elif cell == '══' or cell == '╦═' or cell == '═╦':
                    print(TextBackground.YELLOW + TextFormat.BLACK + cell + TextFormat.RESET_ALL, end='')
                elif cell == '. ' or cell == '+|' or cell == ' |' or cell == '| ' or cell == '\\ ' or cell == ' \\' or cell == ' /' or cell == '/ ' or cell == '__' or cell == '++' or cell == '+\\' or cell == "_ " or cell == '_░':
                    print(TextBackground.DARK_GRAY + TextFormat.BLACK + cell + TextFormat.RESET_ALL, end='')
                elif cell == '▩▩':
                    print(TextBackground.DARK_GRAY + '  ' + TextFormat.RESET_ALL, end='')
                elif cell == '▒▒' or cell == '👹':
                    print(TextBackground.YELLOW + TextFormat.GREEN + cell + TextFormat.RESET_ALL, end='')
                elif cell == '──':
                    print('', end='')
                else:
                    print(TextBackground.GREEN + TextFormat.BLACK + cell + TextFormat.RESET_ALL, end='')
            elif print_method == 7:
                if cell == "░" or cell == "▩▩" or cell == '🚪' or cell == '⇣▩' or cell == '⇡▩':
                    print(TextFormat.DARK_GRAY + TextBackground.LIGHT_GRAY + cell + TextFormat.RESET_ALL, end='')
                elif cell == '▒▒':
                    print(TextBackground.DARK_GRAY + TextFormat.LIGHT_GRAY + cell + TextFormat.RESET_ALL, end='')
                elif cell == "◨ ":
                    print(TextBackground.RED + TextFormat.YELLOW + cell, end='')
                elif index1 == 6 and cell == '  ' or index1 == 10 and cell == '  ':
                    print(TextBackground.RED + TextFormat.YELLOW + '◘◘', end='')
                elif index1 == 7 and cell == '  ' or index1 == 8 and cell == '  ' or index1 == 9 and cell == '  ':
                    print(TextBackground.RED + cell + TextFormat.RESET, end='')
                else:
                    print(cell, end='')
            elif print_method == 8:
                if is_point_lit(index1, index2, player, lit_range):
                    if cell == "░" or cell == "▩▩" or cell == '🚪' or cell == '⇣▩' or cell == '⇡▩':
                        print(TextFormat.DARK_GRAY + TextBackground.LIGHT_GRAY + cell + TextFormat.RESET_ALL, end='')
                    elif cell == '▒▒':
                        print(TextBackground.DARK_GRAY + TextFormat.LIGHT_GRAY + cell + TextFormat.RESET_ALL, end='')
                    elif cell == "◨ ":
                        print(TextBackground.RED + TextFormat.YELLOW + cell, end='')
                    elif index1 == 6 and cell == '  ' or index1 == 10 and cell == '  ':
                        print(TextBackground.RED + TextFormat.YELLOW + '◘◘', end='')
                    elif index1 == 7 and cell == '  ' or index1 == 8 and cell == '  ' or index1 == 9 and cell == '  ':
                        print(TextBackground.RED + cell + TextFormat.RESET, end='')
                    elif cell == "  " or cell == '👨🏼‍🔬' or cell == '🗄 ' or cell == '👳🏻' or cell == ' 🧛🏻‍♂️' or cell == '🕋' or cell == ' ░':
                        print(TextBackground.DARK_GRAY + cell + TextFormat.RESET_ALL, end='')
                    elif cell == '👻':
                        ghost_icon = ['👻', '  ']
                        print(TextBackground.DARK_GRAY + random.choice(ghost_icon) + TextFormat.RESET_ALL, end='')
                    else:
                        print(cell, end='')
                else:
                    if cell == '🎎' or cell == '👻':
                        print('  ', end='')
                    else:
                        print(TextBackground.BLACK + TextFormat.DARK_GRAY + cell + TextFormat.RESET_ALL, end='')
            elif print_method == 9:
                if is_point_lit(index1, index2, player, lit_range + 1):
                    print(TextBackground.DARK_GRAY + cell + TextBackground.RESET, end='')
                elif is_point_lit(index1, index2, player, lit_range + 5):
                    print(TextBackground.BLACK + cell + TextBackground.RESET, end='')
                elif is_point_lit(index1, index2, player, lit_range + 10):
                    print(TextBackground.DARK_GRAY + cell + TextBackground.RESET, end='')
                elif is_point_lit(index1, index2, player, lit_range + 17):
                    print(TextBackground.BLACK + cell + TextBackground.RESET, end='')
                elif is_point_lit(index1, index2, player, lit_range + 25):
                    print(TextBackground.DARK_GRAY + cell + TextBackground.RESET, end='')
                else:
                    print(TextBackground.BLACK + cell + TextBackground.RESET, end='')
            elif print_method == 10:
                if is_point_lit(index1, index2, player, lit_range + 1):
                    print(TextBackground.BLUE + cell + TextBackground.RESET, end='')
                elif is_point_lit(index1, index2, player, lit_range + 5):
                    print(TextBackground.CYAN + cell + TextBackground.RESET, end='')
                elif is_point_lit(index1, index2, player, lit_range + 10):
                    print(TextBackground.RED + cell + TextBackground.RESET, end='')
                elif is_point_lit(index1, index2, player, lit_range + 17):
                    print(TextBackground.MAGENTA + cell + TextBackground.RESET, end='')
                elif is_point_lit(index1, index2, player, lit_range + 25):
                    print(TextBackground.YELLOW + cell + TextBackground.RESET, end='')
                else:
                    print(TextBackground.LIGHT_GRAY + cell + TextBackground.RESET, end='')
            elif print_method == 11:
                if is_point_lit(index1, index2, player, lit_range + 1):
                    print(TextBackground.YELLOW + cell + TextBackground.RESET, end='')
                elif is_point_lit(index1, index2, player, lit_range + 5):
                    print(TextBackground.BLUE + cell + TextBackground.RESET, end='')
                elif is_point_lit(index1, index2, player, lit_range + 10):
                    print(TextBackground.CYAN + cell + TextBackground.RESET, end='')
                elif is_point_lit(index1, index2, player, lit_range + 17):
                    print(TextBackground.RED + cell + TextBackground.RESET, end='')
                elif is_point_lit(index1, index2, player, lit_range + 25):
                    print(TextBackground.MAGENTA + cell + TextBackground.RESET, end='')
                else:
                    print(TextBackground.LIGHT_GRAY + cell + TextBackground.RESET, end='')
            elif print_method == 12:
                if is_point_lit(index1, index2, player, lit_range + 1):
                    print(TextBackground.MAGENTA + cell + TextBackground.RESET, end='')
                elif is_point_lit(index1, index2, player, lit_range + 5):
                    print(TextBackground.YELLOW + cell + TextBackground.RESET, end='')
                elif is_point_lit(index1, index2, player, lit_range + 10):
                    print(TextBackground.BLUE + cell + TextBackground.RESET, end='')
                elif is_point_lit(index1, index2, player, lit_range + 17):
                    print(TextBackground.CYAN + cell + TextBackground.RESET, end='')
                elif is_point_lit(index1, index2, player, lit_range + 25):
                    print(TextBackground.RED + cell + TextBackground.RESET, end='')
                else:
                    print(TextBackground.LIGHT_GRAY + cell + TextBackground.RESET, end='')
            elif print_method == 13:
                if is_point_lit(index1, index2, player, lit_range + 1):
                    print(TextBackground.RED + cell + TextBackground.RESET, end='')
                elif is_point_lit(index1, index2, player, lit_range + 5):
                    print(TextBackground.MAGENTA + cell + TextBackground.RESET, end='')
                elif is_point_lit(index1, index2, player, lit_range + 10):
                    print(TextBackground.YELLOW + cell + TextBackground.RESET, end='')
                elif is_point_lit(index1, index2, player, lit_range + 17):
                    print(TextBackground.BLUE + cell + TextBackground.RESET, end='')
                elif is_point_lit(index1, index2, player, lit_range + 25):
                    print(TextBackground.CYAN + cell + TextBackground.RESET, end='')
                else:
                    print(TextBackground.LIGHT_GRAY + cell + TextBackground.RESET, end='')
            elif print_method == 14:
                if is_point_lit(index1, index2, player, lit_range + 1):
                    print(TextBackground.CYAN + cell + TextBackground.RESET, end='')
                elif is_point_lit(index1, index2, player, lit_range + 5):
                    print(TextBackground.RED + cell + TextBackground.RESET, end='')
                elif is_point_lit(index1, index2, player, lit_range + 10):
                    print(TextBackground.MAGENTA + cell + TextBackground.RESET, end='')
                elif is_point_lit(index1, index2, player, lit_range + 17):
                    print(TextBackground.YELLOW + cell + TextBackground.RESET, end='')
                elif is_point_lit(index1, index2, player, lit_range + 25):
                    print(TextBackground.BLUE + cell + TextBackground.RESET, end='')
                else:
                    print(TextBackground.LIGHT_GRAY + cell + TextBackground.RESET, end='')
        print()
