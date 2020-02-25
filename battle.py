# Class file for battle system
# Author: Luke Simone

# Imports
import random

"""
The battle system

ELEMENTS
player:      The player's trainer object
palyer_pkmn: The player's first party Pokemon or whoever is switched
             into battle
enemy:       The enemy's trainer object
enemy_pkmn:  The enemy's first party Pokemon, whoever is switched in,
             or the wild Pokemon encountered

"""

class Battle:
    def __init__(self, player, enemy, type):
        self.player_pkmn = player._party[0]
        self.enemy_pkmn = enemy._party[0]

        if self.type == 'wild':
            pass
        elif self.type == 'battle':
            pass
        else:
            raise Exception
            print("error: not a battle type")
            exit(1)

    def __del__(self):
        print("Battle over.")

    def setup(self):
        print("Go", )

def _test():
    from trainer import Trainer
    from pokemon import Bulbasaur
    _p = Trainer('Test', 'F')
    _my_b = Bulbasaur()
    _p._party.append(_my_b)
    _e = Bulbasaur()
    _b = Battle(_p, _e, 'wild')
    del _b, _p, _my_b, _e

if __name__ == '__main__':
    _test()
