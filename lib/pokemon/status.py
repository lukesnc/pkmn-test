# File for status conditions in battle
# Author: Luke Simone

class StatUp:
    pass


class StatDown:
    def __init__(self, target, stat):
        pass


class Poison:
    damage_percent = 1/16
    def __init__(self, is_bad):
        self.is_bad = is_bad


class Paralyze:
    pass

# Test functionality


def _test(battle_stat):
    pass


if __name__ == '__main__':
    _poison = Poison(is_bad=True)
    _test(_poison)
