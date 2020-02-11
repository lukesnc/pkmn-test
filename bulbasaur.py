# File containing the class for Pokemon Bulbasaur
# Author: Luke Simone

# Imports
from pokemon import Pokemon
from random import random

class Bulbasaur(Pokemon):
    # Attributes
    name = "Blulbasaur"
    nickname = ""
    type = "Grass/Poison"
    gender = 'M' if random() < .875 else 'F'
    moves = ['Tackle', 'Growl']
    nature = "Adamant"
    pokedexNum = 1

    # Stats
    hp = 21
    attack = 12
    defense = 11
    spAtk = 11
    spDef = 13
    speed = 11

    # Leveling
    level = 5
    exp = 264
    evolution = 0

    # Battle status (asleep, confused, etc.)
    status = None
    heldItem = None
