# File containing the class for various Pokemon
# Author: Luke Simone

# Imports
import random

from pkmnbase import Pokemon

class Bulbasaur(Pokemon):
    # Attributes / stats
    name = 'Bulbasaur'
    classification = 'Seed Pokemon'
    pokedex_num = 1
    type = 'Grass/Poison'
    chance_is_male = .8814
    capture_rate = 45
    height = 0.7
    weight = 6.9
    base_egg_steps = 5120
    ev_earned = {'spAtk':1}
    base_stats = {'hp':45,'atk':49,'def':49,'spAtk':65,'spDef':65,'spd':45}
    evolution = 0
    abilities = ['Overgrow', 'Chlorophyll']

    def __init__(self):
        Pokemon.__init__(self)
        self._moves = ['Tackle', 'Growl']
        self._level = random.randint(4, 7)
