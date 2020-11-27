import random


class Spell:
    def __init__(self, name, cost, dmg, type):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.maxdmg = dmg
        self.type = type

    def generate_damage(self):
        return random.randrange(self.dmg - 5, self.dmg + 5)


class Spells:
    fire = Spell("🔥 Fire", 30, 120, "black")
    thunder = Spell("⛈️ Thunder", 55, 185, "black")
    blizzard = Spell("❄️ Blizzard", 85, 275, "black")
    meteor = Spell("☄️ Meteor", 165, 450, "black")

    electricity = Spell("⚡️ Electricity", 100, 400, "black")
    quake = Spell("💥 Earth quake", 120, 350, "black")
    hurricane = Spell('🌪 Hurricane', 200, 600, 'black')

    zombie_bite = Spell('💋 Zombie "kiss"', 50, 150, 'zombie')
    vampire_bite = Spell('🧛🏻‍♂️ Vampire bite', 50, 220, 'zombie')

    curse_of_weakness = Spell('💀 Curse of Weakness', 60, 1, 'curse')
    bless = Spell('☀️ Bless of the King', 1, 1, 'bless')

    heal = Spell("✨ Flash heal", 25, 150, "white")
    cure = Spell("🌟 Greater heal", 55, 400, "white")

    repair = Spell("🔧 Self Repair", 50, 250, "white")