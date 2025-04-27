from characters import characters_list
from weapons import weapons_list

class Player:
    def __init__(self, name):
        self.name = name
        self.current_room = "Hall"

    def move_to(self, room):
        self.current_room = room

    def make_suggestion(self):
        print("\nMake your suggestion:")

        valid_characters = {character.lower(): character for character in characters_list}
        valid_weapons = {weapon.lower(): weapon for weapon in weapons_list}

        character = self._prompt_choice("character", valid_characters, characters_list)
        weapon = self._prompt_choice("weapon", valid_weapons, weapons_list)

        print(f"\nYou suggested that {character} committed the crime in the {self.current_room} with the {weapon}.")

    def _prompt_choice(self, item_type, valid_items, items_list):
        while True:
            choice = input(f"\nChoose a {item_type} {items_list}: ").strip().lower()
            if choice in valid_items:
                return valid_items[choice]
            print(f"Invalid {item_type}. Please choose from the list.")
