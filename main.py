#!/usr/bin/python3

# Pokemon combat and creature system test
# Author: Luke Simone

# Imports
import sys
from datetime import datetime
import logging

from pokemon import Bulbasaur
from trainer import Trainer

# Global vars
LOG_PATH = './logs/pkmn-' + str(datetime.now()) + '.log'
logging.basicConfig(filename=LOG_PATH, level=logging.INFO)

# Main
class Game():
    def __init__(self):
        # Create trainer
        print("Hello and welcome to the world of Pokemon!")
        input()
        print("Why don't you tell me a little bit about yourself.")
        input()
        gender = Trainer.get_gender()
        name = Trainer.get_name()
        me = Trainer(name, gender)
        me.log_info()

        # Test with Bulbasaur
        boy = Bulbasaur()
        boy.catch('Master Ball')

        # "Battle"
        input()
        boy.gain_exp(150)

        boy.log_stats()

if __name__ == '__main__':
    g = Game()
    sys.exit()
