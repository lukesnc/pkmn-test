# Class file for Pokemon structure
# Author: Luke Simone

# Imports
import random
from datetime import datetime
import logging

from type import Type
from stats import *

class Pokemon(object):
    # Static class variables
    name = ''
    classification = ''
    pokedex_num = None
    type = '???'
    chance_is_male = 0.5
    capture_rate = 0
    height = 0 #m
    weight = 0 #kg
    base_egg_steps = 0
    ev_earned = {'stat':0}
    base_stats = {'hp':0,'atk':0,'def':0,'spAtk':0,'spDef':0,'spd':0}
    evolution = 0
    abilities = []

    def __init__(self):
        # Set stats
        self._nature = generate_nature()
        self._ability = random.choice(self.abilities)
        self._ivs = generate_ivs()
        self._gender = set_gender(self.chance_is_male)
        self._evs = {'hp':0,'atk':0,'def':0,'spAtk':0,'spDef':0,'spd':0}
        self._level = 1
        self._exp = None
        self._exp_to_next_lvl = None
        self._set_exp()
        self._moves = []
        self._nickname = None
        self._ball = 'Poke Ball'

        # Must come last
        self._stats = generate_stats(self.base_stats, self._ivs, self._evs,
                                     self._level, self._nature)

        # Trainer info
        self._date_met = datetime.now().strftime("%d-%m-%Y %H:%M")
        self._location_met = 'Route 1'
        self._characteristic = set_characteristic(self._ivs)

        # Battle status (asleep, confused, etc.)
        self._status = None
        self._held_item = None

    def _set_exp(self, extra_points=0):
        self._exp = pow(self._level, 3) + extra_points
        self._exp_to_next_lvl = pow(self._level + 1, 3) - self._exp

    def catch(self, ball):
        self._caught(ball)

    def _caught(self, ball):
        print("Successfully caught", self.name + '!')
        # Take catch args
        self._ball = ball
        choice = input("Give " + self.name + " a nickname? [yes/no] ").lower().strip()
        if choice == 'yes':
            nickname = input("Enter nickname: ").strip()
            if len(nickname) > 10:
                print("Try again.\n")
                self.catch()
            self._nickname = nickname

    def gain_exp(self, points):
        print(self.name, "gained", points, "Exp. Points!")
        self._exp += points
        input()
        if points > self._exp_to_next_lvl:
            self._level_up()
            extra = points - self._exp_to_next_lvl
            self._set_exp(extra)
        else:
            self._exp_to_next_lvl -= points

    def set_status(self):
        return self._status

    def set_held_item(self):
        return self._held_item

    def _level_up(self):
        self._level += 1
        print(self.name, "grew to Lv.", str(self._level) + "!")

        old_hp = self._stats['hp']
        old_atk = self._stats['atk']
        old_def = self._stats['def']
        old_spAtk = self._stats['spAtk']
        old_spDef = self._stats['spDef']
        old_spd = self._stats['spd']
        self._stats = generate_stats(self.base_stats, self._ivs, self._evs,
                                     self._level, self._nature)

        input()
        print("Max HP    +" + str(self._stats['hp'] - old_hp))
        print("Attack    +" + str(self._stats['atk'] - old_atk))
        print("Defense   +" + str(self._stats['def'] - old_def))
        print("Sp. Atk   +" + str(self._stats['spAtk'] - old_spAtk))
        print("Sp. Def   +" + str(self._stats['spDef'] - old_spDef))
        print("Speed     +" + str(self._stats['spd'] - old_spd))
        input()
        print("Max HP    " + str(self._stats['hp']))
        print("Attack    " + str(self._stats['atk']))
        print("Defense   " + str(self._stats['def']))
        print("Sp. Atk   " + str(self._stats['spAtk']))
        print("Sp. Def   " + str(self._stats['spDef']))
        print("Speed     " + str(self._stats['spd']))

    def log_stats(self):
        logging.info("POKEMON - " + str(self.name.upper()))
        logging.info("Name:           " + str(self.name))
        logging.info("Nickname:       " + str(self._nickname))
        logging.info("Pokedex #:      " + str(self.pokedex_num))
        logging.info("Class:          " + str(self.classification))
        logging.info("Height:         " + str(self.height) + 'm')
        logging.info("Weight:         " + str(self.weight) + 'kg')
        logging.info("Type(s):        " + str(self.type))
        logging.info("Gender:         " + str(self._gender))
        logging.info("Nature:         " + str(self._nature))
        logging.info("Ability:        " + str(self._ability))
        logging.info("Ball:           " + str(self._ball))
        logging.info("Max HP:         " + str(self._stats['hp']) + " iv: " + str(self._ivs['hp']))
        logging.info("Attack:         " + str(self._stats['atk']) + " iv: " + str(self._ivs['atk']))
        logging.info("Defense:        " + str(self._stats['def']) + " iv: " + str(self._ivs['def']))
        logging.info("Sp. Attack:     " + str(self._stats['spAtk']) + " iv: " + str(self._ivs['spAtk']))
        logging.info("Sp. Defense:    " + str(self._stats['spDef']) + " iv: " + str(self._ivs['spDef']))
        logging.info("Speed:          " + str(self._stats['spd']) + " iv: " + str(self._ivs['spd']))
        logging.info("Level:          " + str(self._level))
        logging.info("Exp. Points:    " + str(self._exp) + " To next: " + str(self._exp_to_next_lvl))
        logging.info("Moves:          " + str(self._moves))
        logging.info("Date met:       " + str(self._date_met))
        logging.info("Location met:   " + str(self._location_met))
        logging.info("Characteristic: " + str(self._characteristic))
        logging.info("\n")

    def fight(self):
        pass

    def run(self):
        pass

    def give_item(self, item):
        pass
