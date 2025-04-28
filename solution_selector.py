import random
from characters import characters_list
from weapons import weapons_list
from mansion import mansion_rooms


def select_solution():
    return {
        "Character": _choose_random(characters_list),
        "Weapon": _choose_random(weapons_list),
        "Room": _choose_random(mansion_rooms)
    }


def _choose_random(options):
    return random.choice(options)
