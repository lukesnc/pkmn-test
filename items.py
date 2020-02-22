# File containing the item database
# Author: Luke Simone

__all__ = ['potion','super_potion','antidote','poke_ball','great_ball',
           'ultra_ball']

class Item(object):
    def __init__(self, name, desc, cost):
        self._name = name
        self._description = desc
        self._cost = int(cost)
        self._sell_price = int(cost * 0.5)

    def use(self):
        # Successfully used
        return True

class Medicine(Item):
    def __init__(self, name, desc, cost, type, hp_rest=0, stat_cured=None):
        Item.__init__(self, name, desc, cost)
        self._type = type # HP or Status
        self._hp_restored = hp_rest
        self._status_cured = stat_cured

class Ball(Item):
    def __init__(self, name, desc, cost, rate):
        Item.__init__(self, name, desc, cost)
        self._catch_rate_mod = rate

# Test item values
def _test(_i):
    print("Item:", _i._name)
    print("Description:", _i._description)
    print("Cost:", _i._cost)
    print("Sell price:", _i._sell_price)
    print("Used item.", _i.use())
    # Medicine specific
    try:
        print("Type:", _i._type)
        print("HP Restored:", _i._hp_restored)
        print("Status cured:", _i._status_cured)
    except:
        pass
    # Ball specific
    try:
        print("Catch rate:", _i._catch_rate_mod)
    except:
        pass
    del _i


# Potion
_desc = "When used from the Bag on a Pokémon, it heals the Pokémon by 20 HP."
potion = Medicine('Potion', _desc, 300, 'HP', 20)

# Super Potion
_desc = "When used from the Bag on a Pokémon, it heals the Pokémon by 60 HP."
super_potion = Medicine('Super Potion', _desc, 700, 'HP', 60)

# Antidote
_desc = "When used from the Bag on a Pokémon, it cures a Pokémon from poisoning."
antidote = Medicine('Antidote', _desc, 100, 'Status', 'Poison')

# Poke Ball
_desc = "A device for catching wild Pokémon. It's thrown like a ball at a Pokémon, comfortably encapsulating its target."
poke_ball = Ball('Poke Ball', _desc, 200, 1.0)

# Great Ball
_desc = "A good, high-performance Poké Ball that provides a higher success rate for catching Pokémon than a standard Poké Ball."
great_ball = Ball('Great Ball', _desc, 600, 1.5)

# Ultra ball
_desc = "An ultra-high-performance Poké Ball that provides a higher success rate for catching Pokémon than a Great Ball."
ultra_ball = Ball('Ultra Ball', _desc, 800, 2.0)

if __name__ == '__main__':
    _test(great_ball)
