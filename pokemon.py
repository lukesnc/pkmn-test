# Class file for Pokemon structure
# Author: Luke Simone

# Imports
from type import Type

class Pokemon:
    # Stats
    hp = None
    attack = None
    defense = None
    speed = None
    spAtk = None
    spDef = None

    # Attributes
    type = '???'
    gender = None
    ability = None
    nature = None
    moves = []
    pokedexNum = None

    # Leveling
    level = 1
    exp = 0

    # Battle status (asleep, confused, etc.)
    status = None
    heldItem = None
