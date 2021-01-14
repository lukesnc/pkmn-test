# All Pokemon moves
# Author: Luke Simone

from .base import Move, StatusMove
from lib.pokemon.status import StatDown, Poison

pound = Move(1, 'Pound', 'Normal', 'Physical', 35, 40, 1.0)
tackle = Move(33, 'Tackle', 'Normal', 'Physical', 35, 40, 1.0)
growl = StatusMove(45, 'Growl', 'Normal', 40, StatDown('enemy', 'atk'), 1.0)
ember = Move(52, 'Ember', 'Fire', 'Special', 25, 40, 1.0)
poison_powder = StatusMove(
    77, 'Poison Powder', 'Poison', 35, Poison(is_bad=False), 0.75)
thunder = Move(87, 'Thunder', 'Electric', 'Special', 10, 110, 0.7)
