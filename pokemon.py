# File containing the class for various Pokemon
# Author: Luke Simone

# Imports
import random

from pkmnbase import Pokemon

class Bulbasaur(Pokemon):
    # Attributes / stats
    _name = 'Bulbasaur'
    _classification = 'Seed Pokemon'
    _pokedex_num = 1
    _type = 'Grass/Poison'
    _chance_is_male = .8814
    _capture_rate = 45
    _height = 0.7
    _weight = 6.9
    _base_egg_steps = 5120
    _ev_earned = {'spAtk':1}
    _base_stats = {'hp':45,'atk':49,'def':49,'spAtk':65,'spDef':65,'spd':45}
    _evolution = 0
    _abilities = ['Overgrow', 'Chlorophyll']

    def __init__(self):
        Pokemon.__init__(self)
        self._moves = ['Tackle', 'Growl']
        self._level = random.randint(4, 7)
