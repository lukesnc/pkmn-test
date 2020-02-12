# File containing the class for Pokemon Bulbasaur
# Author: Luke Simone

# Imports
from pokemon import Pokemon
from random import random

class Bulbasaur(Pokemon):
    # Attributes
    name = "Blulbasaur"
    type = "Grass/Poison"
    gender = 'M' if random() < .875 else 'F'
    pokedexNum = 1
    evolution = 0

    # Base stats
    base_stats = {'hp':0,'atk':0,'def':0,'spAtk':0,'spDef':0,'spd':0}

    def __init__(self):
        # Leveling
        self.level = 5
        self.exp = 264

        # Battle status (asleep, confused, etc.)
        self.status = None
        self.held_item = None
