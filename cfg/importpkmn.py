# File to import Pokemon stats from cfg into Pokemon class
# Author: Luke Simone

from configparser import ConfigParser

pokemon_to_import = 'Bulbasaur'

PKMNFILE = './pkmn-cfg/' + pokemon_to_import + '.cfg'

importer = ConfigParser()
try:
    importer.read(PKMNFILE)
except:
    print("Something went wrong.")
    exit(1)
