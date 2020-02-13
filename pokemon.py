# File containing the class for various Pokemon
# Author: Luke Simone

# Imports
import random
from pokemon_base import Pokemon

class Bulbasaur(Pokemon):
    # Attributes / stats
    # Redo this
    BASE_STATS = {'hp':45,'atk':49,'def':49,'spAtk':65,'spDef':65,'spd':45}

    def __init__(self):
        level = random.randint(4, 7)
        super(Bulbasaur, self).__init__(level)
        self._moves = ['Tackle', 'Growl']
