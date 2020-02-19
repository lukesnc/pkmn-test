# File containing the class for the Trainer (the player)
# Author: Luke Simone

# Imports
from random import randint
from datetime import datetime
import logging

LOG_PATH = './logs/trainer-' + str(datetime.now()) + '.log'
logger = logging.basicConfig(filename=LOG_PATH, level=logging.INFO)

class Trainer:
    name = ''
    gender = None
    has_pokedex = False
    secret_id = randint(1, 99999)
    trainer_id = randint(1, 99999) + secret_id * 65536
    bag = {}
    pokemon = []

    def __init__(self, name, gender):
        self._name = name
        self._gender = gender

    @staticmethod
    def get_gender():
        gender = None
        while gender != ('M' or 'F'):
            choice = input("Are you a boy or a girl? ").lower().strip()
            if choice == 'boy':
                gender = 'M'
            elif choice == 'girl':
                gender = 'F'
            else:
                print("That's not a gender!\n")
        while True:
            choice = input("So, you're a " + g + "? [yes/no] ").lower().strip()
            if choice == 'yes':
                return gender
            else:
                print("Oh, okay.\n")
                Trainer.get_gender()
                break

    @staticmethod
    def get_name():
        n = input("\nNow, what is your name? ").strip()
        if len(n) > 10:
            print("Try again.\n")
            Trainer.get_name()
        return n

    def log_info(self):
        pass

    def receive_pokedex(self):
        self.has_pokedex = True

    def throw_ball(ball):
        pass
