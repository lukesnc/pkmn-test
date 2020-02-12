# File containing the class for various Pokemon
# Author: Luke Simone

# Imports
import random
from pokemon_base import Pokemon

class Bulbasaur(Pokemon):
    # Attributes
    name = "Bulbasaur"
    type = "Grass/Poison"
    gender = 'M' if random.random() < .875 else 'F'
    pkdx_num = 1
    evolution = 0

    # Base stats
    base_stats = {'hp':45,'atk':49,'def':49,'spAtk':65,'spDef':65,'spd':45}

    def __init__(self, nickname='', ball='Poke Ball'):
        self.exp = 264
        self.level = 100
        self.evs = {'hp':0,'atk':0,'def':0,'spAtk':0,'spDef':0,'spd':0}
        self.moves = ['Tackle', 'Growl']

        self.status = None
        self.held_item = None

        # Comes last
        super(Bulbasaur, self).__init__(nickname, ball)
