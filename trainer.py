# File containing the class for the Trainer (the player)
# Author: Luke Simone

# Imports
from random import randint
import logging

class Trainer:
    def __init__(self, name, gender):
        self._name = name
        self._gender = gender
        self._has_pokedex = False
        self._secret_id = randint(1, 99999)
        self._trainer_id = randint(1, 99999) + self._secret_id * 65536
        self._bag = {}
        self._pokemon = []

    @staticmethod
    def get_gender():
        gender = None
        while gender is None:
            g = input("Are you a boy or a girl? ").lower().strip()
            if g == 'boy':
                gender = 'M'
            elif g == 'girl':
                gender = 'F'
            else:
                print("That's not a gender!\n")
        while True:
            choice = input("So, you're a " + g + "? [yes/no] ")
            if choice.lower().strip() == 'yes':
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
        logging.info("TRAINER")
        logging.info("Name:          " + str(self._name))
        logging.info("Gender:        " + str(self._gender))
        logging.info("Has Pokedex:   " + str(self._has_pokedex))
        logging.info("Trainer ID:    " + str(self._trainer_id))
        logging.info("Bag:           " + str(self._bag))
        logging.info("Party Pokemon: " + str(self._pokemon))
        logging.info("\n")

    def receive_pokedex(self):
        self.has_pokedex = True

    def throw_ball(ball):
        pass
