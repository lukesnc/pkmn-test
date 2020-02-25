# Class file for Pokemon moves
# Author: Luke Simone

# Imports
from random import random

from battlestatus import *

# Attack moves class
class Move(object):
    def __init__(self, num, name, type, cat, pp, pow, acc):
        self.number = num
        self.name = name
        self.type = type # ex. Grass
        self.category = cat # Special/Physical/Status
        self.pp = pp
        self.power = pow
        self.accuracy = acc

    def use(self):
        if random() < self.accuracy and self.pp > 0:
            self.pp -= 1
            return [self.type, self.category, self.power]
        else:
            if self.pp > 0:
                print("There's no PP left for this move!")
            else:
                print("The attack missed!")

# Status moves class
_effects = ['Stat Up', 'Stat Down', 'Status', 'Restore HP']
class StatusMove(Move):
    def __init__(self, num, name, type, pp, effect, acc):
        Move.__init__(self, num, name, type, 'Status', pp, None, acc)
        self.effect = effect

def _test(move):
    print("MOVE -", move.name)
    print("Number:", move.number)
    print("Type:", move.type)
    print("Category:", move.category)
    print("PP:", move.pp)
    print("Power:", move.power)
    print("Accuracy:", move.accuracy)
    try:
        print("Status effect:", move.effect)
    except:
        pass
    print("\n")

# Moves
pound = Move(1, 'Pound', 'Normal', 'Physical', 35, 40, 1.0)
tackle = Move(33, 'Tackle', 'Normal', 'Physical', 35, 40, 1.0)
growl = StatusMove(45, 'Growl', 'Normal', 40, StatDown('enemy','atk'), 1.0)
ember = Move(52, 'Ember', 'Fire', 'Special', 25, 40, 1.0)
poison_powder = StatusMove(77, 'Poison Powder', 'Poison', 35, Poison(), 0.75)
thunder = Move(87, 'Thunder', 'Electric', 'Special', 10, 110, 0.7)

if __name__ == '__main__':
    _test(ember)
    _test(thunder)
    _test(poison_powder)
