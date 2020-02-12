#!/usr/bin/python3

# Pokemon combat and creature system test
# Author: Luke Simone

# Imports
import sys
from pokemon import Bulbasaur

# Global vars

# Main
class Start():
    def __init__(self):
        # Test with Bulbasaur
        boy = Bulbasaur('my guy', 'Great Ball')
        boy.show_stats()

        # "Battle"
        input()
        boy.gain_exp(150)


if __name__ == '__main__':
    s = Start()
    sys.exit()
