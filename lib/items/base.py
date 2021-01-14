# File containing the item base classes
# Author: Luke Simone

class Item(object):
    def __init__(self, name, desc, cost):
        self.name = name
        self.description = desc
        self.cost = int(cost)
        self.sell_price = int(cost * 0.5)

    def __str__(self):
        return str(self.name)

    def use(self):
        # Successfully used
        return True


class Medicine(Item):
    def __init__(self, name, desc, cost, med_type, hp_rest=0, stat_cured=None):
        Item.__init__(self, name, desc, cost)
        self.med_type = med_type  # HP or Status
        self._hp_restored = hp_rest
        self._status_cured = stat_cured

    def use(self):
        if self.med_type == 'HP':
            return self._hp_restored
        else:
            return self._status_cured


class Ball(Item):
    def __init__(self, name, desc, cost, rate):
        Item.__init__(self, name, desc, cost)
        self._catch_rate_mod = rate

    def use(self):
        return self._catch_rate_mod


# Test item values
def _test(_i):
    print("Item:", _i.name)
    print("Description:", _i.description)
    print("Cost:", _i.cost)
    print("Sell price:", _i.sell_price)
    # Medicine specific
    try:
        print("Type:", _i.med_type)
        print("HP Restored:", _i._hp_restored)  # use use() in actual code!
        print("Status cured:", _i._status_cured)
    except AttributeError:
        pass
    # Ball specific
    try:
        print("Catch rate:", _i._catch_rate_mod)
    except AttributeError:
        pass
    del _i
