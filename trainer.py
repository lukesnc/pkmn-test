# File containing the class for the Trainer (the player)
# Author: Luke Simone

# Imports
from random import randint

class Trainer:
    name = ''
    gender = None
    has_pokedex = False
    secret_id = randint(1, 99999)
    trainer_id = randint(1, 99999) + secret_id * 65536
    bag = {}
    pokemon = []

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    @staticmethod
    def get_gender():
        g = input("Are you a boy or a girl? ").lower().strip()
        if g == 'boy':
            gender = 'M'
        elif g == 'girl':
            gender = 'F'
        else:
            print("That's not a gender!\n")
            Trainer.get_gender()
        choice = input("So, you're a " + g + "? [yes/no] ").lower().strip()
        if choice == 'yes':
            return gender
        else:
            print("Oh, okay.\n")
            Trainer.get_gender()

    @staticmethod
    def get_name():
        n = input("\nNow, what is your name? ").strip()
        if len(n) > 10:
            print("Try again.\n")
            Trainer.get_name()
        return n

    def receive_pokedex(self):
        self.has_pokedex = True

    def throw_ball(ball):
        pass
