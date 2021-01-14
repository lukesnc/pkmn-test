# All Pokemon moves
# Author: Luke Simone

from .base import Move, StatusMove
from lib.pokemon.status import StatDown, Poison

Pound = Move(1, 'Pound', 'Normal', 'Physical', 35, 40, 1.0)
Tackle = Move(33, 'Tackle', 'Normal', 'Physical', 35, 40, 1.0)
Growl = StatusMove(45, 'Growl', 'Normal', 40, StatDown('enemy', 'atk'), 1.0)
Ember = Move(52, 'Ember', 'Fire', 'Special', 25, 40, 1.0)
PoisonPowder = StatusMove(
    77, 'Poison Powder', 'Poison', 35, Poison(is_bad=False), 0.75)
Thunder = Move(87, 'Thunder', 'Electric', 'Special', 10, 110, 0.7)
