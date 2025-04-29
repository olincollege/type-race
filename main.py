"""
Main file containing game setup and the main loop. Run this file to launch the
game.
"""

from model.model import SinglePlayer
from view.view import GUIView
from controller.controller import TextController
from datetime import datetime

# User input for single/multi-player
# game_mode = input("Enter 's' for single player or 'm' for multiplayer: ")

# Initialize MVC classes
player = SinglePlayer()
view = GUIView(player)
controller = TextController(player)

# Main game loop:
while True:
    if player.game_over:
        break
    controller.typechecker()
    view.draw()
