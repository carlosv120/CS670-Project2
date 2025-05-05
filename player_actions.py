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

        character = self._choose_item("character", characters_list)
        weapon = self._choose_item("weapon", weapons_list)
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

    def _choose_item(self, item_type, options):
        lookup = {item.lower(): item for item in options}

        while True:
            print(f"\nChoose a {item_type} {options}: ")

            value = input("> ").strip().lower()

            if value in lookup:
                if lookup[value] in self.hand:
                    print(f"You have that {item_type} in your deck. Pick another.")
                    continue
                return lookup[value]
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
            if not self._wait_for_ready():
                continue

            print(f"\n{other.name}, you can refute with {matches}.")
            if len(matches) == 1:
                shown = matches[0]
            else:
                shown = self._prompt_refute_choice(matches)

            print(f"\n*************** {other.name} refuted with {shown} ***************")
            print(f"\nPassing control to {self.name} (Player's turn).")

            while True:
                confirm = input(f"\n{self.name}, are you ready to continue? (yes/no): ").strip().lower()
                if confirm == "yes":
                    break
                if confirm == "no":
                    print("Take your time, let me know when you're ready.")
                else:
                    print("Invalid input. Please answer 'yes' or 'no'.")

            return other.name, shown

        print("No one could refute your suggestion.")
        return None, None

    def _wait_for_ready(self):

        while True:
            ready = input("Are you ready to reveal a card? (yes/no): ").strip().lower()

            if ready == "yes":
                return True
            if ready == "no":
                print("\nTake your time, let me know when you are ready.")
                continue
            print("\nPlease answer 'yes' or 'no'.")

    def _prompt_refute_choice(self, matches):
        lookup = {m.lower(): m for m in matches}
        
        while True:
            chosen = input("Select the card to reveal: ").strip().lower()
            if chosen in lookup:
                return lookup[chosen]
            print("Invalid choice. Pick from the list.\n")
