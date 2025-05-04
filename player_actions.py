from random import choice
from characters import characters_list
from weapons import weapons_list
from mansion import mansion_rooms


def sort_cards(hand):
    locations = [c for c in hand if c in mansion_rooms]
    persons   = [c for c in hand if c in characters_list]
    objects   = [c for c in hand if c in weapons_list]
    return locations + persons + objects


class Player:
    def __init__(self, name):
        self.name = name
        self.current_room = "Hall"
        self.hand = []
        self.notes = []
        self.seen = set()
        self.active = True 

    def move_to(self, room):
        self.current_room = room

    def show_notes(self):
        print("\n--- Your Notes ---")
        for idx, entry in enumerate(self.notes, 1):
            sug = entry["suggestion"]
            ref = entry["refuter"] or "None"
            card = entry["card"] or "None"
            print(f"{idx}. Suggestion {sug} | Refuter: {ref} | Card shown: {card}")
        print("Seen cards:", sort_cards(self.seen))
        print("------------------\n")

    def make_suggestion(self, players, current_player_index):
        print("\nMake your suggestion:")
        print(f"Remember, these are your cards: {sort_cards(self.hand)}")
        character = self._choose_character()
        weapon = self._choose_weapon()
        room = self.current_room
        print(f"\nYou suggested that {character} committed the crime in the {room} with the {weapon}.")
        refuter, shown_card = self._refute(players, current_player_index, {character, weapon, room})
        self.notes.append(
            {"suggestion": (character, weapon, room),
             "refuter": refuter,
             "card": shown_card}
        )
        if shown_card:
            self.seen.add(shown_card)

    def _choose_character(self):
        lookup = self._build_lookup(characters_list)
        while True:
            card = self._prompt_choice(f"\nChoose a character {characters_list}: ", lookup, "character")
            if card in self.hand:
                print("You have that character in your deck. Pick another character.")
                continue
            return card

    def _choose_weapon(self):
        lookup = self._build_lookup(weapons_list)
        while True:
            card = self._prompt_choice(f"\nChoose a weapon {weapons_list}: ", lookup, "weapon")
            if card in self.hand:
                print("You have that weapon in your deck. Pick another weapon.")
                continue
            return card

    @staticmethod
    def _build_lookup(options):
        return {item.lower(): item for item in options}

    def _prompt_choice(self, prompt_message, valid_options, item_type):
        while True:
            value = input(prompt_message).strip().lower()
            if value in valid_options:
                return valid_options[value]
            print(f"Invalid {item_type}. Please choose from the list.")

    def _refute(self, players, current_player_index, suggestion_set):
        print("\nChecking if any player can refute...")
        n = len(players)
        for step in range(1, n):
            other = players[(current_player_index + step) % n]
            matches = [c for c in suggestion_set if c in other.hand]
            if not matches:
                print(f"{other.name} cannot refute.")
                continue

            print(f"\n{other.name} can refute. Passing control to {other.name}...")
            while True:
                ready = input("Are you ready to reveal a card? (yes/no): ").strip().lower()
                if ready == "no":
                    print("\nTake your time, let me know when you are ready.")
                    continue
                if ready != "yes":
                    print("\nPlease answer 'yes' or 'no'.")
                    continue

                print(f"\n{other.name}, you can refute with {matches}.")
                if len(matches) == 1:
                    shown = matches[0]
                else:
                    lookup = {m.lower(): m for m in matches}
                    while True:
                        chosen = input("Select the card to reveal: ").strip().lower()
                        if chosen in lookup:
                            shown = lookup[chosen]
                            break
                        print("Invalid choice. Pick from the list.")
                print(f"\n{other.name} refuted with {shown}")
                return other.name, shown

        print("No one could refute your suggestion.")
        return None, None
