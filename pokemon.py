# Class file for Pokemon structure
# Author: Luke Simone

# Imports
from type import Type
from random import choice, randint

# Consts
NATURES = ['Hardy','Lonely','Brave','Adamant','Naughty',
           'Bold','Docile','Relaxed','Impish','Lax','Timid',
           'Hasty','Serious','Jolly','Naive','Modest','Mild',
           'Quiet','Bashful','Rash','Calm','Gentle','Sassy',
           'Careful','Quirky']
NATURE_MOD_INCREASE = 1.10
NATURE_MOD_DECREASE = 0.90
NATURE_MOD_NONE = 1.0

class Pokemon(object):
    # Attributes
    name = ''
    pkdx_num = None
    type = '???'
    gender = None
    nature = choice(NATURES)

    # Attributes the player affects
    nickname = ''
    ball = None

    # Base stats
    base_stats = {'hp':0,'atk':0,'def':0,'spAtk':0,'spDef':0,'spd':0}
    ivs = {'hp':randint(0,32),'atk':randint(0,32),'def':randint(0,32),'spAtk':randint(0,32),'spDef':randint(0,32),'spd':randint(0,32)}

    # Current stats
    stats = {'hp':0,'atk':0,'def':0,'spAtk':0,'spDef':0,'spd':0}
    evs = {'hp':0,'atk':0,'def':0,'spAtk':0,'spDef':0,'spd':0}
    level = 1
    exp = 1
    evolution = 0
    moves = []

    # Battle status (asleep, confused, etc.)
    status = None
    held_item = None

    def __init__(self, nickname='', ball='Poke Ball'):
        self.__set_stats()
        self.nickname = nickname
        self.ball = ball

    # Sets stats based on IVs and base stats
    def __set_stats(self):
        # Set hp
        self.stats['hp'] = int((((2 * self.base_stats['hp'] + self.ivs['hp'] + (self.evs['hp']/4) * self.level) / 100) + self.level + 10))

        # Set the rest
        for stat in self.stats:
            if stat != 'hp':
                self.stats[stat] = int(((((2 * self.base_stats[stat] + self.ivs[stat] + (self.evs[stat]/4) * self.level) / 100) + 5) * self.__nature_mod(stat)))

    def __nature_mod(self, stat):
        if stat == 'atk':
            if self.nature in NATURES[1:5]:
                return NATURE_MOD_INCREASE
            elif self.nature in NATURES[5::5]:
                return NATURE_MOD_DECREASE

        elif stat == 'def':
            if self.nature in NATURES[5:10] and not 'Docile':
                return NATURE_MOD_INCREASE
            elif self.nature in []:
                return NATURE_MOD_DECREASE

        elif stat == 'spd':
            if self.nature in NATURES[10:15] and not 'Serious':
                return NATURE_MOD_INCREASE
            elif self.nature in []:
                return NATURE_MOD_DECREASE

        elif stat == 'spAtk':
            if self.nature in NATURES[15:20] and not 'Bashful':
                return NATURE_MOD_INCREASE
            elif self.nature in []:
                return NATURE_MOD_DECREASE

        elif stat == 'spDef':
            if self.nature in NATURES[20:24]:
                return NATURE_MOD_INCREASE
            elif self.nature in []:
                return NATURE_MOD_DECREASE

        else:
            return NATURE_MOD_NONE

    def gain_exp(self, points):
        pass

    def __level_up(self):
        pass

    def give_item(self, item):
        pass

    def show_stats(self):
        print("Name:", self.name)
        print("Nickname:", self.nickname)
        print("Pokedex #:", self.pkdx_num)
        print("Type(s):", self.type)
        print("Gender:", self.gender)
        print("Nature:", self.nature, '(' + str(self.NATURES.index(self.nature)) + ')')
        print("Ball:", self.ball)
        print("HP:", self.stats['hp'])
        print("Attack:", self.stats['atk'])
        print("Defense:", self.stats['def'])
        print("Sp. Attack:", self.stats['spAtk'])
        print("Sp. Defense:", self.stats['spDef'])
        print("Speed:", self.stats['spd'])
        print("Level:", self.level)
        print("Exp. Points:", self.exp)
        print("Moves:", self.moves)

    def fight(self):
        pass

    def run(self):
        pass
