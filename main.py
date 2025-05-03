from mansion import mansion_rooms
from player_actions import Player
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
    print(f"\nFor testing purposes, the solution is: {solution}\n")

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
        move = input("\nWhere would you like to move? (type room name or 'exit' to leave): ").strip().lower()

        if move == "exit":
            return None

        selected_room = valid_rooms.get(move)
        if selected_room:
            player.move_to(selected_room)
            print("You moved to:", selected_room)
            return True

        print("Invalid input. Please type a valid room name or 'exit'.")

def handle_suggestion(player):
    while True:
        make_suggestion = input("\nWould you like to make a suggestion? (yes/no): ").strip().lower()
        if make_suggestion in ["yes", "no"]:
            break
        print("Invalid input. Please type 'yes' or 'no'.")

    if make_suggestion == "yes":
        player.make_suggestion()

def prompt_next_player(next_player, player):
    while True:
        ready = input(f"\nIs next player {next_player.name} ready? (yes/no): ").strip().lower()
        if ready == "yes":
            print(f"\n--------- End of {player.name}'s Turn ---------\n")
            return
        if ready == "no":
            print("Take your time, let me know when ready.")
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

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

        handle_suggestion(player)

        next_player_index = (current_player_index + 1) % num_players
        next_player = players[next_player_index]
        prompt_next_player(next_player, player)

        current_player_index = next_player_index

    print("\nGame has ended.")

def main():
    print("Project 2 Part 1: Cluedo")

    num_players = get_number_of_players()
    players = get_player_names(num_players)
    solution = select_solution()
    print_solution_for_testing(solution)

    valid_rooms = build_valid_room_map()
    game_loop(players, valid_rooms)

if __name__ == "__main__":
    main()
