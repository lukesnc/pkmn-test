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
        self.player_pkmn = player._party
        self.enemy_pkmn = enemy._party

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
    p = Trainer('Test', 'F')
    my_b = Bulbasaur()
    p._party.append(my_b)
    e = Bulbasaur()
    b = Battle(p, e, 'wild')
    del b, p, my_b, e

if __name__ == '__main__':
    _test()
