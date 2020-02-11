# Class file for Pokemon structure
# Author: Luke Simone

# Imports
from type import Type
from random import choice

class Pokemon:
    # Attributes
    name = ''
    nickname = ''
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
    bHp, bAtk, bDef, bSpAtk, bSpDef, bSpd = 6

    # Current stats
    hp, attack, defnse, spAtk, spDef, speed = 6
    level = 1
    exp = 0
    evolution = 0
    moves = []

    # Battle status (asleep, confused, etc.)
    status = None
    heldItem = None

    def __init__(self, name, pkdxNum, type, nickname='', gender=None, ball='Poke Ball', lvl=1, moves=[], item=None):
        self.name = name
        self.nickname = nickname
        self.pokedexNum = pkdxNum
        self.type = type
        self.gender = gender
        self.ball = ball
        self.level = lvl
        self.moves = moves
        self.heldItem = item

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
