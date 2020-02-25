# Class file for Pokemon types
# Author: Luke Simone

# Imports

class Type:
    def __init__(self, name, attack_type, defend_type):
        self.name = name
        self._attack_type = attack_type # Dict
        self._defend_type = defend_type # Dict

def _test(_t):
    pass

# Types
_types = []
fire = Type('Fire', {}, {})
for t in _types:
    pass



if __name__ == '__main__':
    _test(fire)
