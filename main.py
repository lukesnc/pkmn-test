#!/usr/bin/python3

# Pokemon combat and creature system test
# Author: Luke Simone

# Imports
import sys
from datetime import datetime
import logging

from pokemon import Bulbasaur
from trainer import Trainer
import items
import moves
import stats

# Global vars
LOG_PATH = './logs/pkmn-' + str(datetime.now()) + '.txt'
logging.basicConfig(filename=LOG_PATH, level=logging.INFO)

class Game():
    def __init__(self):
        print("Hello and welcome to the world of Pokemon!")
        input()
        print("Why don't you tell me a little bit about yourself.")
        input()
        me = Trainer('Luke', 'M')
        me.log_info()

        # Test with Bulbasaur
        boy = Bulbasaur()
        boy.catch('Great Ball') # CHANGE TO GREAT BALL ITEM
        boy.log_stats()

if __name__ == '__main__':
    g = Game()
    sys.exit()
