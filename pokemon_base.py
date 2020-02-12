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
EXP_MOD = 3

class Pokemon(object):
    # Attributes
    name = ''
    pokedex_num = None
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
    exp = 0
    exp_to_next_lvl = 0
    evolution = 0
    moves = []

    # Battle status (asleep, confused, etc.)
    status = None
    held_item = None

    def __init__(self, nickname='', ball='Poke Ball'):
        # Take catch args
        self.nickname = nickname
        self.ball = ball

        # Set stats
        self.__set_stats()
        self.__set_exp()

    # Sets stats based on IVs and base stats
    # Formulas found at bulbapedia.bulbagarden.net/wiki/Individual_values
    def __set_stats(self):
        # Set hp
        self.stats['hp'] = int(((2 * self.base_stats['hp'] + self.ivs['hp'] + int(self.evs['hp']/4)) * self.level) / 100) + self.level + 10

        # Set the rest
        for stat in self.stats:
            if stat != 'hp':
                self.stats[stat] = int((int(((2 * self.base_stats[stat] + self.ivs[stat] + int(self.evs[stat]/4)) * self.level) / 100) + 5) * self.__get_nature_mod(stat))

    def __get_nature_mod(self, stat):
        if stat == 'atk':
            if self.nature in NATURES[1:5]:
                return NATURE_MOD_INCREASE
            elif self.nature in NATURES[5::5]:
                return NATURE_MOD_DECREASE
            else:
                return NATURE_MOD_NONE

        elif stat == 'def':
            if self.nature in NATURES[5:10] and self.nature != 'Docile':
                return NATURE_MOD_INCREASE
            elif self.nature in ['Lonely','Hasty','Mild','Gentle']:
                return NATURE_MOD_DECREASE
            else:
                return NATURE_MOD_NONE

        elif stat == 'spd':
            if self.nature in NATURES[10:15] and self.nature != 'Serious':
                return NATURE_MOD_INCREASE
            elif self.nature in ['Brave','Relaxed','Quiet','Sassy']:
                return NATURE_MOD_DECREASE
            else:
                return NATURE_MOD_NONE

        elif stat == 'spAtk':
            if self.nature in NATURES[15:20] and self.nature != 'Bashful':
                return NATURE_MOD_INCREASE
            elif self.nature in ['Adamant','Impish','Jolly','Careful']:
                return NATURE_MOD_DECREASE
            else:
                return NATURE_MOD_NONE

        elif stat == 'spDef':
            if self.nature in NATURES[20:24]:
                return NATURE_MOD_INCREASE
            elif self.nature in NATURES[4::5] and self.nature != 'Quirky':
                return NATURE_MOD_DECREASE
            else:
                return NATURE_MOD_NONE

    def __set_exp(self, extra_points=0):
        self.exp = pow(self.level, EXP_MOD) + extra_points
        self.exp_to_next_lvl = pow(self.level + 1, EXP_MOD) - self.exp

    def gain_exp(self, points):
        print(self.name, "gained", points, "Exp. Points!")
        self.exp += points
        input()
        if points > self.exp_to_next_lvl:
            self.__level_up()
            extra = points - self.exp_to_next_lvl
            self.__set_exp(extra)
        else:
            self.exp_to_next_lvl -= points

    def __level_up(self):
        self.level += 1
        print(self.name, "grew to Lv.", str(self.level) + "!")

        old_hp = self.stats['hp']
        old_atk = self.stats['atk']
        old_def = self.stats['def']
        old_spAtk = self.stats['spAtk']
        old_spDef = self.stats['spDef']
        old_spd = self.stats['spd']
        self.__set_stats()

        input()
        print("Max HP    +" + str(self.stats['hp'] - old_hp))
        print("Attack    +" + str(self.stats['atk'] - old_atk))
        print("Defense   +" + str(self.stats['def'] - old_def))
        print("Sp. Atk   +" + str(self.stats['spAtk'] - old_spAtk))
        print("Sp. Def   +" + str(self.stats['spDef'] - old_spDef))
        print("Speed     +" + str(self.stats['spd'] - old_spd))
        input()
        print("Max HP    " + str(self.stats['hp']))
        print("Attack    " + str(self.stats['atk']))
        print("Defense   " + str(self.stats['def']))
        print("Sp. Atk   " + str(self.stats['spAtk']))
        print("Sp. Def   " + str(self.stats['spDef']))
        print("Speed     " + str(self.stats['spd']))

    def show_stats(self):
        print("Name:       ", self.name)
        print("Nickname:   ", self.nickname)
        print("Pokedex #:  ", self.pokedex_num)
        print("Type(s):    ", self.type)
        print("Gender:     ", self.gender)
        print("Nature:     ", self.nature, '(' + str(NATURES.index(self.nature)) + ')')
        print("Ball:       ", self.ball)
        print("Max HP:     ", self.stats['hp'], 'IV:', self.ivs['hp'], 'Base:', self.base_stats['hp'])
        print("Attack:     ", self.stats['atk'], 'IV:', self.ivs['atk'], 'Base:', self.base_stats['atk'])
        print("Defense:    ", self.stats['def'], 'IV:', self.ivs['def'], 'Base:', self.base_stats['def'])
        print("Sp. Attack: ", self.stats['spAtk'], 'IV:', self.ivs['spAtk'], 'Base:', self.base_stats['spAtk'])
        print("Sp. Defense:", self.stats['spDef'], 'IV:', self.ivs['spDef'], 'Base:', self.base_stats['spDef'])
        print("Speed:      ", self.stats['spd'], 'IV:', self.ivs['spd'], 'Base:', self.base_stats['spd'])
        print("Level:      ", self.level)
        print("Exp. Points:", self.exp, "To next:", self.exp_to_next_lvl)
        print("Moves:      ", self.moves)

    def fight(self):
        pass

    def run(self):
        pass

    def give_item(self, item):
        pass
