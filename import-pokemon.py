# File to import Pokemon stats from cfg into Pokemon class
# Author: Luke Simone

# Imports
from configparser import ConfigParser

pokemon_to_import = 'Bulbasaur'

PKMNFILE = './pokemon-cfg/' + pokemon_to_import + '.cfg'

importer = ConfigParser()
try:
    importer.read(PKMNFILE)
except:
    print("Something went wrong.")
    exit(1)
