from random import shuffle
from mansion import mansion_rooms
from characters import characters_list
from weapons import weapons_list
from player_actions import Player, sort_cards
from solution_selector import select_solution


def get_number_of_players():
    while True:
        user_input = input("Enter number of players (2-6): ").strip()
        if user_input.isdigit():
            num_players = int(user_input)
            if 2 <= num_players <= 6:
                return num_players
        print("Invalid input. Please enter a valid number between 2 and 6.")


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
        move = input(
            "\nWhere would you like to move? (type room name, 'notes', or 'exit'): "
        ).strip().lower()

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
    while True:
        make_suggestion = input("\nWould you like to make a suggestion? (yes/no): ").strip().lower()
        if make_suggestion in ("yes", "no"):
            break
        print("Invalid input. Please type 'yes' or 'no'.")
    if make_suggestion == "yes":
        player.make_suggestion(players, current_player_index)


def prompt_next_player(next_player, player):
    while True:
        ready = input(f"\nIs next player {next_player.name} ready? (yes/no): ").strip().lower()
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


def game_loop(players, valid_rooms):
    current_player_index = 0
    num_players = len(players)
    game_active = True
    while game_active:
        player = players[current_player_index]
        print(f"********* {player.name}'s Turn *********")
        move_successful = move_player(player, valid_rooms)
        if move_successful is None:
            print(f"{player.name} has exited the game.")
            game_active = False
            continue
        handle_suggestion(player, players, current_player_index)
        next_index = (current_player_index + 1) % num_players
        prompt_next_player(players[next_index], player)
        current_player_index = next_index
    print("\nGame has ended.")


def main():
    print("\nProject 2 Part 2: Cluedo")
    num_players = get_number_of_players()
    players = get_player_names(num_players)
    solution = select_solution()
    print_solution_for_testing(solution)
    deal_cards(players, solution)
    for p in players:
        print(f"{p.name}'s hand: {sort_cards(p.hand)}")
    print()
    valid_rooms = build_valid_room_map()
    game_loop(players, valid_rooms)


if __name__ == "__main__":
    main()
