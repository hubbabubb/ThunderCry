from classes.game import Person, CharacterTypes, TextFormat, TextBackground, read_save_file, write_save_file, LevelItem, Enemies
from classes.magic import Spells
from classes.inventory import Collectables
from classes import levels

import time
import util
import engine
import ui
import pygame


def intro():
    s = pygame.mixer.Sound("battle.wav")
    s.play(-1)

    util.clear_screen()
    print()
    print(TextBackground.WHITE + TextFormat.BLACK + TextFormat.Bold + '      ___       ___            ___       ___       ___       ___       ___       ___       ___      ')
    print('     /\\__\\     /\\  \\          /\  \     /\\  \\     /\\  \\     /\\__\\     /\\__\\     /\\__\\     /\\  \\     ')
    print('    /:/  /    /::\\  \\        /::\  \   /::\\  \\   /::\\  \\   /:/  /    /:/ _/_   /:| _|_   /::\\  \\    ')
    print('   /:/__/    /::\\:\\__\\      /\\:\\:\__\ /::\\:\\__\\ /::\\:\\__\\ /:/__/    /:/_/\\__\\ /::|/\\__\\ /::\\:\\__\\   ')
    print('   \\:\\  \\    \\/\\::/  /      \\:\\:\\/__/ \\/\\::/  / \\:\\:\\/  / \\:\\  \    \\:\\/:/  / \\/|::/  / \\/\\::/  /   ')
    print('    \\:\\__\\     /:/  /        \\::/  /     \\/__/   \\:\\/  /   \\:\\__\    \\::/  /    |:/  /    /:/  /    ')
    print('     \\/__/     \\/__/          \\/__/               \\/__/     \\/__/     \\/__/     \\/__/     \/__/     ')
    print('                                                       _                                            ' + TextFormat.RESET_ALL)
    time.sleep(1)
    print('                                        __ _ _ __   __| |')
    print('                                       / _` | \'_ \ / _` |')
    print('                                      | (_| | | | | (_| |')
    print('                                       \__,_|_| |_|\__,_|')
    time.sleep(1)
    print('                 ██████╗ ' + TextBackground.RED + '   ' + TextBackground.BLUE + '   ' + TextBackground.RESET + '╗ ██████╗ ███████╗ ██████╗ ██████╗  ██████╗ ██╗    ')
    print('                ██╔════╝' + TextBackground.BLUE + '  ' + TextBackground.RESET + '╔═══' + TextBackground.RED + '  ' + TextBackground.RESET + '╗██╔══██╗██╔════╝██╔════╝██╔═══██╗██╔═══██╗██║')
    print('                ██║     ' + TextBackground.RED + ' ' + TextBackground.BLUE + ' ' + TextBackground.RESET + '║   ' + TextBackground.BLUE + ' ' + TextBackground.RED + ' ' + TextBackground.RESET + '║██║  ██║█████╗  ██║     ██║   ██║██║   ██║██║')
    print('                ██║     ' + TextBackground.RED + '  ' + TextBackground.RESET + '║   ' + TextBackground.BLUE + '  ' + TextBackground.RESET + '║██║  ██║██╔══╝  ██║     ██║   ██║██║   ██║██║')
    print('                ╚██████╗╚' + TextBackground.BLUE + '   ' + TextBackground.RED + '   ' + TextBackground.RESET + '╔╝██████╔╝███████╗╚██████╗╚██████╔╝╚██████╔╝███████╗')
    print('                 ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚╤═╤══╝  ╚═════╝ ╚══════╝')
    time.sleep(1)
    print('                             _ __  _ __ ___  ___  ___ _ __ | |_ ___')
    print('                            | \'_ \| \'__/ _ \/ __|/ _ \ \'_ \| __/ __|')
    print('                            | |_) | | |  __/\__ \  __/ | | | |_\__ \ ')
    print('                            | .__/|_|  \___||___/\___|_| |_|\__|___/ ')
    print('                            |_|')
    time.sleep(4)

    util.clear_screen()
    print('\n \n \n \n')
    print(TextFormat.YELLOW + '    ██       ▄█    █▄   ██    █▄  ██▄▄▄   ██████▄    ▄███████   ▄███████ ▄███████   ▄██████ ▄█  ▄   ')
    time.sleep(0.1)
    print(' ████████▄   ██    ██   ██    ██ ██▀▀▀█▄ ██   ▀██   ██    ██   ██    ██ ██    ██   ██    ██ ██  █▄')
    time.sleep(0.1)
    print('   ▀██▀▀██   ██    ██   ██    ██ ██   ██ ██    ██   ██    █▀   ██    ██ ██    █▀   ██    ██ ██▄▄██')
    time.sleep(0.1)
    print('    ██   ▀  ▄██▄▄▄▄██▄▄ ██    ██ ██   ██ ██    ██  ▄██▄▄▄     ▄██▄▄▄▄█▀ ██        ▄██▄▄▄▄█▀ ▀▀▀▀██')
    time.sleep(0.1)
    print('    ██     ▀▀██▀▀▀▀██▀  ██    ██ ██   ██ ██    ██ ▀▀██▀▀▀    ▀▀██▀▀▀▀▀  ██       ▀▀██▀▀▀▀▀  ▄█  ██')
    time.sleep(0.1)
    print('    ██       ██    ██   ██    ██ ██   ██ ██    ██   ██    █▄ ▀█████████ ██    █▄▀█████████ ██   ██')
    time.sleep(0.1)
    print('    ██       ██    ██   ██    ██ ██   ██ ██   ▄██   ██    ██   ██    ██ ██    ██  ██    ██ ██   ██')
    time.sleep(0.1)
    print('   ▄███▀     ██    █▀   ██████▀  ▀█   █▀ ███████▀   ████████   ██    ██ ███████▀  ██    ██  ▀███▀  ')
    time.sleep(0.1)
    print('                                                              ██    ██           ██    ██           ' + TextFormat.RESET_ALL)
    time.sleep(1)
    print(TextFormat.MAGENTA)
    util.clear_screen()
    print('\n \n \n \n')
    print(TextFormat.YELLOW + '    ██       ▄█    █▄   ██    █▄  ██▄▄▄   ██████▄    ▄███████   ▄███████ ▄███████   ▄██████ ▄█  ▄   ')
    print(' ████████▄   ██    ██   ██    ██ ██▀▀▀█▄ ██   ▀██   ██    ██   ██    ██ ██    ██   ██    ██ ██  █▄')
    print('   ▀██▀▀██   ██    ██   ██    ██ ██   ██ ██    ██   ██    █▀   ██    ██ ██    █▀   ██    ██ ██▄▄██')
    print('    ██   ▀  ▄██▄▄▄▄██▄▄ ██    ██ ██   ██ ██    ██  ▄██▄▄▄     ▄██▄▄▄▄█▀ ██        ▄██▄▄▄▄█▀ ▀▀▀▀██')
    print('    ██     ▀▀██▀▀▀▀██▀  ██    ██ ██   ██ ██    ██ ▀▀██▀▀▀    ▀▀██▀▀▀▀▀  ██       ▀▀██▀▀▀▀▀  ▄█  ██')
    print('    ██       ██    ██   ██    ██ ██   ██ ██    ██   ██    █▄ ▀█████████ ██    █▄▀█████████ ██   ██')
    print('    ██       ██    ██   ██    ██ ██   ██ ██   ▄██   ██    ██   ██    ██ ██    ██  ██    ██ ██   ██')
    print('   ▄███▀     ██    █▀   ██████▀  ▀█   █▀ ███████▀   ████████   ██    ██ ███████▀  ██    ██  ▀███▀  ')
    print('                                                              ██    ██           ██    ██           ' + TextFormat.RESET_ALL)
    print(TextFormat.MAGENTA)
    print('                   ┌─┐┌┐┌┌┬┐')
    print('                   ├─┤│││ ││')
    print('                   ┴ ┴┘└┘─┴┘ ')
    time.sleep(1)
    util.clear_screen()
    print('\n \n \n \n')
    print(TextFormat.YELLOW + '    ██       ▄█    █▄   ██    █▄  ██▄▄▄   ██████▄    ▄███████   ▄███████ ▄███████   ▄██████ ▄█  ▄   ')
    print(' ████████▄   ██    ██   ██    ██ ██▀▀▀█▄ ██   ▀██   ██    ██   ██    ██ ██    ██   ██    ██ ██  █▄')
    print('   ▀██▀▀██   ██    ██   ██    ██ ██   ██ ██    ██   ██    █▀   ██    ██ ██    █▀   ██    ██ ██▄▄██')
    print('    ██   ▀  ▄██▄▄▄▄██▄▄ ██    ██ ██   ██ ██    ██  ▄██▄▄▄     ▄██▄▄▄▄█▀ ██        ▄██▄▄▄▄█▀ ▀▀▀▀██')
    print('    ██     ▀▀██▀▀▀▀██▀  ██    ██ ██   ██ ██    ██ ▀▀██▀▀▀    ▀▀██▀▀▀▀▀  ██       ▀▀██▀▀▀▀▀  ▄█  ██')
    print('    ██       ██    ██   ██    ██ ██   ██ ██    ██   ██    █▄ ▀█████████ ██    █▄▀█████████ ██   ██')
    print('    ██       ██    ██   ██    ██ ██   ██ ██   ▄██   ██    ██   ██    ██ ██    ██  ██    ██ ██   ██')
    print('   ▄███▀     ██    █▀   ██████▀  ▀█   █▀ ███████▀   ████████   ██    ██ ███████▀  ██    ██  ▀███▀  ')
    print('                                                              ██    ██           ██    ██           ' + TextFormat.RESET_ALL)
    print(TextFormat.MAGENTA)
    print('                   ┌─┐┌┐┌┌┬┐  ┌┬┐┬ ┬┌─┐ ')
    print('                   ├─┤│││ ││   │ ├─┤├┤  ')
    print('                   ┴ ┴┘└┘─┴┘   ┴ ┴ ┴└─┘ ')
    time.sleep(1)
    util.clear_screen()
    print('\n \n \n \n')
    print(TextFormat.YELLOW + '    ██       ▄█    █▄   ██    █▄  ██▄▄▄   ██████▄    ▄███████   ▄███████ ▄███████   ▄██████ ▄█  ▄   ')
    print(' ████████▄   ██    ██   ██    ██ ██▀▀▀█▄ ██   ▀██   ██    ██   ██    ██ ██    ██   ██    ██ ██  █▄')
    print('   ▀██▀▀██   ██    ██   ██    ██ ██   ██ ██    ██   ██    █▀   ██    ██ ██    █▀   ██    ██ ██▄▄██')
    print('    ██   ▀  ▄██▄▄▄▄██▄▄ ██    ██ ██   ██ ██    ██  ▄██▄▄▄     ▄██▄▄▄▄█▀ ██        ▄██▄▄▄▄█▀ ▀▀▀▀██')
    print('    ██     ▀▀██▀▀▀▀██▀  ██    ██ ██   ██ ██    ██ ▀▀██▀▀▀    ▀▀██▀▀▀▀▀  ██       ▀▀██▀▀▀▀▀  ▄█  ██')
    print('    ██       ██    ██   ██    ██ ██   ██ ██    ██   ██    █▄ ▀█████████ ██    █▄▀█████████ ██   ██')
    print('    ██       ██    ██   ██    ██ ██   ██ ██   ▄██   ██    ██   ██    ██ ██    ██  ██    ██ ██   ██')
    print('   ▄███▀     ██    █▀   ██████▀  ▀█   █▀ ███████▀   ████████   ██    ██ ███████▀  ██    ██  ▀███▀  ')
    print('                                                              ██    ██           ██    ██           ' + TextFormat.RESET_ALL)
    print(TextFormat.MAGENTA)
    print('                   ┌─┐┌┐┌┌┬┐  ┌┬┐┬ ┬┌─┐  ╔╦╗┌─┐┌─┐┌┬┐┌─┐┌┐┌  ╔╦╗┌─┐┬ ┬┌─┐┬─┐┌─┐')
    print('                   ├─┤│││ ││   │ ├─┤├┤    ║║├─┤├┤ ││││ ││││   ║ │ ││││├┤ ├┬┘└─┐')
    print('                   ┴ ┴┘└┘─┴┘   ┴ ┴ ┴└─┘  ═╩╝┴ ┴└─┘┴ ┴└─┘┘└┘   ╩ └─┘└┴┘└─┘┴└─└─┘' + TextFormat.RESET_ALL + '\n \n \n \n')
    time.sleep(2)
    util.clear_screen()
    print('\n \n \n \n')
    print(TextFormat.YELLOW + '    ██       ▄█    █▄   ██    █▄  ██▄▄▄   ██████▄    ▄███████   ▄███████ ▄███████   ▄██████ ▄█  ▄   ')
    print(' ████████▄   ██    ██   ██    ██ ██▀▀▀█▄ ██   ▀██   ██    ██   ██    ██ ██    ██   ██    ██ ██  █▄')
    print('   ▀██▀▀██   ██    ██   ██    ██ ██   ██ ██    ██   ██    █▀   ██    ██ ██    █▀   ██    ██ ██▄▄██')
    print('    ██   ▀  ▄██▄▄▄▄██▄▄ ██    ██ ██   ██ ██    ██  ▄██▄▄▄     ▄██▄▄▄▄█▀ ██        ▄██▄▄▄▄█▀ ▀▀▀▀██')
    print('    ██     ▀▀██▀▀▀▀██▀  ██    ██ ██   ██ ██    ██ ▀▀██▀▀▀    ▀▀██▀▀▀▀▀  ██       ▀▀██▀▀▀▀▀  ▄█  ██')
    print('    ██       ██    ██   ██    ██ ██   ██ ██    ██   ██    █▄ ▀█████████ ██    █▄▀█████████ ██   ██')
    print('    ██       ██    ██   ██    ██ ██   ██ ██   ▄██   ██    ██   ██    ██ ██    ██  ██    ██ ██   ██')
    print('   ▄███▀     ██    █▀   ██████▀  ▀█   █▀ ███████▀   ████████   ██    ██ ███████▀  ██    ██  ▀███▀  ')
    print('                                                              ██    ██           ██    ██           ' + TextFormat.RESET_ALL)
    print(TextFormat.MAGENTA)
    print('                   ┌─┐┌┐┌┌┬┐  ┌┬┐┬ ┬┌─┐                      ╔╦╗┌─┐┬ ┬┌─┐┬─┐┌─┐')
    print('                   ├─┤│││ ││   │ ├─┤├┤                        ║ │ ││││├┤ ├┬┘└─┐')
    print('                   ┴ ┴┘└┘─┴┘   ┴ ┴ ┴└─┘                       ╩ └─┘└┴┘└─┘┴└─└─┘' + TextFormat.RESET_ALL + '\n \n \n \n')
    time.sleep(0.2)
    util.clear_screen()
    print('\n \n \n \n')
    print(TextFormat.YELLOW + '    ██       ▄█    █▄   ██    █▄  ██▄▄▄   ██████▄    ▄███████   ▄███████ ▄███████   ▄██████ ▄█  ▄   ')
    print(' ████████▄   ██    ██   ██    ██ ██▀▀▀█▄ ██   ▀██   ██    ██   ██    ██ ██    ██   ██    ██ ██  █▄')
    print('   ▀██▀▀██   ██    ██   ██    ██ ██   ██ ██    ██   ██    █▀   ██    ██ ██    █▀   ██    ██ ██▄▄██')
    print('    ██   ▀  ▄██▄▄▄▄██▄▄ ██    ██ ██   ██ ██    ██  ▄██▄▄▄     ▄██▄▄▄▄█▀ ██        ▄██▄▄▄▄█▀ ▀▀▀▀██')
    print('    ██     ▀▀██▀▀▀▀██▀  ██    ██ ██   ██ ██    ██ ▀▀██▀▀▀    ▀▀██▀▀▀▀▀  ██       ▀▀██▀▀▀▀▀  ▄█  ██')
    print('    ██       ██    ██   ██    ██ ██   ██ ██    ██   ██    █▄ ▀█████████ ██    █▄▀█████████ ██   ██')
    print('    ██       ██    ██   ██    ██ ██   ██ ██   ▄██   ██    ██   ██    ██ ██    ██  ██    ██ ██   ██')
    print('   ▄███▀     ██    █▀   ██████▀  ▀█   █▀ ███████▀   ████████   ██    ██ ███████▀  ██    ██  ▀███▀  ')
    print('                                                              ██    ██           ██    ██           ' + TextFormat.RESET_ALL)
    print(TextFormat.MAGENTA)
    print('                   ┌─┐┌┐┌┌┬┐  ┌┬┐┬ ┬┌─┐  ╔╦╗┌─┐┌─┐┌┬┐┌─┐┌┐┌  ╔╦╗┌─┐┬ ┬┌─┐┬─┐┌─┐')
    print('                   ├─┤│││ ││   │ ├─┤├┤    ║║├─┤├┤ ││││ ││││   ║ │ ││││├┤ ├┬┘└─┐')
    print('                   ┴ ┴┘└┘─┴┘   ┴ ┴ ┴└─┘  ═╩╝┴ ┴└─┘┴ ┴└─┘┘└┘   ╩ └─┘└┴┘└─┘┴└─└─┘' + TextFormat.RESET_ALL + '\n \n \n \n')
    time.sleep(0.1)
    util.clear_screen()
    print('\n \n \n \n')
    print(TextFormat.YELLOW + '    ██       ▄█    █▄   ██    █▄  ██▄▄▄   ██████▄    ▄███████   ▄███████ ▄███████   ▄██████ ▄█  ▄   ')
    print(' ████████▄   ██    ██   ██    ██ ██▀▀▀█▄ ██   ▀██   ██    ██   ██    ██ ██    ██   ██    ██ ██  █▄')
    print('   ▀██▀▀██   ██    ██   ██    ██ ██   ██ ██    ██   ██    █▀   ██    ██ ██    █▀   ██    ██ ██▄▄██')
    print('    ██   ▀  ▄██▄▄▄▄██▄▄ ██    ██ ██   ██ ██    ██  ▄██▄▄▄     ▄██▄▄▄▄█▀ ██        ▄██▄▄▄▄█▀ ▀▀▀▀██')
    print('    ██     ▀▀██▀▀▀▀██▀  ██    ██ ██   ██ ██    ██ ▀▀██▀▀▀    ▀▀██▀▀▀▀▀  ██       ▀▀██▀▀▀▀▀  ▄█  ██')
    print('    ██       ██    ██   ██    ██ ██   ██ ██    ██   ██    █▄ ▀█████████ ██    █▄▀█████████ ██   ██')
    print('    ██       ██    ██   ██    ██ ██   ██ ██   ▄██   ██    ██   ██    ██ ██    ██  ██    ██ ██   ██')
    print('   ▄███▀     ██    █▀   ██████▀  ▀█   █▀ ███████▀   ████████   ██    ██ ███████▀  ██    ██  ▀███▀  ')
    print('                                                              ██    ██           ██    ██           ' + TextFormat.RESET_ALL)
    print(TextFormat.MAGENTA)
    print('                   ┌─┐┌┐┌┌┬┐  ┌┬┐┬ ┬┌─┐                      ╔╦╗┌─┐┬ ┬┌─┐┬─┐┌─┐')
    print('                   ├─┤│││ ││   │ ├─┤├┤                        ║ │ ││││├┤ ├┬┘└─┐')
    print('                   ┴ ┴┘└┘─┴┘   ┴ ┴ ┴└─┘                       ╩ └─┘└┴┘└─┘┴└─└─┘' + TextFormat.RESET_ALL + '\n \n \n \n')
    time.sleep(0.2)
    util.clear_screen()
    print('\n \n \n \n')
    print(TextFormat.YELLOW + '    ██       ▄█    █▄   ██    █▄  ██▄▄▄   ██████▄    ▄███████   ▄███████ ▄███████   ▄██████ ▄█  ▄   ')
    print(' ████████▄   ██    ██   ██    ██ ██▀▀▀█▄ ██   ▀██   ██    ██   ██    ██ ██    ██   ██    ██ ██  █▄')
    print('   ▀██▀▀██   ██    ██   ██    ██ ██   ██ ██    ██   ██    █▀   ██    ██ ██    █▀   ██    ██ ██▄▄██')
    print('    ██   ▀  ▄██▄▄▄▄██▄▄ ██    ██ ██   ██ ██    ██  ▄██▄▄▄     ▄██▄▄▄▄█▀ ██        ▄██▄▄▄▄█▀ ▀▀▀▀██')
    print('    ██     ▀▀██▀▀▀▀██▀  ██    ██ ██   ██ ██    ██ ▀▀██▀▀▀    ▀▀██▀▀▀▀▀  ██       ▀▀██▀▀▀▀▀  ▄█  ██')
    print('    ██       ██    ██   ██    ██ ██   ██ ██    ██   ██    █▄ ▀█████████ ██    █▄▀█████████ ██   ██')
    print('    ██       ██    ██   ██    ██ ██   ██ ██   ▄██   ██    ██   ██    ██ ██    ██  ██    ██ ██   ██')
    print('   ▄███▀     ██    █▀   ██████▀  ▀█   █▀ ███████▀   ████████   ██    ██ ███████▀  ██    ██  ▀███▀  ')
    print('                                                              ██    ██           ██    ██           ' + TextFormat.RESET_ALL)
    print(TextFormat.MAGENTA)
    print('                   ┌─┐┌┐┌┌┬┐  ┌┬┐┬ ┬┌─┐  ╔╦╗┌─┐┌─┐┌┬┐┌─┐┌┐┌  ╔╦╗┌─┐┬ ┬┌─┐┬─┐┌─┐')
    print('                   ├─┤│││ ││   │ ├─┤├┤    ║║├─┤├┤ ││││ ││││   ║ │ ││││├┤ ├┬┘└─┐')
    print('                   ┴ ┴┘└┘─┴┘   ┴ ┴ ┴└─┘  ═╩╝┴ ┴└─┘┴ ┴└─┘┘└┘   ╩ └─┘└┴┘└─┘┴└─└─┘' + TextFormat.RESET_ALL + '\n \n \n \n')
    print('                                Press any button to continue...')
    key = util.key_pressed()
    if key == 'q':
        exit()
    else:
        util.clear_screen()
        print('\n \n \n \n')
        print(TextFormat.YELLOW + '    ██       ▄█    █▄   ██    █▄  ██▄▄▄   ██████▄    ▄███████   ▄███████ ▄███████   ▄██████ ▄█  ▄   ')
        print(' ████████▄   ██    ██   ██    ██ ██▀▀▀█▄ ██   ▀██   ██    ██   ██    ██ ██    ██   ██    ██ ██  █▄')
        print('   ▀██▀▀██   ██    ██   ██    ██ ██   ██ ██    ██   ██    █▀   ██    ██ ██    █▀   ██    ██ ██▄▄██')
        print('    ██   ▀  ▄██▄▄▄▄██▄▄ ██    ██ ██   ██ ██    ██  ▄██▄▄▄     ▄██▄▄▄▄█▀ ██        ▄██▄▄▄▄█▀ ▀▀▀▀██')
        print('    ██     ▀▀██▀▀▀▀██▀  ██    ██ ██   ██ ██    ██ ▀▀██▀▀▀    ▀▀██▀▀▀▀▀  ██       ▀▀██▀▀▀▀▀  ▄█  ██')
        print('    ██       ██    ██   ██    ██ ██   ██ ██    ██   ██    █▄ ▀█████████ ██    █▄▀█████████ ██   ██')
        print('    ██       ██    ██   ██    ██ ██   ██ ██   ▄██   ██    ██   ██    ██ ██    ██  ██    ██ ██   ██')
        print('   ▄███▀     ██    █▀   ██████▀  ▀█   █▀ ███████▀   ████████   ██    ██ ███████▀  ██    ██  ▀███▀  ')
        print('                                                              ██    ██           ██    ██           ' + TextFormat.RESET_ALL)
        print(TextFormat.MAGENTA)
        print('                   ┌─┐┌┐┌┌┬┐  ┌┬┐┬ ┬┌─┐                      ╔╦╗┌─┐┬ ┬┌─┐┬─┐┌─┐')
        print('                   ├─┤│││ ││   │ ├─┤├┤                        ║ │ ││││├┤ ├┬┘└─┐')
        print('                   ┴ ┴┘└┘─┴┘   ┴ ┴ ┴└─┘                       ╩ └─┘└┴┘└─┘┴└─└─┘' + TextFormat.RESET_ALL + '\n \n \n \n')
        time.sleep(0.2)
        util.clear_screen()
        print('\n \n \n \n')
        print(TextFormat.YELLOW + '    ██       ▄█    █▄   ██    █▄  ██▄▄▄   ██████▄    ▄███████   ▄███████ ▄███████   ▄██████ ▄█  ▄   ')
        print(' ████████▄   ██    ██   ██    ██ ██▀▀▀█▄ ██   ▀██   ██    ██   ██    ██ ██    ██   ██    ██ ██  █▄')
        print('   ▀██▀▀██   ██    ██   ██    ██ ██   ██ ██    ██   ██    █▀   ██    ██ ██    █▀   ██    ██ ██▄▄██')
        print('    ██   ▀  ▄██▄▄▄▄██▄▄ ██    ██ ██   ██ ██    ██  ▄██▄▄▄     ▄██▄▄▄▄█▀ ██        ▄██▄▄▄▄█▀ ▀▀▀▀██')
        print('    ██     ▀▀██▀▀▀▀██▀  ██    ██ ██   ██ ██    ██ ▀▀██▀▀▀    ▀▀██▀▀▀▀▀  ██       ▀▀██▀▀▀▀▀  ▄█  ██')
        print('    ██       ██    ██   ██    ██ ██   ██ ██    ██   ██    █▄ ▀█████████ ██    █▄▀█████████ ██   ██')
        print('    ██       ██    ██   ██    ██ ██   ██ ██   ▄██   ██    ██   ██    ██ ██    ██  ██    ██ ██   ██')
        print('   ▄███▀     ██    █▀   ██████▀  ▀█   █▀ ███████▀   ████████   ██    ██ ███████▀  ██    ██  ▀███▀  ')
        print('                                                              ██    ██           ██    ██           ' + TextFormat.RESET_ALL)
        print(TextFormat.MAGENTA)
        print('                   ┌─┐┌┐┌┌┬┐  ┌┬┐┬ ┬┌─┐  ╔╦╗┌─┐┌─┐┌┬┐┌─┐┌┐┌  ╔╦╗┌─┐┬ ┬┌─┐┬─┐┌─┐')
        print('                   ├─┤│││ ││   │ ├─┤├┤    ║║├─┤├┤ ││││ ││││   ║ │ ││││├┤ ├┬┘└─┐')
        print('                   ┴ ┴┘└┘─┴┘   ┴ ┴ ┴└─┘  ═╩╝┴ ┴└─┘┴ ┴└─┘┘└┘   ╩ └─┘└┴┘└─┘┴└─└─┘' + TextFormat.RESET_ALL + '\n \n \n \n')
        time.sleep(0.1)
        util.clear_screen()
        print('\n \n \n \n')
        print(TextFormat.YELLOW + '    ██       ▄█    █▄   ██    █▄  ██▄▄▄   ██████▄    ▄███████   ▄███████ ▄███████   ▄██████ ▄█  ▄   ')
        print(' ████████▄   ██    ██   ██    ██ ██▀▀▀█▄ ██   ▀██   ██    ██   ██    ██ ██    ██   ██    ██ ██  █▄')
        print('   ▀██▀▀██   ██    ██   ██    ██ ██   ██ ██    ██   ██    █▀   ██    ██ ██    █▀   ██    ██ ██▄▄██')
        print('    ██   ▀  ▄██▄▄▄▄██▄▄ ██    ██ ██   ██ ██    ██  ▄██▄▄▄     ▄██▄▄▄▄█▀ ██        ▄██▄▄▄▄█▀ ▀▀▀▀██')
        print('    ██     ▀▀██▀▀▀▀██▀  ██    ██ ██   ██ ██    ██ ▀▀██▀▀▀    ▀▀██▀▀▀▀▀  ██       ▀▀██▀▀▀▀▀  ▄█  ██')
        print('    ██       ██    ██   ██    ██ ██   ██ ██    ██   ██    █▄ ▀█████████ ██    █▄▀█████████ ██   ██')
        print('    ██       ██    ██   ██    ██ ██   ██ ██   ▄██   ██    ██   ██    ██ ██    ██  ██    ██ ██   ██')
        print('   ▄███▀     ██    █▀   ██████▀  ▀█   █▀ ███████▀   ████████   ██    ██ ███████▀  ██    ██  ▀███▀  ')
        print('                                                              ██    ██           ██    ██           ' + TextFormat.RESET_ALL)
        print(TextFormat.MAGENTA)
        print('                   ┌─┐┌┐┌┌┬┐  ┌┬┐┬ ┬┌─┐                      ╔╦╗┌─┐┬ ┬┌─┐┬─┐┌─┐')
        print('                   ├─┤│││ ││   │ ├─┤├┤                        ║ │ ││││├┤ ├┬┘└─┐')
        print('                   ┴ ┴┘└┘─┴┘   ┴ ┴ ┴└─┘                       ╩ └─┘└┴┘└─┘┴└─└─┘' + TextFormat.RESET_ALL + '\n \n \n \n')
        time.sleep(0.2)
        util.clear_screen()
        print('\n \n \n \n')
        print(TextFormat.YELLOW + '    ██       ▄█    █▄   ██    █▄  ██▄▄▄   ██████▄    ▄███████   ▄███████ ▄███████   ▄██████ ▄█  ▄   ')
        print(' ████████▄   ██    ██   ██    ██ ██▀▀▀█▄ ██   ▀██   ██    ██   ██    ██ ██    ██   ██    ██ ██  █▄')
        print('   ▀██▀▀██   ██    ██   ██    ██ ██   ██ ██    ██   ██    █▀   ██    ██ ██    █▀   ██    ██ ██▄▄██')
        print('    ██   ▀  ▄██▄▄▄▄██▄▄ ██    ██ ██   ██ ██    ██  ▄██▄▄▄     ▄██▄▄▄▄█▀ ██        ▄██▄▄▄▄█▀ ▀▀▀▀██')
        print('    ██     ▀▀██▀▀▀▀██▀  ██    ██ ██   ██ ██    ██ ▀▀██▀▀▀    ▀▀██▀▀▀▀▀  ██       ▀▀██▀▀▀▀▀  ▄█  ██')
        print('    ██       ██    ██   ██    ██ ██   ██ ██    ██   ██    █▄ ▀█████████ ██    █▄▀█████████ ██   ██')
        print('    ██       ██    ██   ██    ██ ██   ██ ██   ▄██   ██    ██   ██    ██ ██    ██  ██    ██ ██   ██')
        print('   ▄███▀     ██    █▀   ██████▀  ▀█   █▀ ███████▀   ████████   ██    ██ ███████▀  ██    ██  ▀███▀  ')
        print('                                                              ██    ██           ██    ██           ' + TextFormat.RESET_ALL)
        print(TextFormat.MAGENTA)
        print('                   ┌─┐┌┐┌┌┬┐  ┌┬┐┬ ┬┌─┐  ╔╦╗┌─┐┌─┐┌┬┐┌─┐┌┐┌  ╔╦╗┌─┐┬ ┬┌─┐┬─┐┌─┐')
        print('                   ├─┤│││ ││   │ ├─┤├┤    ║║├─┤├┤ ││││ ││││   ║ │ ││││├┤ ├┬┘└─┐')
        print('                   ┴ ┴┘└┘─┴┘   ┴ ┴ ┴└─┘  ═╩╝┴ ┴└─┘┴ ┴└─┘┘└┘   ╩ └─┘└┴┘└─┘┴└─└─┘' + TextFormat.RESET_ALL + '\n \n \n \n')
        time.sleep(1)
        util.clear_screen()
        print('\n \n \n \n')
        print(TextFormat.YELLOW + '    ██       ▄█    █▄   ██    █▄  ██▄▄▄   ██████▄    ▄███████   ▄███████ ▄███████   ▄██████ ▄█  ▄   ')
        print(' ████████▄   ██    ██   ██    ██ ██▀▀▀█▄ ██   ▀██   ██    ██   ██    ██ ██    ██   ██    ██ ██  █▄')
        print('   ▀██▀▀██   ██    ██   ██    ██ ██   ██ ██    ██   ██    █▀   ██    ██ ██    █▀   ██    ██ ██▄▄██')
        print('    ██   ▀  ▄██▄▄▄▄██▄▄ ██    ██ ██   ██ ██    ██  ▄██▄▄▄     ▄██▄▄▄▄█▀ ██        ▄██▄▄▄▄█▀ ▀▀▀▀██')
        print('    ██     ▀▀██▀▀▀▀██▀  ██    ██ ██   ██ ██    ██ ▀▀██▀▀▀    ▀▀██▀▀▀▀▀  ██       ▀▀██▀▀▀▀▀  ▄█  ██')
        print('    ██       ██    ██   ██    ██ ██   ██ ██    ██   ██    █▄ ▀█████████ ██    █▄▀█████████ ██   ██')
        print('    ██       ██    ██   ██    ██ ██   ██ ██   ▄██   ██    ██   ██    ██ ██    ██  ██    ██ ██   ██')
        print('   ▄███▀     ██    █▀   ██████▀  ▀█   █▀ ███████▀   ████████   ██    ██ ███████▀  ██    ██  ▀███▀  ')
        print('                                                              ██    ██           ██    ██           ' + TextFormat.RESET_ALL)
        time.sleep(1)
        volume = 1
        for load in range(5):
            volume -= 0.2
            s.set_volume(volume)
            for dot in range(4):
                util.clear_screen()
                print(" ☯︎ Loading" + '.' * dot)
                time.sleep(0.2)
        s.stop()


def print_level(board, message, player, print_method, top, lit_range=0):
    print("  ┌─────────────────────────────────────────────────────────────────────────────────────────────┐")
    print('  │' + TextFormat.Bold + top.center(93) + TextFormat.RESET_ALL + '│')
    print("  └─────────────────────────────────────────────────────────────────────────────────────────────┘ ")
    ui.display_board(board, print_method, player, lit_range)
    print('   ☯︎ ' + message)


def print_message(message_text):
    util.clear_screen()
    print()
    print("        ", end='')
    print('      ' + TextBackground.YELLOW + '┌──────────────────────────────────────────────────────────────────────┐' + TextBackground.RESET)
    for message in message_text:
        print("        ", end='')
        print('      ' + TextBackground.YELLOW + '│' + message.center(70) + '│' + TextBackground.RESET)
    print("        ", end='')
    print('      ' + TextBackground.YELLOW + '└──────────────────────────────────────────────────────────────────────┘' + TextBackground.RESET)
    print()
    input("   ☯︎ Press ENTER to continue...")
    return False


def print_character(player, char_typo):
    util.clear_screen()
    print('          *--*--*--*--*--*--*--*')
    print('   YOUR CHARACTER:\n')
    print('   ', player.icon, player.name)
    print('    A' + char_typo, 'with', TextFormat.BLUE, str(player.maxhp), 'health points and', TextFormat.CYAN + str(player.mp), 'magic points.', TextFormat.RESET_ALL)
    print('    Your ', TextFormat.RED, f'average damage will be {player.atk}' + TextFormat.RESET_ALL + ', what you can improve during your way.')
    print('    Your shield blocks ', TextFormat.YELLOW, str(player.df), ' points', TextFormat.RESET_ALL, 'from enemy attacks.\n')
    if len(player.spell_list) != 0:
        print('          *--*--*--*--*--*--*--*')
        print('    Your spells:\n')
        for spell in player.spell_list:
            print(f"    {spell.name}" + TextFormat.CYAN + f" (cost: {spell.cost}, damage: {spell.dmg})." + TextFormat.RESET_ALL)
    if len(player.items) != 0:
        print('          *--*--*--*--*--*--*--*')
        print('    Your items:\n')
        for item in player.items:
            print(f"    {item['item'].name}" + TextFormat.BLUE + f" ({item['item'].description}) x{item['quantity']}" + TextFormat.RESET_ALL)
    print()
    input("    Press ENTER to continue...")


def create_player():
    player = Person(" @", 0, 0, 0, 0, 0, 0, 0, 0, 'Tutorial')
    board = engine.create_board(player)
    tutorial(board, player)

    board = engine.create_board(player)
    gender(board, player)

    board = engine.create_board(player)
    c_type, save = char_type(board, player)

    util.clear_screen()
    while True:
        print()
        name = input('Give your character a name(max 15 characters): ')
        if len(name) > 15:
            print('Sadly it is more than 15 characters.')
            continue
        break

    if player.level == 2:
        if c_type == 1:
            icon = CharacterTypes.wizzard_him
            player = Person(icon, name, 500, 250, 75, 25, [Spells.fire, Spells.blizzard, Spells.meteor, Spells.heal],
                            [{'item': Collectables.potion, 'quantity': 4},
                             {'item': Collectables.elixir, 'quantity': 2},
                             {'item': Collectables.mystic, 'quantity': 1}], [], 'enchanted_garden')
            print_character(player, " Wizard")
        elif c_type == 2:
            icon = CharacterTypes.elf_him
            player = Person(icon, name, 750, 165, 110, 20,
                            [Spells.fire, Spells.heal, Spells.cure],
                            [{'item': Collectables.elixir, 'quantity': 5},
                             {'item': Collectables.potion, 'quantity': 2},
                             {'item': Collectables.super_potion, 'quantity': 1},
                             {'item': Collectables.bow, 'quantity': 30},
                             {'item': Collectables.knife, 'quantity': 3}], [], 'enchanted_garden')
            print_character(player, "n Elf")
        elif c_type == 3:
            icon = CharacterTypes.zombie_him
            player = Person(icon, name, 850, 50, 140, 25, [Spells.zombie_bite],
                            [{'item': Collectables.grenade, 'quantity': 5},
                             {'item': Collectables.bomb, 'quantity': 50},
                             {'item': Collectables.spider, 'quantity': 3}], [], 'enchanted_garden')
            print_character(player, " Zombie")
    elif player.level == 1:
        if c_type == 1:
            icon = CharacterTypes.wizzard_her
            player = Person(icon, name, 475, 260, 70, 27, [Spells.fire, Spells.blizzard, Spells.meteor, Spells.heal],
                            [{'item': Collectables.potion, 'quantity': 4},
                             {'item': Collectables.elixir, 'quantity': 2},
                             {'item': Collectables.mystic, 'quantity': 1}], [], 'enchanted_garden')
            print_character(player, " Witch")
        elif c_type == 2:
            icon = CharacterTypes.elf_her
            player = Person(icon, name, 725, 180, 105, 22,
                            [Spells.fire, Spells.heal, Spells.cure],
                            [{'item': Collectables.elixir, 'quantity': 5},
                             {'item': Collectables.potion, 'quantity': 2},
                             {'item': Collectables.super_potion, 'quantity': 1},
                             {'item': Collectables.bow, 'quantity': 30},
                             {'item': Collectables.knife, 'quantity': 3}], [], 'enchanted_garden')
            print_character(player, "n Elf")
        elif c_type == 3:
            icon = CharacterTypes.zombie_her
            player = Person(icon, name, 900, 50, 140, 23, [Spells.zombie_bite],
                            [{'item': Collectables.grenade, 'quantity': 5},
                             {'item': Collectables.bomb, 'quantity': 1},
                             {'item': Collectables.spider, 'quantity': 3}], [], 'enchanted_garden')
            print_character(player, " Zombie")

    print_message([f'Welcome {player.name}!', '', 'Once upon a time, we had a great Kingdom,', 'the Thunder Kingdom,', 'what was meant to keep peace and balance.',
                  "", "One day from the shadow dimension of illusions", "a mysterious Big Orb appeared! :(", "It corrupted our King's mind in order to ruin the Kingdom.",
                   f"Brave {player.name} the land needs you to bring back the peace,", "and restore the Thunder King's mind!"])
    return player, save


def tutorial(board, player):
    print_method = 1
    engine.put_player_on_board(board, player)

    snake = LevelItem('🐍', 'snake', True, 13, 14)
    bag = LevelItem('💰', 'bag', True, 3, 7)
    letter = LevelItem('📜', 'letter', True, 8, 5)

    level = True
    top = "TUTORIAL"
    message = "Info"
    while level:
        util.clear_screen()
        print_level(board, message, player, print_method, top)
        key = util.key_pressed()

        # MAIN CONTROL
        if key == 'q':
            levels.quit_game()
        elif key == "d":
            player.move_right(board)
        elif key == "s":
            player.move_down(board)
        elif key == "w":
            player.move_up(board)
        elif key == "a":
            player.move_left(board)
        elif key == "f":
            if letter.is_close(board, player):
                print_message(('W, A, S, D = move', 'F = Use item/FIGHT', 'T = Open Tools Bar/Talk', '', 'Good luck on your way!'))
            elif snake.is_close(board, player) and snake.on:
                top = "You can battle later"
                snake.turn_off(board)
            elif bag.is_close(board, player) and bag.on:
                message = 'You got the key!'
                bag.turn_off(board)
                board[3][14] = '  '
                board[3][16] = '  '
        elif key == 't':
            top = 'Your tools will be here!'
            util.clear_screen()
            print_level(board, message, player, print_method, top)
            util.key_pressed()

        if letter.is_close(board, player):
            message = "Letters sometimes are useful. Press F to read!"
        elif snake.is_close(board, player) and snake.on:
            message = "This is an enemy. Press F to fight!"
        elif bag.is_close(board, player) and bag.on:
            message = "This, and similar bags will help you on your way! Press F to loot!"
        elif player.pos_x == 3 and player.pos_y == 14:
            message = "This is the exit"
        elif player.pos_x == 3 and player.pos_y == 15:
            player.level = 'Gender'
            return
        else:
            message = "Info"
            top = "TUTORIAL"


def gender(board, player):
    print_method = 2
    player.icon = "@"
    engine.put_player_on_board(board, player)
    level = True
    top = "CHOOSE YOUR GENDER"
    message = "Press F to be a female"
    while level:
        util.clear_screen()
        print_level(board, message, player, print_method, top)
        key = util.key_pressed()

        # MAIN CONTROL
        if key == 'q':
            levels.quit_game()
        elif key == "d":
            player.move_right(board, '▒')
            player.move_right(board, '░')
            player.move_right(board, ' ')
        elif key == "s":
            player.move_down(board, '▒')
            player.move_down(board, '░')
        elif key == "w":
            player.move_up(board, '▒')
            player.move_up(board, '░')
        elif key == "a":
            player.move_left(board, '▒')
            player.move_left(board, '░')
        elif key == "f":
            if board[player.pos_x - 1][player.pos_y] == '▒':
                top = "You choose female"
                board[3][30] = ' '
                player.level = 1
            if board[player.pos_x - 1][player.pos_y] == '░':
                top = "You choose male"
                board[3][30] = ' '
                player.level = 2

        if board[player.pos_x - 1][player.pos_y] == '▒':
            message = "Press F to be a female"
        elif board[player.pos_x - 1][player.pos_y] == '░':
            message = "Press F to be a male"

        if player.pos_x == 3 and player.pos_y == 30:
            return


def char_type(board, player):
    print_method = 3
    player.icon += ' '
    engine.put_player_on_board(board, player)
    teleport_1 = LevelItem("🕳 ", "Teleport", True, 4, 28)
    teleport_2 = LevelItem("🕳 ", "Teleport", True, 13, 3)
    level = True
    top = "CHOOSE YOUR CHARACTER RACE"
    message = "Info"
    while level:
        util.clear_screen()
        print_level(board, message, player, print_method, top)
        key = util.key_pressed()
        # MAIN CONTROL
        if key == 'q':
            levels.quit_game()
        elif key == "d":
            player.move_right(board)
        elif key == "s":
            # TELEPORT
            if teleport_1.is_close(board, player):
                board[player.pos_x][player.pos_y] = '  '
                board[12][3] = player.icon
                player.pos_x = 12
                player.pos_y = 3
            elif teleport_2.is_close(board, player):
                board[player.pos_x][player.pos_y] = '  '
                board[3][28] = player.icon
                player.pos_x = 3
                player.pos_y = 28
            else:
                player.move_down(board)
        elif key == "w":
            player.move_up(board)
        elif key == "a":
            player.move_left(board)

        # OTHER CONTROLS
        if player.level == 1:
            if key == 't' and player.pos_x == 4 and player.pos_y == 7:
                print_message(['WITCH', '', 'Deep knowledge about magic,', 'with the power of the elements.', 'Fight against their foes', 'with great wisdom.'])
            elif key == 'f' and player.pos_x == 4 and player.pos_y == 7:
                top = 'You have chosen witch!'
                c_type = 1
                player.icon = CharacterTypes.wizzard_her
            elif key == 't' and player.pos_x == 8 and player.pos_y == 15:
                print_message(['ELF', '', 'Ranger of the light.', 'Eliminates all intruders', 'with quick decisions and sharp-mind', 'using items and elixirs.', 'Cures any wounds with the bless of light.'])
            elif key == 'f' and player.pos_x == 8 and player.pos_y == 15:
                top = 'You have chosen elf!'
                c_type = 2
                player.icon = CharacterTypes.elf_her
            elif key == 't' and player.pos_x == 7 and player.pos_y == 24:
                print_message(['ZOMBIE', '', 'Rawwww powwwwwerrrrr.', 'Arrrrghttttt'])
            elif key == 'f' and player.pos_x == 7 and player.pos_y == 24:
                top = 'You have chosen zombie!'
                c_type = 3
                player.icon = CharacterTypes.zombie_her
        elif player.level == 2:
            if key == 't' and player.pos_x == 4 and player.pos_y == 7:
                print_message(['WIZARD', '', 'Deep knowledge about magic,', 'with the power of the elements.', 'Fight against their foes', 'with great wisdom.'])
            elif key == 'f' and player.pos_x == 4 and player.pos_y == 7:
                top = 'You have chosen wizard!'
                c_type = 1
                player.icon = CharacterTypes.wizzard_him
            elif key == 't' and player.pos_x == 8 and player.pos_y == 15:
                print_message(['ELF', '', 'Ranger of the light.', 'Eliminates all intruders', 'with quick decisions and sharp-mind', 'using items and elixirs.', 'Cures any wounds with the bless of light.'])
            elif key == 'f' and player.pos_x == 8 and player.pos_y == 15:
                top = 'You have chosen elf!'
                c_type = 2
                player.icon = CharacterTypes.elf_him
            elif key == 't' and player.pos_x == 7 and player.pos_y == 24:
                print_message(['ZOMBIE', '', 'Rawwww powwwwwerrrrr.', 'Arrrrghttttt'])
            elif key == 'f' and player.pos_x == 7 and player.pos_y == 24:
                top = 'You have chosen zombie!'
                c_type = 3
                player.icon = CharacterTypes.zombie_him

        if key == 'f':
            if player.pos_x == 10 and player.pos_y == 24 or player.pos_x == 11 and player.pos_y == 25 or player.pos_x == 11 and player.pos_y == 26 or player.pos_x == 11 and player.pos_y == 27 or player.pos_x == 11 and player.pos_y == 28 or player.pos_x == 11 and player.pos_y == 29:
                save = 0
                return c_type, save
            elif player.pos_x == 10 and player.pos_y == 7 or player.pos_x == 11 and player.pos_y == 8 or player.pos_x == 11 and player.pos_y == 9 or player.pos_x == 11 and player.pos_y == 10 or player.pos_x == 11 and player.pos_y == 11 or player.pos_x == 11 and player.pos_y == 12:
                save = 1
                return c_type, save

        # POSITION CHECK
        if teleport_1.is_close(board, player) or teleport_2.is_close(board, player):
            message = "This is a teleport."
        elif player.pos_x == 4 and player.pos_y == 7:
            message = "Wizard - press F to select, T to talk"
        elif player.pos_x == 8 and player.pos_y == 15:
            message = "Elf - press F to select, T to talk"
        elif player.pos_x == 7 and player.pos_y == 24:
            message = "Zombie - press F to select, T to talk"
        elif player.pos_x == 10 and player.pos_y == 24 or player.pos_x == 11 and player.pos_y == 25 or player.pos_x == 11 and player.pos_y == 26 or player.pos_x == 11 and player.pos_y == 27 or player.pos_x == 11 and player.pos_y == 28 or player.pos_x == 11 and player.pos_y == 29:
            message = "Press F to start the adventure WITH OUT save."
        elif player.pos_x == 10 and player.pos_y == 7 or player.pos_x == 11 and player.pos_y == 8 or player.pos_x == 11 and player.pos_y == 9 or player.pos_x == 11 and player.pos_y == 10 or player.pos_x == 11 and player.pos_y == 11 or player.pos_x == 11 and player.pos_y == 12:
            message = "Press F to start the adventure and save your progress."
        else:
            message = "Info"


def play(player):
    while True:
        if player.level == 'enchanted_garden':
            board = engine.create_board(player)
            win, player = levels.enchanted_garden(board, player)
            if win == 1:
                player.level = 'wild_wilds'
                write_save_file('classes/save/player.pkl', player)
                continue
            else:
                player = read_save_file('classes/save/player.pkl')
                continue
        elif player.level == 'wild_wilds':
            board = engine.create_board(player)
            win, player = levels.wild_wilds(board, player)
            if win == 1:
                player.level = "castle_main_hall"
                write_save_file('classes/save/player.pkl', player)
                continue
            else:
                player = read_save_file('classes/save/player.pkl')
                continue
        elif player.level == "castle_main_hall":
            board = engine.create_board(player)
            win, player = levels.castle_main_hall(board, player)
            if win == 1:
                player.level = "castle_basement"
                write_save_file('classes/save/player.pkl', player)
                continue
            else:
                player = read_save_file('classes/save/player.pkl')
                continue
        elif player.level == "castle_basement":
            board = engine.create_board(player)
            win, player = levels.castle_basement(board, player)
            if win == 1:
                player.level = "castle_main_hall_2"
                write_save_file('classes/save/player.pkl', player)
                continue
            else:
                player = read_save_file('classes/save/player.pkl')
                continue
        elif player.level == "castle_main_hall_2":
            board = engine.create_board(player)
            win, player = levels.castle_main_hall_2(board, player)
            if win == 1:
                player.level = "tower"
                write_save_file('classes/save/player.pkl', player)
                continue
            else:
                player = read_save_file('classes/save/player.pkl')
                continue
        elif player.level == "tower":
            board = engine.create_board(player)
            win, player = levels.tower(board, player)
            if win == 1:
                player.level = "outro"
                continue
            else:
                player = read_save_file('classes/save/player.pkl')
                continue
        elif player.level == "outro":
            board = engine.create_board(player)
            outro(board, player)


def main():
    intro()
    player = read_save_file('classes/save/player.pkl')
    if not player:
        player, save = create_player()
        write_save_file('classes/save/player.pkl', player)
        play(player)
    else:
        print_character(player, " saved character")
        print('          *--*--*--*--*--*--*--*')
        load = input("    Load this player (Y/N)?")
        if load == "n" or load == "N" or load == "No":
            player, save = create_player()
            if save == 1:
                write_save_file('classes/save/player.pkl', player)
                play(player)
            else:
                play(player)
        else:
            play(player)


def play_outro(board, enemy):
    util.clear_screen()
    print('\n\n')
    ui.display_board(board, 9, enemy)
    time.sleep(1)

    for index in range(3):
        util.clear_screen()
        board[8][17] = '  '
        print('\n\n')
        ui.display_board(board, 9, enemy)
        time.sleep(0.5)
        util.clear_screen()
        board[8][17] = '👁 '
        print('\n\n')
        ui.display_board(board, 9, enemy)
        time.sleep(0.7)

    util.clear_screen()
    board[8][17] = '  '
    print('\n\n')
    ui.display_board(board, 9, enemy)
    time.sleep(1.4)

    board[8][17] = '🤴🏼'

    timer = [0.7, 0.4, 0.2, 0.1, 0.1, 0.1]
    for wait in timer:
        for index in range(5):
            display_mode = int('1' + str(index))
            util.clear_screen()
            print('\n\n')
            ui.display_board(board, display_mode, enemy)
            time.sleep(wait)
    time.sleep(1.5)

    messages = [['Cr', 'ea', 'te', 'd ', 'by', ': '], ['So', 'mo', 'sk', 'öv', 'i ', 'Be', 'nc', 'e ', '& '], ['Hu', 'be', 'r ', 'Ge', 'rg', 'ő '],
                ['  '], ['Sp', 'ec', 'ia', 'l ', 'Th', 'an', 'ks', ' t', 'o ', 'Co', 'de', 'Co', 'ol']]
    for row, message in enumerate(messages):
        for index, char in enumerate(message):
            x_pos = int('1' + str(row))
            board[x_pos][index + 2] = char
            util.clear_screen()
            print('\n\n')
            ui.display_board(board, 14, enemy)
            time.sleep(0.2)
        time.sleep(1)

    return board


def outro(board, player):
    engine.put_player_on_board(board, player)
    engine.put_enemy_on_board(board, Enemies.king)

    play_outro(board, Enemies.king)

    display_mode = 13
    level = True
    while level:
        display_mode += 1
        if display_mode == 15:
            display_mode = 10
        util.clear_screen()
        print('\n\n')
        ui.display_board(board, display_mode, Enemies.king)
        print('\n\n\n')

        key = util.key_pressed()

        # MAIN CONTROL
        if key == 'q':
            levels.quit_game()
        elif key == "d":
            player.move_right(board)
        elif key == "s":
            player.move_down(board)
        elif key == "w":
            player.move_up(board)
        elif key == "a":
            player.move_left(board)
        elif key == "t" and player.pos_x == 8 and player.pos_y == 16:
            print_message(['YOU', 'DID', 'IT!!! :)'])
        elif key == "i":
            print_character(player, " character")


if __name__ == '__main__':
    pygame.init()
    main()
