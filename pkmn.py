#!/usr/bin/python3
# Pokemon combat and creature system test
# Author: Luke Simone

# Imports
import sys
if sys.version_info < (3, 0):
    sys.stderr.write("Requires Python 3.x\n")
    sys.exit(1)

from lib.db.pokemon import Bulbasaur
from lib.core.trainer import Trainer
import lib.db.items as itm
import lib.db.moves
import lib.core.stats
import lib.core.battle as bttl

class Game():
    def __init__(self):
        print("Hello and welcome to the world of Pokemon!")
        input()
        print("Why don't you tell me a little bit about yourself.")
        input()
        # name, gender = Trainer.get_name(), Trainer.get_gender()
        # player = Trainer(name, gender)
        me = Trainer('Luke', 'M')

        # Test with Bulbasaur
        boy = Bulbasaur()
        if me.throw_ball(itm.poke_ball, boy):
            boy.catch(itm.ultra_ball)
        # boy.log_stats()

        # Test battle
        bttl.test()

if __name__ == '__main__':
    try:
        g = Game()
    except KeyboardInterrupt:
        sys.stderr.write("\nQuitting...\n")
    sys.exit()
