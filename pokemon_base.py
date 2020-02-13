# Class file for Pokemon structure
# Author: Luke Simone

# Imports
import random
from type import Type

# For calculating exp. points


class Pokemon(object):
    # Static class variables
    NAME = ''
    CLASSIFICATION = ''
    POKEDEX_NUM = None
    TYPE = '???'
    CHANCE_IS_MALE = 0.5
    CAPTURE_RATE = 0
    HEIGHT = 0 #m
    WEIGHT = 0 #kg
    BASE_EGG_STEPS = 0
    EV_EARNED = {'stat':0}
    BASE_STATS = {'hp':0,'atk':0,'def':0,'spAtk':0,'spDef':0,'spd':0}
    EVOLUTION = 0

    def __init__(self, level):
        # Set stats
        self._nature = self._get_nature()
        self._ivs = {
            'hp':random.randint(0,32),
            'atk':random.randint(0,32),
            'def':random.randint(0,32),
            'spAtk':random.randint(0,32),
            'spDef':random.randint(0,32),
            'spd':random.randint(0,32)
        }

        self._gender = self._get_gender(CHANCE_IS_MALE)
        self._evs = {'hp':0,'atk':0,'def':0,'spAtk':0,'spDef':0,'spd':0}
        self._level = level
        self._exp = None
        self._exp_to_next_lvl = None
        self._set_exp()
        self._moves = []
        self._nickname = None
        self._ball = None

        # Must come last
        self._stats = {
            'hp': self._generate_stat('hp'),
            'atk': self._generate_stat('atk'),
            'def': self._generate_stat('def'),
            'spAtk': self._generate_stat('spAtk'),
            'spDef': self._generate_stat('spDef'),
            'spd': self._generate_stat('spd')
        }

        # Battle status (asleep, confused, etc.)
        self.status = None
        self.held_item = None


    def _get_nature(self):
        NATURES = ['Hardy','Lonely','Brave','Adamant','Naughty',
                   'Bold','Docile','Relaxed','Impish','Lax','Timid',
                   'Hasty','Serious','Jolly','Naive','Modest','Mild',
                   'Quiet','Bashful','Rash','Calm','Gentle','Sassy',
                   'Careful','Quirky']
        return random.choice(NATURES)

    # Sets stats based on IVs and base stats
    # Formulas found at bulbapedia.bulbagarden.net/wiki/Individual_values
    def _generate_stat(self, stat):
        if stat == 'hp':
            return int(((2 * self.BASE_STATS['hp'] + self._ivs['hp'] + int(self.evs['hp']/4)) * self._level) / 100) + self._level + 10
        else:
            return int((int(((2 * self.BASE_STATS[stat] + self._ivs[stat] + int(self.evs[stat]/4)) * self._level) / 100) + 5) * self._get_nature_mod(stat))

    def _get_gender(self, chance_is_male=0.5):
        if random.random() < chance_is_male:
            return 'M'
        else:
            return 'F'

    def _get_nature_mod(self, stat):
        NATURE_MOD_INCREASE = 1.10
        NATURE_MOD_DECREASE = 0.90
        NATURE_MOD_NONE = 1.0

        if stat == 'atk':
            if self._nature in NATURES[1:5]:
                return NATURE_MOD_INCREASE
            elif self._nature in NATURES[5::5]:
                return NATURE_MOD_DECREASE
            else:
                return NATURE_MOD_NONE

        elif stat == 'def':
            if self._nature in NATURES[5:10] and self._nature != 'Docile':
                return NATURE_MOD_INCREASE
            elif self._nature in ['Lonely','Hasty','Mild','Gentle']:
                return NATURE_MOD_DECREASE
            else:
                return NATURE_MOD_NONE

        elif stat == 'spd':
            if self._nature in NATURES[10:15] and self._nature != 'Serious':
                return NATURE_MOD_INCREASE
            elif self._nature in ['Brave','Relaxed','Quiet','Sassy']:
                return NATURE_MOD_DECREASE
            else:
                return NATURE_MOD_NONE

        elif stat == 'spAtk':
            if self._nature in NATURES[15:20] and self._nature != 'Bashful':
                return NATURE_MOD_INCREASE
            elif self._nature in ['Adamant','Impish','Jolly','Careful']:
                return NATURE_MOD_DECREASE
            else:
                return NATURE_MOD_NONE

        elif stat == 'spDef':
            if self._nature in NATURES[20:24]:
                return NATURE_MOD_INCREASE
            elif self._nature in NATURES[4::5] and self._nature != 'Quirky':
                return NATURE_MOD_DECREASE
            else:
                return NATURE_MOD_NONE

    def _set_exp(self, extra_points=0):
        EXP_MOD = 3

        self._exp = pow(self._level, EXP_MOD) + extra_points
        self._exp_to_next_lvl = pow(self._level + 1, EXP_MOD) - self._exp

    def _caught(self, ball):
        print("Successfully caught", self.name + '!')
        # Take catch args
        self._ball = ball
        choice = input("Give", self.name, "a nickname? [yes/no] ").lower().strip()
        if choice == 'yes':
            nickname = input("Enter nickname: ").strip()
            if len(nickname) > 10:
                print("Try again.\n")
                self.catch()
            self._nickname = nickname

    def catch(self, ball):
        self._caught(ball)


    def gain_exp(self, points):
        print(self.name, "gained", points, "Exp. Points!")
        self._exp += points
        input()
        if points > self._exp_to_next_lvl:
            self._level_up()
            extra = points - self._exp_to_next_lvl
            self._set_exp(extra)
        else:
            self._exp_to_next_lvl -= points

    def _level_up(self):
        self._level += 1
        print(self.name, "grew to Lv.", str(self._level) + "!")

        old_hp = self._stats['hp']
        old_atk = self._stats['atk']
        old_def = self._stats['def']
        old_spAtk = self._stats['spAtk']
        old_spDef = self._stats['spDef']
        old_spd = self._stats['spd']
        self._set_stats()

        input()
        print("Max HP    +" + str(self._stats['hp'] - old_hp))
        print("Attack    +" + str(self._stats['atk'] - old_atk))
        print("Defense   +" + str(self._stats['def'] - old_def))
        print("Sp. Atk   +" + str(self._stats['spAtk'] - old_spAtk))
        print("Sp. Def   +" + str(self._stats['spDef'] - old_spDef))
        print("Speed     +" + str(self._stats['spd'] - old_spd))
        input()
        print("Max HP    " + str(self._stats['hp']))
        print("Attack    " + str(self._stats['atk']))
        print("Defense   " + str(self._stats['def']))
        print("Sp. Atk   " + str(self._stats['spAtk']))
        print("Sp. Def   " + str(self._stats['spDef']))
        print("Speed     " + str(self._stats['spd']))

    def show_stats(self):
        print("Name:       ", self.name)
        print("Nickname:   ", self._nickname)
        print("Pokedex #:  ", self.pokedex_num)
        print("Class:      ", self.classification)
        print("Height:     ", str(self.height) + 'm')
        print("Weight:     ", str(self.weight) + 'kg')
        print("Type(s):    ", self.type)
        print("Gender:     ", self._gender)
        print("Nature:     ", self._nature, '(' + str(NATURES.index(self._nature)) + ')')
        print("Ball:       ", self._ball)
        print("Max HP:     ", self._stats['hp'], 'IV:', self._ivs['hp'], 'Base:', self.BASE_STATS['hp'])
        print("Attack:     ", self._stats['atk'], 'IV:', self._ivs['atk'], 'Base:', self.BASE_STATS['atk'])
        print("Defense:    ", self._stats['def'], 'IV:', self._ivs['def'], 'Base:', self.BASE_STATS['def'])
        print("Sp. Attack: ", self._stats['spAtk'], 'IV:', self._ivs['spAtk'], 'Base:', self.BASE_STATS['spAtk'])
        print("Sp. Defense:", self._stats['spDef'], 'IV:', self._ivs['spDef'], 'Base:', self.BASE_STATS['spDef'])
        print("Speed:      ", self._stats['spd'], 'IV:', self._ivs['spd'], 'Base:', self.BASE_STATS['spd'])
        print("Level:      ", self._level)
        print("Exp. Points:", self._exp, "To next:", self._exp_to_next_lvl)
        print("Moves:      ", self._moves)

    def fight(self):
        pass

    def run(self):
        pass

    def give_item(self, item):
        pass
