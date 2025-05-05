"""
Main file containing game setup and the main loop. Run this file to launch the
game.
"""

from model.model import TypeRacePlayer, HostPlayer, ClientPlayer
from view.view import GUIView
from controller.controller import TextController


def game_mode_select():
    """
    Ask the user to select single player or multi-player. Will recursively ask
    until a valid response is received.

    Returns str 's' for single player mode and 'm' for multiplayer mode.
    """

    mode = input(
        "Enter 's' for single player, 'h' for host (multiplayer), or 'c' for "
        "client (multiplayer): "
    )
    if mode in ("s", "h", "c"):
        return mode
    return game_mode_select()


# User input for single/multi-player
game_mode = game_mode_select()

# Initialize Model class
if game_mode == "s":
    player = TypeRacePlayer()
elif game_mode == "h":
    player = HostPlayer()
else:  # game mode 'c'
    player = ClientPlayer()

# Initialize View and Controller classes
view = GUIView(player)
controller = TextController(player)

# Set start time
player.set_start_time()

# Main game loop:
while True:
    # If the game over condition is True, exit the game loop
    if player.game_over:
        break

    # Check the controller for new user input
    controller.typechecker()
    # Update the time and wpm of the player
    player.update_time()
    player.update_wpm()
    # Refresh the display
    view.draw()

# Print game results
if hasattr(player, "opponent_wpm"):  # If multiplayer game
    if player.wpm > player.opponent_wpm:
        print("\nCongratulations! You won!")
    elif player.wpm == player.opponent_wpm:
        print("\nYou... tied??? Good thing our code checks for that!")
    else:
        print("\nWomp womp! You lost!")
    print(f"My wpm: {player.wpm}, Opponent wpm: {player.opponent_wpm}\n")
else:
    print(f"\nGame over. WPM: {player.wpm}")
