# Class file for Pokemon moves
# Author: Luke Simone

# Imports
from random import random

# Attack moves class
class Move(object):
    def __init__(self, num, name, type, cat, pp, pow, acc):
        self._number = num
        self._name = name
        self._type = type # ex. Grass
        self._category = cat # Special/Physical/Status
        self._pp = pp
        self._power = pow
        self._accuracy = acc

    def use(self):
        if random() < self._accuracy and self._pp > 0:
            self._pp -= 1
            return [self._type, self._category, self._power]
        else:
            if self._pp > 0:
                print("There's no PP left for this move!")
            else:
                print("The attack missed!")

# Status moves class
_effects = ['Stat Up', 'Stat Down', 'Status', 'Restore HP']
class StatusMove(Move):
    def __init__(self, num, name, type, pp, effect, acc):
        Move.__init__(self, num, name, type, 'Status', pp, None, acc)
        self._effect = effect

# Moves
pound = Move(1, 'Pound', 'Normal', 'Physical', 35, 40, 1.0)
tackle = Move(33, 'Tackle', 'Normal', 'Physical', 35, 40, 1.0)
ember = Move(52, 'Ember', 'Fire', 'Special', 25, 40, 1.0)
poison_powder = StatusMove(77, 'Poison Powder', 'Poison', 35, 'Posion', 0.75)
thunder = Move(87, 'Thunder', 'Electric', 'Special', 10, 110, 0.7)
