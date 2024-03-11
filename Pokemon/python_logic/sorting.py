from typing import List
from enum import Enum

"""
Be Able to Sort Pokemon by generation but also evolution line number
    So like have a stat be evolution order? Or actually I think it's better to have a list of 'can evolve from' and 'can evolve to', and then calculate evolution order recursively lol
"""

# Stats
class Pokemon:
    name: str
    dex_num: int
    types: List[str]
    # evolves_from: List[Pokemon]
    evolves_from: List
    evolvtes_to: List
    

class Generation:
    gen_order: int
    gen_name: str
    gen_start_num: int
    gen_end_num: int
    gen_count: int


class PokemonCard:
    id: str
    expansion: str
    expansion_num: int
    type: int       # (1=pokemon, 2=trainer, 3=energy)
    name: str
    type: str
    hp: int
    rarity: int

class Expansion:
    year: int
    expansion_set: str
    sets: List

class Rarity(Enum):
    common = 1
    uncommon = 2
    rare = 3
    holo = 4
    v = 5
    vmax = 6
    vstar = 7
    ex = 8
    other = 9

    # OR
    # you have pokemoncard.rarity to get a number or pokemoncard.rarity.s to get a string
    rarity_num = None
    def s(self):
        n = self.rarity_num
        if   n == 1: "common"
        elif n == 2: "uncommon"
        elif n == 3: "rare"
        elif n == 4: "holo rare"
        elif n == 5: "v"
        elif n == 6: "vmax"
        elif n == 7: "vstar"
        elif n == 8: "ex"
        else:        "other"

class Evolution:
    # Have some kind of method to handle a logic check on an evolution
    # Maybe have 'stat', 'less, equal, more', and 'value', and then you can like check if stat or less/equal/more or value is true?
    pass