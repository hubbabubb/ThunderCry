class Item:
    def __init__(self, name, type, description, prop, on=True):
        self.name = name
        self.type = type
        self.description = description
        self.prop = prop
        self.maxprop = prop
        self.on = on


class Collectables:
    # POTIONS
    food = Item("🍗 Food", "potion", "Heals you by 50 HP", 50)
    potion = Item("💊 Potion", "potion", "Heals you by 100 HP", 100)
    hi_potion = Item("🍯 Hi-potion", "potion", "Heals you by 150 HP", 150)
    super_potion = Item("💎 Super potion", "potion", "Fill your HP to full", 99999)
    magic_drink_1 = Item("🍸 Cheap Dry Gin", "potion", "Heals you by 300 HP", 300)
    magic_drink_2 = Item("🍷 The second cheapest wine", "potion", "Heals you by 400 HP", 400)
    magic_drink_3 = Item("🍺 Walter's Beer", "potion", "Heals you by 500 HP", 500)
    magic_drink_4 = Item("🥃 Whiskey on the rocks", "potion", "Heals you by 600 HP", 600)
    magic_drink_5 = Item("🍹 Long Island", "potion", "Heals you by 700 HP", 700)
    magic_drink_6 = Item("🥤 Bloody Mary", "potion", "Heals you by 800 HP", 800)

    # ELIXIRS
    elixir = Item("⚱️ Elixir", "elixir", "+50 to your MP", 50)
    mega_elixir = Item("🏺 Mega Elixir", "elixir", "+100 to your MP", 100)
    super_elixir = Item("🥫 Super Elixir", "elixir", "+150 to your MP", 150)
    mystic = Item("🔮 Mystic Elixir", "elixir", "Fill your MP to full", 99999)

    vaccine = Item('💉 Vaccine', 'vaccine', 'Cures every kind of poison +100 HP', 100)

    # ATTACK
    bomb = Item("💣 BOMB", "attack", "Deals 500 HP damage", 500)
    sword = Item("🗡 Sword", "attack", "Deals 200 HP damage", 200)
    double_sword = Item("⚔️ Double Sword", "attack", "Deals 350 HP damage", 350)
    grenade = Item("💣 Grenade", "attack", "Deals 155 HP damage", 155)
    bow = Item("🏹 Bow", "attack", "Deals 105 HP damage", 105)
    knife = Item("🔪 Knife", "attack", "Deals 135 HP damage", 135)
    hammer = Item("🔨 Hammer", "attack", "Deals 135 HP damage", 135)
    wolf = Item('🐺 Wolf bite', "attack", "Deals 150 HP damage", 150)
    CD = Item("💿 CD", "attack", "Deals 200 HP damage", 200)
    gear = Item ('⚙️ Gear', "attack", "Deals 220 HP damage", 220)
    tusk = Item("Tusk", 'attack', "Deals 130 HP damage", 130)

    # POISONS
    mushroom = Item('🍄 Toxic Mushroom', 'poison', 'Take 5% damage from MAX HP for 3 rounds', 5)
    spider = Item('🕷 Spider bite', 'poison', 'Take 7% damage in every round', 7)
    deadly_poison = Item('💀 Deadly poison', 'poison', 'Take 10% damage from MAX HP for 3 rounds', 10)

    # TOOLS
    pick = Item('⛏ Pick', "tool", "Can be used to break something", 0)
    old_key = Item('🗝 Key', 'tool', 'Can be used for some doors', 0)
    boots = Item('👢 Boots-a', 'tool', 'Can be used to give to someone...', 0, False)
    CD_tool = Item("💾 floppy", "tool", "Use in computers", 50)

    # CHEAT
    noob = Item("🥊 instant_kill", "attack", "Kill your enemy", 99999)
    teleport = Item("🖲 teleport", "tool", "Use in computers", 1)
