# Class file for battle system
# Author: Luke Simone

import random
import os

import lib.pokemon.status as status

class Battle(object):
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

    ACTIONS = ('Fight', 'Bag', 'Pokemon', 'Run')

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

        # Begin battle
        self.setup()
        while not self.finished:
            # Determine first turn
            order = [self.player_pkmn, self.enemy_pkmn]
            if self.player_pkmn.stats['spd'] < self.enemy_pkmn.stats['spd']:
                order.reverse()
            
            choice = self.get_choice()

            # Battle turns
            if choice == 'Fight':
                self.choose_fight()
            elif choice == 'Bag':
                self.choose_bag()
            elif choice == 'Pokemon':
                self.choose_pokemon()
            else:
                self.choose_run()


            # Check for certain status effects
            for pkmn in order:
                if pkmn.status == status.Poison:
                    pkmn.hp -= pkmn.hp * status.Poison.damage_percent

            # End of turn
            self.turn += 1

    def choose_fight(self):
        raise NotImplementedError

    def choose_bag(self):
        raise NotImplementedError

    def choose_pokemon(self):
        raise NotImplementedError

    def choose_run(self):
        raise NotImplementedError

    def display_battle_stats(self):
        for pkmn in (self.enemy_pkmn, self.player_pkmn):
            print(f"{str(pkmn)}{pkmn.gender} Lv{pkmn.level}")
            _status = "" if pkmn.status is None else f"({str(pkmn.status)})"
            print(f"{_status} HP: {pkmn.hp} / {pkmn.stats['hp']}\n")
        
    def get_choice(self):
        while True:
            self.display_battle_stats()
            print("\n[1]Fight   [2]Bag\n[3]Pokemon [4]Run\n")
            try:
                c = int(input(f"What will {str(self.player_pkmn)} do? ").strip())
                if c > 4 or c < 1:
                    raise Exception
                return self.ACTIONS[c]
            except:
                os.system('clear')

    def setup(self):
        os.system('clear')
        print("\n==========================")
        print(f"Go {str(self.player_pkmn)}!\n")

    def __del__(self):
        print("Battle over.")


# Test battle
def test(pkmn):
    from lib.trainer import Trainer
    from lib.pokemon import Bulbasaur
    _p = Trainer('Test', 'F')
    _my_b = pkmn
    _p.party.append(_my_b)
    _e = Bulbasaur()
    _b = Battle(_p, _e, wild=True)
    del _b, _p, _my_b, _e
