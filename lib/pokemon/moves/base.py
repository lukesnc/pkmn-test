# Base class for Pokemon moves
# Author: Luke Simone

from random import random

# Attack moves class
class Move(object):
    def __init__(self, num, name, mv_type, cat, pp, mv_pow, acc):
        self.number = num
        self.name = name
        self.type = mv_type  # ex. Grass
        self.category = cat  # Special/Physical/Status
        self.pp = pp
        self.power = mv_pow
        self.accuracy = acc

    def __str__(self):
        return str(self.name)

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
class StatusMove(Move):
    _effects = ['Stat Up', 'Stat Down', 'Status', 'Restore HP']
    def __init__(self, num, name, mv_type, pp, effect, acc):
        Move.__init__(self, num, name, mv_type, 'Status', pp, None, acc)
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

# if __name__ == '__main__':
#     _test(ember)
#     _test(thunder)
#     _test(poison_powder)
