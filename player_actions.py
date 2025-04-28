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

        character = self._prompt_choice(
            prompt_message=f"\nChoose a character {characters_list}: ",
            valid_options=valid_characters,
            item_type="character"
        )

        weapon = self._prompt_choice(
            prompt_message=f"\nChoose a weapon {weapons_list}: ",
            valid_options=valid_weapons,
            item_type="weapon"
        )

        print(f"\nYou suggested that {character} committed the crime in the {self.current_room} with the {weapon}.")

    def _prompt_choice(self, prompt_message, valid_options, item_type):
        while True:
            choice = input(prompt_message).strip().lower()
            if choice in valid_options:
                return valid_options[choice]
            print(f"Invalid {item_type}. Please choose from the list.")
