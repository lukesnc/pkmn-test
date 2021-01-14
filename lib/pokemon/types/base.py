# Pokemon types base class
# Author: Luke Simone


class Type:
    def __init__(self, name, attack_type, defend_type):
        self.name = name
        self._attack_type = attack_type  # Dict
        self._defend_type = defend_type  # Dict

    def __str__(self):
        return str(self.name)


def _test(_t):
    pass

# if __name__ == '__main__':
#     _test(fire)
