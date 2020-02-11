#!/usr/bin/python3

# Pokemon combat and creature system test
# Author: Luke Simone

# Imports
import sys
from random import random
from pokemon import Pokemon

# Global vars

# Main
class Start():
    def __init__(self):
        # Test with Bulbasaur
        boy = Pokemon('my man', 'Master Ball')
        boy.show_stats()


if __name__ == '__main__':
    s = Start()
    sys.exit()
