from random import shuffle
from mansion import mansion_rooms
from characters import characters_list
from weapons import weapons_list
from player_actions import Player, sort_cards
from solution_selector import select_solution
import time

def clean_input(prompt):
    return input(prompt).strip().lower()

def get_valid_input(prompt, valid_options):

    while True:
        response = clean_input(prompt)

        if response in valid_options:
            return response
        print("Invalid input. Please type one of:", ', '.join(valid_options))

def print_option_list(label, options):
    print(f"\nChoose a {label}:")

    for item in options:
        print(f"  - {item}")

def get_number_of_players():

    while True:
        user_input = input("Enter number of players (2-6): ").strip()

        if user_input.isdigit():
            num_players = int(user_input)

            if 2 <= num_players <= 6:
                return num_players
        print("Invalid input. Please enter a valid number between 2 and 6.\n")


def get_player_names(num_players):
    players = []

    for i in range(1, num_players + 1):
        while True:
            name = input(f"\nEnter name for Player {i}: ").strip()

            if name and name.replace(" ", "").isalpha():
                players.append(Player(name))
                break
            print("Invalid name. Please enter a valid name using only letters.")
    return players


def print_solution_for_testing(solution):
    print(f"\n[SOLUTION FOR TESTING] {solution}\n")


def build_valid_room_map():
    return {room.lower(): room for room in mansion_rooms}


def show_available_rooms():
    print("\nAvailable Rooms:")

    for room in mansion_rooms:
        print("-", room)


def move_player(player, valid_rooms):

    print("\nYou are in:", player.current_room)
    show_available_rooms()

    while True:
        move = clean_input("\nWhere would you like to move? (type room name, 'notes', or 'exit'): ")

        if move == "notes":
            player.show_notes()
            continue
        if move == "exit":
            return None

        selected_room = valid_rooms.get(move)

        if not selected_room:
            print("\nInvalid input. Please type a room name, 'notes', or 'exit'.")
            continue
        if selected_room == player.current_room:
            print("You are already in that room. Pick a different room.")
            continue

        player.move_to(selected_room)
        print("You moved to:", selected_room)

        return True



def handle_suggestion(player, players, current_player_index):
    make_suggestion = get_valid_input("\nWould you like to make a suggestion? (yes/no): ", ("yes", "no"))

    if make_suggestion == "yes":
        player.make_suggestion(players, current_player_index)


def _prompt_accuse_item(label, options, first=False):

    if first:
        print("\n**** ACCUSE ****")
    print_option_list(label, options)

    lookup = {o.lower(): o for o in options}

    while True:
        choice = clean_input("> ")

        if choice in lookup:
            return lookup[choice]
        print("Invalid choice. Type one of the names above.\n")


def handle_accusation(player, solution):
    accuse = get_valid_input("\nDo you want to make an accusation? (yes/no): ", ("yes", "no"))

    if accuse == "no":
        return False, False

    char = _prompt_accuse_item("character", characters_list, first=True)
    weap = _prompt_accuse_item("weapon", weapons_list)
    room = _prompt_accuse_item("room", mansion_rooms)

    print(f"\n{player.name} accuses {char} in the {room} with the {weap}!")
    time.sleep(2)

    if {"Character": char, "Weapon": weap, "Room": room} == solution:

        print(f"\n>>> {player.name} made a CORRECT accusation and wins the game! <<<")
        return True, True

    print("\nThat accusation is incorrect. You are out of the game.")
    player.active = False

    return False, False


def prompt_next_player(next_player, player):

    while True:
        ready = clean_input(f"\nIs next player {next_player.name} ready? (yes/no): ")

        if ready == "yes":
            print(f"\n--------- End of {player.name}'s Turn ---------\n")
            return
        if ready == "no":
            print("\nTake your time, let me know when ready.")
        else:
            print("Invalid input. Please type 'yes' or 'no'.")


def deal_cards(players, solution):
    deck = (
        [c for c in characters_list if c != solution["Character"]]
        + [w for w in weapons_list if w != solution["Weapon"]]
        + [r for r in mansion_rooms if r != solution["Room"]]
    )

    shuffle(deck)

    for idx, card in enumerate(deck):
        players[idx % len(players)].hand.append(card)


def game_loop(players, valid_rooms, solution):
    current_player_index = 0
    num_players = len(players)

    while True:
        active_players = [p for p in players if p.active]

        if not active_players:
            print("\nNo active players remain. Crime unsolved.")
            print("The correct solution was:", solution)
            return

        player = players[current_player_index]

        if not player.active:
            current_player_index = (current_player_index + 1) % num_players
            continue

        print(f"********* {player.name}'s Turn *********")
        move_successful = move_player(player, valid_rooms)

        if move_successful is None:
            print(f"{player.name} has exited the game.")
            return

        handle_suggestion(player, players, current_player_index)

        won, ended = handle_accusation(player, solution)

        if won:
            return
        
        if ended and all(not p.active for p in players):
            print("\nNo active players remain. Crime unsolved.")
            print("The correct solution was:", solution)
            return

        next_index = (current_player_index + 1) % num_players

        while not players[next_index].active:
            next_index = (next_index + 1) % num_players

        prompt_next_player(players[next_index], player)
        current_player_index = next_index


def setup_game():
    num_players = get_number_of_players()
    players = get_player_names(num_players)

    for p in players:
        p.active = True

    solution = select_solution()
    print_solution_for_testing(solution)
    deal_cards(players, solution)

    for p in players:
        print(f"{p.name}'s hand: {sort_cards(p.hand)}\n")
    print()

    valid_rooms = build_valid_room_map()
    return players, valid_rooms, solution


def main():
    
    print("\nProject 2 Part 2: Cluedo")
    players, valid_rooms, solution = setup_game()
    game_loop(players, valid_rooms, solution)


if __name__ == "__main__":
    main()
