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
        character = self._choose_character()
        weapon = self._choose_weapon()
        print(
            f"\nYou suggested that {character} committed the crime "
            f"in the {self.current_room} with the {weapon}."
        )

    def _choose_character(self):
        lookup = self._build_lookup(characters_list)
        return self._prompt_choice(
            f"\nChoose a character {characters_list}: ", lookup, "character"
        )

    def _choose_weapon(self):
        lookup = self._build_lookup(weapons_list)
        return self._prompt_choice(
            f"\nChoose a weapon {weapons_list}: ", lookup, "weapon"
        )

    @staticmethod
    def _build_lookup(options):
        return {item.lower(): item for item in options}

    def _prompt_choice(self, prompt_message, valid_options, item_type):
        while True:
            choice = input(prompt_message).strip().lower()
            if choice in valid_options:
                return valid_options[choice]
            print(f"Invalid {item_type}. Please choose from the list.")
