"""
Main file containing game setup and the main loop. Run this file to launch the game.
"""
from model.model import SinglePlayer
from view.view import TextView
from controller.controller import TypeRaceController
from datetime import datetime
from abc import ABC

# User input for single/multi-player
# Initialize MVC classes

# Game over function

# Main game loop:
#   check controller for user input
#   update timer in model
def main():
    """
    Runs all of the classes to make the game playable
    """
    player = SinglePlayer()
    view = TextView(player)

    view.start()
    # while not check or counter == 9:
        # controller1.move()
        # view.draw()
        # check = board.check_win("X")
        # if check:
            # print("Player 1 is the winner")
            # break
        # controller2.move()
        # view.draw()
        # check = board.check_win("O")
        # if check:
            # print("Player 2 is the winner")
    # if counter == 9:
        # print("cat won")
    # counter += 1
main()