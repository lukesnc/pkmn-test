# File containing the class for the Trainer (the player)
# Author: Luke Simone

# Imports
from random import randint
import logging

import lib.db.items as itm

class Trainer:
    """This is what the player plays as; a Pokemon Trainer"""
    
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self._has_pokedex = False
        self.__secret_id = randint(0, 99999)
        self._trainer_id = randint(0, 65535)
        self.final_id = self._trainer_id + self.__secret_id * 65536
        # Bag and pockets {item: quantity}
        self.bag = {'Items': {},
                    'Medicine': {itm.potion:1},
                    'Balls': {itm.poke_ball:5},
                    'Battle Items': {},
                    'Key Items': ['Town Map']}
        self.party = []

    def __str__(self):
        return str(self.name)

    def _use_item(self, category, item):
        self.bag[category][item] -= 1
        if self.bag[category][item] == 0:
            self.bag[category].pop(item)

    def _throw_ball(self, ball, pkmn):
        # Check that trainer has one of the desired ball
        if ball in self.bag['Balls'] and self.bag['Balls'][ball] > 0:
            self._use_item('Balls', ball)
            # If catch successful
            # if boy.use()
            return True
        # Fail
        return False


    def throw_ball(self, ball, pkmn):
        if self._throw_ball(ball, pkmn):
            return True
        return False

    def add_to_party(self, pkmn):
        self.party.append(pkmn)
        print(pkmn.get_name(), "has been added to your party.")

    def receive_pokedex(self):
        self._has_pokedex = True

    def log_info(self):
        logging.info("TRAINER")
        logging.info("Name:          %s", self.name)
        logging.info("Gender:        %s", self.gender)
        logging.info("Has Pokedex:   %s", self._has_pokedex)
        logging.info("Trainer ID:    %s", self.final_id)
        logging.info("Bag:           %s", self.bag)
        logging.info("Party Pokemon: %s", self.party)
        logging.info("\n")

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
