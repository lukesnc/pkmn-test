# Class file for Pokemon structure
# Author: Luke Simone

# Imports
from type import Type

class Pokemon:
    # Attributes
    name = ""
    nickname = ""
    type = '???'
    gender = None
    moves = []
    nature = None
    pokedexNum = None

    # Stats
    hp = None
    attack = None
    defense = None
    spAtk = None
    spDef = None
    speed = None

    # Leveling
    level = 1
    exp = 0
    evolution = 0

    # Battle status (asleep, confused, etc.)
    status = None
    heldItem = None

    def __init__(self, nickname=""):
        self.nickname = nickname


    def show_stats(self):
        print("Name:", self.name)
        print("Nickname:", self.nickname)
        print("Type(s):", self.type)
        print("Gender:", self.gender)
        print("Moves:", self.moves)
        print("Nature:", self.nature)
        print("Pokedex #:", self.pokedexNum)
        print("HP:", self.hp)
        print("Attack:", self.attack)
        print("Defense:", self.defense)
        print("Sp. Attack:", self.spAtk)
        print("Sp. Defense:", self.spDef)
        print("Speed:", self.speed)
        print("Level:", self.level)
        print("Exp. Points:", self.exp)

    def fight(self):
        pass

    def run(self):
        pass
