# Class file for battle system
# Author: Luke Simone

import random

from lib.pokemon.status import *

class Battle:
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

    def __init__(self, player, enemy, wild=True):
        self.player = player
        self.enemy = enemy
        self.wild = wild
        self.player_pkmn = player.party[0]
        try:
            self.enemy_pkmn = enemy.party[0]
        except AttributeError:
            self.enemy_pkmn = enemy
        self.finished = False
        self.turn = 0

    def fight(self):
        self.setup()
        while not self.finished:
            # Determine first turn
            order = [self.player_pkmn, self.enemy_pkmn]
            if self.player_pkmn.stats['spd'] < self.enemy_pkmn.stats['spd']:
                order.reverse()

            # Battle turns
            raise NotImplementedError



            # Check for certain status effects
            for pkmn in order:
                if pkmn.status == Poison:
                    pkmn.hp -= pkmn.hp * Poison.damage_percent

            # End of turn
            self.turn += 1

    def display_options(self):
        print()

    def setup(self):
        print("Go", self.player_pkmn.get_name())

    def __del__(self):
        print("Battle over.")


# Test battle
def test():
    from lib.trainer import Trainer
    from lib.pokemon import Bulbasaur
    _p = Trainer('Test', 'F')
    _my_b = Bulbasaur()
    _p.party.append(_my_b)
    _e = Bulbasaur()
    _b = Battle(_p, _e, wild=True)
    del _b, _p, _my_b, _e
