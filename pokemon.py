# Class file for Pokemon structure
# Author: Luke Simone

# Imports
from type import Type
from random import choice

class Pokemon(object):
    # Attributes
    name, nickname = ""
    pokedexNum = None
    type = '???'
    gender = None
    nature = random.choice(['Adamant','Bashful','Bold',
                            'Brave','Calm','Careful',
                            'Docile','Gentle','Hardy','Hasty',
                            'Impish','Jolly','Lax','Lonely',
                            'Mild','Modest','Naive','Naughty',
                            'Quiet','Quirky','Rash','Relaxed',
                            'Sassy','Serious','Timid'])
    ball = None

    # Base stats
    bHp, bAtk, bDef, bSpAtk, bSpDef, bSpd = None

    # Current stats
    hp, atk, def, spAtk, spDef, spd = None
    level = 1
    exp = 0
    evolution = 0
    moves = []

    # Battle status (asleep, confused, etc.)
    status = None
    heldItem = None

    def __init__(self, nn="", ball="Poke Ball", lvl=1):
        self.nickname = nn
        self.ball = ball
        self.level = lvl

    def show_stats(self):
        print("Name:", self.name)
        print("Nickname:", self.nickname)
        print("Pokedex #:", self.pokedexNum)
        print("Type(s):", self.type)
        print("Gender:", self.gender)
        print("Nature:", self.nature)
        print("Ball:", self.ball)
        print("HP:", self.hp)
        print("Attack:", self.attack)
        print("Defense:", self.defense)
        print("Sp. Attack:", self.spAtk)
        print("Sp. Defense:", self.spDef)
        print("Speed:", self.speed)
        print("Level:", self.level)
        print("Exp. Points:", self.exp)
        print("Moves:", self.moves)

    def fight(self):
        pass

    def run(self):
        pass
