# All items
# Author: Luke Simone

from .base import Medicine, Ball

potion = Medicine(
    name='Potion',
    desc="When used from the Bag on a Pokémon, it heals the Pokémon by 20 HP.",
    cost=300,
    med_type='HP',
    hp_rest=20
)

super_potion = Medicine(
    name='Super Potion',
    desc="When used from the Bag on a Pokémon, it heals the Pokémon by 60 HP.",
    cost=700,
    med_type='HP',
    hp_rest=60
)

antidote = Medicine(
    name='Antidote',
    desc="When used from the Bag on a Pokémon, it cures a Pokémon from poisoning.",
    cost=100,
    med_type='Status',
    stat_cured='Poison'
)

poke_ball = Ball(
    name='Poke Ball',
    desc="A device for catching wild Pokémon. It's thrown like a ball at a Pokémon, comfortably encapsulating its target.",
    cost=200,
    rate=1.0
)

great_ball = Ball(
    name='Great Ball',
    desc="A good, high-performance Poké Ball that provides a higher success rate for catching Pokémon than a standard Poké Ball.",
    cost=600,
    rate=1.5
)

ultra_ball = Ball(
    name='Ultra Ball',
    desc="An ultra-high-performance Poké Ball that provides a higher success rate for catching Pokémon than a Great Ball.",
    cost=800,
    rate=2.0
)
