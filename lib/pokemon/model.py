# Class file for Pokemon structure
# Author: Luke Simone

import random
from datetime import datetime
import logging

from .types import NoneType
from .statgen import *


class Pokemon(object):
    """
    The base Pokemon class
    All Pokemon will derive from this as a subclass
    Includes methods for things that a Pokemon can do
    See notes.txt for more
    """
    # Static class variables
    _name = ''
    _classification = ''
    _pokedex_num = None
    _type = [NoneType]
    _chance_is_male = 0.5
    _height = 0  # m
    _weight = 0  # kg
    _base_egg_steps = 0
    _base_stats = {'hp': 0, 'atk': 0, 'def': 0,
                   'spAtk': 0, 'spDef': 0, 'spd': 0}
    _evolution = 0
    _abilities = []
    capture_rate = 0
    ev_earned = {'stat': 0}

    def __init__(self):
        # Set stats
        self.level = 1
        self.moves = []
        self._nickname = None

        self._nature = generate_nature()
        self.ability = random.choice(self._abilities)
        self.gender = set_gender(self._chance_is_male)

        self._ivs = generate_ivs()
        self._evs = {'hp': 0, 'atk': 0, 'def': 0,
                     'spAtk': 0, 'spDef': 0, 'spd': 0}
        self._exp = None
        self._exp_to_next_lvl = None
        self._set_exp()
        self.stats = generate_stats(self._base_stats, self._ivs, self._evs,
                                     self.level, self._nature)

        # Trainer info
        self._date_met = datetime.now().strftime("%d-%m-%Y %H:%M")
        self._location_met = 'Route 1'
        self._ball = 'Poke Ball'
        self._characteristic = set_characteristic(self._ivs)

        # Battle status (asleep, confused, etc.)
        self.status_condition = None
        self.held_item = None
        self.hp = self.stats['hp']

    def __str__(self):
        if self._nickname is not None:
            return self._nickname
        return self._name

    def __int__(self):
        return int(self._pokedex_num)

    def _set_exp(self, extra_points=0):
        self._exp = pow(self.level, 3) + extra_points
        self._exp_to_next_lvl = pow(self.level + 1, 3) - self._exp

    def catch(self, ball):
        self._caught(ball)

    def _caught(self, ball):
        print("Successfully caught", self._name + '!')
        # Take catch args
        self._ball = ball.name
        choice = input("Give " + self._name +
                       " a nickname? [yes/no] ").lower().strip()
        if choice == 'yes':
            nickname = input("Enter nickname: ").strip()
            if len(nickname) > 10:
                print("Try again.\n")
                self.catch(ball)
            self._nickname = nickname
            # Hands off to trainer

    def gain_exp(self, points):
        print(self._name, "gained", points, "Exp. Points!")
        self._exp += points
        input()
        if points > self._exp_to_next_lvl:
            self._level_up()
            extra = points - self._exp_to_next_lvl
            self._set_exp(extra)
        else:
            self._exp_to_next_lvl -= points

    def _level_up(self):
        self.level += 1
        print(self._name, "grew to Lv.", str(self.level) + "!")

        old_hp = self.stats['hp']
        old_atk = self.stats['atk']
        old_def = self.stats['def']
        old_sp_atk = self.stats['spAtk']
        old_sp_def = self.stats['spDef']
        old_spd = self.stats['spd']
        self.stats = generate_stats(self._base_stats, self._ivs, self._evs,
                                     self.level, self._nature)

        input()
        print("Max HP    +" + str(self.stats['hp'] - old_hp))
        print("Attack    +" + str(self.stats['atk'] - old_atk))
        print("Defense   +" + str(self.stats['def'] - old_def))
        print("Sp. Atk   +" + str(self.stats['spAtk'] - old_sp_atk))
        print("Sp. Def   +" + str(self.stats['spDef'] - old_sp_def))
        print("Speed     +" + str(self.stats['spd'] - old_spd))
        input()
        print("Max HP    " + str(self.stats['hp']))
        print("Attack    " + str(self.stats['atk']))
        print("Defense   " + str(self.stats['def']))
        print("Sp. Atk   " + str(self.stats['spAtk']))
        print("Sp. Def   " + str(self.stats['spDef']))
        print("Speed     " + str(self.stats['spd']))

    def log_stats(self):
        logging.info("POKEMON - %s", self._name.upper())
        logging.info("Name:           %s", self._name)
        logging.info("Nickname:       %s", self._nickname)
        logging.info("Pokedex #:      %s", self._pokedex_num)
        logging.info("Class:          %s", self._classification)
        logging.info("Height:         %s m", self._height)
        logging.info("Weight:         %s kg", self._weight)
        logging.info("Type(s):        %s", self._type)
        logging.info("Gender:         %s", self.gender)
        logging.info("Nature:         %s", self._nature)
        logging.info("Ability:        %s", self.ability)
        logging.info("Ball:           %s", self._ball)
        logging.info("Max HP:         %s iv: %s",
                     self.stats['hp'], self._ivs['hp'])
        logging.info("Attack:         %s iv: %s",
                     self.stats['atk'], self._ivs['atk'])
        logging.info("Defense:        %s iv: %s",
                     self.stats['def'], self._ivs['def'])
        logging.info("Sp. Attack:     %s iv: %s",
                     self.stats['spAtk'], self._ivs['spAtk'])
        logging.info("Sp. Defense:    %s iv: %s",
                     self.stats['spDef'], self._ivs['spDef'])
        logging.info("Speed:          %s iv: %s",
                     self.stats['spd'], self._ivs['spd'])
        logging.info("Level:          %s", self.level)
        logging.info("Exp. Points:    %s To next: %s",
                     self._exp, self._exp_to_next_lvl)
        logging.info("Moves:          %s", self.moves)
        logging.info("Date met:       %s", self._date_met)
        logging.info("Location met:   %s", self._location_met)
        logging.info("Characteristic: %s", self._characteristic)
        logging.info("\n")

    def fight(self):
        raise NotImplementedError

    def run(self):
        raise NotImplementedError

    def give_item(self, item):
        raise NotImplementedError
