#!/usr/bin/python3

# Pokemon combat and creature system test
# Author: Luke Simone

# Imports
import sys
from pokemon import Bulbasaur
from trainer import Trainer

# Global vars

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

        # Test with Bulbasaur
        boy = Bulbasaur()
        boy.catch('cummy bear', 'Master Ball')

        # "Battle"
        input()
        boy.gain_exp(150)

if __name__ == '__main__':
    g = Game()
    sys.exit()
