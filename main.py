"""
Main file containing game setup and the main loop. Run this file to launch the
game.
"""

from model.model import SinglePlayer
from view.view import GUIView
from controller.controller import TextController

# User input for single/multi-player
# game_mode = input("Enter 's' for single player or 'm' for multiplayer: ")

# Initialize MVC classes
player = SinglePlayer()
view = GUIView(player)
controller = TextController(player)

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
