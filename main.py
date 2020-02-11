#!/usr/bin/python3

# Pokemon combat and creature system test
# Author: Luke Simone

# Imports
import sys
from bulbasaur import Bulbasaur

# Global vars

# Main
class Start():
    def __init__(self):
        # Test with Bulbasaur
        bro = Bulbasaur("my man")
        bro.show_stats()


if __name__ == '__main__':
    s = Start()
    sys.exit()
