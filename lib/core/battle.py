# Class file for battle system
# Author: Luke Simone

# Imports
import random

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
    
    def __init__(self, player, enemy, battle_type):
        self.player = player
        self.enemy = enemy
        self.type = battle_type
        self.player_pkmn = player.party[0]
        try:
            self.enemy_pkmn = enemy.party[0]
        except:
            self.enemy_pkmn = enemy

        if self.type == 'wild':
            pass
        elif self.type == 'battle':
            pass
        else:
            raise Exception("error: not a battle type")
        

    def __del__(self):
        print("Battle over.")

    def setup(self):
        print("Go", self.player_pkmn.get_name())


# Test battle
def _test():
    from lib.core.trainer import Trainer
    from lib.db.pokemon import Bulbasaur
    _p = Trainer('Test', 'F')
    _my_b = Bulbasaur()
    _p.party.append(_my_b)
    _e = Bulbasaur()
    _b = Battle(_p, _e, 'wild')
    del _b, _p, _my_b, _e

if __name__ == '__main__':
    _test()
