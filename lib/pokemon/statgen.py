# File stat constants and calculations
# Author: Luke Simone

import random

__all__ = ['generate_nature', 'generate_ivs', 'generate_stats',
           'set_gender', 'set_characteristic']


class _Stats:
    """Collection of functions for calculating stats"""

    # Constants
    NATURES = ['Hardy', 'Lonely', 'Brave', 'Adamant', 'Naughty',
               'Bold', 'Docile', 'Relaxed', 'Impish', 'Lax', 'Timid',
               'Hasty', 'Serious', 'Jolly', 'Naive', 'Modest', 'Mild',
               'Quiet', 'Bashful', 'Rash', 'Calm', 'Gentle', 'Sassy',
               'Careful', 'Quirky']
    NATURE_MOD_INCREASE = 1.10
    NATURE_MOD_DECREASE = 0.90
    NATURE_MOD_NONE = 1.0

    STAT_TEMPLATE = {'hp': 0, 'atk': 0, 'def': 0,
                     'spAtk': 0, 'spDef': 0, 'spd': 0}

    CHARACTERISTICS = {'hp': ['Loves to eat', 'Often dozes off',
                              'Often scatters things', 'Scatters things often',
                              'Likes to Relax'],
                       'atk': ['Proud of its power', 'Likes to thrash about',
                               'A little quick tempered', 'Likes to fight',
                               'Quick Tempered'],
                       'def': ['Sturdy body', 'Capable of taking hits',
                               'Highly persistent', 'Good endurance',
                               'Good perseverance'],
                       'spAtk': ['Highly curious', 'Mischievous',
                                 'Thoroughly Cunning', 'Often lost in thought',
                                 'Very finicky'],
                       'spDef': ['Strong willed', 'Somewhat vain',
                                 'Strongly defiant', 'Hates to lose',
                                 'Somewhat stubborn'],
                       'spd': ['Likes to run', 'Alert to sounds',
                               'Impetuous and silly', 'Somewhat of a clown',
                               'Quick to flee']}

    def __init__(self):
        pass

    # Return a random nature for a pokemon to have
    def generate_nature(self):
        return random.choice(self.NATURES)

    # Generates an individual value (IV)
    def generate_ivs(self):
        return {k: random.randint(0, 32) for k in self.STAT_TEMPLATE}

    # Sets stats based on IVs, EVs, and base stats
    # Formulas found at bulbapedia.bulbagarden.net/wiki/Individual_values
    def generate_stats(self, base_stats, ivs, evs, level, nature):
        def _gen():
            for k in self.STAT_TEMPLATE:
                if k == 'hp':
                    yield k, int(((2 * base_stats[k] + ivs[k] +
                                   int(evs[k]/4)) * level) / 100) + level + 10
                else:
                    yield k, int((int(((2 * base_stats[k] + ivs[k] + int(evs[k]/4)) * level) /
                                      100) + 5) * self._set_nature_mod(k, nature))
        return {k: v for k, v in _gen()}  # Dictionary

    # Generates the Pokemons gender, default is 50/50
    def set_gender(self, chance_is_male):
        try:
            if random.random() < chance_is_male:
                return '♂'
            return '♀'
        except TypeError:
            return None

    # Gets a particular stats modifier based on the nature (10% inc or dec)
    def _set_nature_mod(self, stat, nature):
        if stat == 'atk':
            if nature in self.NATURES[1:5]:
                return self.NATURE_MOD_INCREASE
            elif nature in self.NATURES[5::5]:
                return self.NATURE_MOD_DECREASE
            return self.NATURE_MOD_NONE

        elif stat == 'def':
            if nature in self.NATURES[5:10] and nature != 'Docile':
                return self.NATURE_MOD_INCREASE
            elif nature in ['Lonely', 'Hasty', 'Mild', 'Gentle']:
                return self.NATURE_MOD_DECREASE
            return self.NATURE_MOD_NONE

        elif stat == 'spd':
            if nature in self.NATURES[10:15] and nature != 'Serious':
                return self.NATURE_MOD_INCREASE
            elif nature in ['Brave', 'Relaxed', 'Quiet', 'Sassy']:
                return self.NATURE_MOD_DECREASE
            return self.NATURE_MOD_NONE

        elif stat == 'spAtk':
            if nature in self.NATURES[15:20] and nature != 'Bashful':
                return self.NATURE_MOD_INCREASE
            elif nature in ['Adamant', 'Impish', 'Jolly', 'Careful']:
                return self.NATURE_MOD_DECREASE
            return self.NATURE_MOD_NONE

        elif stat == 'spDef':
            if nature in self.NATURES[20:24]:
                return self.NATURE_MOD_INCREASE
            elif nature in self.NATURES[4::5] and nature != 'Quirky':
                return self.NATURE_MOD_DECREASE
            return self.NATURE_MOD_NONE

    # Gets a Pokemons characteristic based on their iv values
    def set_characteristic(self, ivs):
        # Find highest IV
        highest_iv = 'hp'
        for k, v in ivs.items():
            if ivs[highest_iv] < v:
                highest_iv = k

        # Set characteristic based on highest IV
        for k, v in ivs.items():
            if k == highest_iv:
                if v in range(0, 31, 5):
                    return self.CHARACTERISTICS[k][0]
                if v in range(1, 32, 5):
                    return self.CHARACTERISTICS[k][1]
                if v in range(2, 28, 5):
                    return self.CHARACTERISTICS[k][2]
                if v in range(3, 29, 5):
                    return self.CHARACTERISTICS[k][3]
                if v in range(4, 30, 5):
                    return self.CHARACTERISTICS[k][4]


# Test functionality
def _test():
    # Charizard
    _bs = {'hp': 78, 'atk': 84, 'def': 78,
           'spAtk': 109, 'spDef': 85, 'spd': 100}
    _evs = {'hp': 0, 'atk': 0, 'def': 0, 'spAtk': 0, 'spDef': 0, 'spd': 0}
    _n = generate_nature()
    _ivs = generate_ivs()
    _s = generate_stats(_bs, _ivs, _evs, 50, _n)
    _g = set_gender(.875)
    _c = set_characteristic(_ivs)
    print("nature:", _n)
    print("gender:", _g)
    print("char:  ", _c)
    print("hp:    ", _s['hp'], "iv: ", _ivs['hp'])
    print("atk:   ", _s['atk'], "iv: ", _ivs['atk'])
    print("def:   ", _s['def'], "iv: ", _ivs['def'])
    print("spAtk: ", _s['spAtk'], "iv: ", _ivs['spAtk'])
    print("spDef: ", _s['spDef'], "iv: ", _ivs['spDef'])
    print("spd:   ", _s['spd'], "iv: ", _ivs['spd'])


# Public package
_s = _Stats()
generate_nature = _s.generate_nature
generate_ivs = _s.generate_ivs
generate_stats = _s.generate_stats
set_gender = _s.set_gender
set_characteristic = _s.set_characteristic

del _s

if __name__ == '__main__':
    _test()
