"""
Class definitions for the controller component of a typing game.

Defines abstract and concrete controller classes for managing player input
and updating the game state based on keyboard interactions.
"""

import pygame
from abc import ABC, abstractmethod


class TypeRaceController(ABC):
    """
    Abstract base class for a typing game's controller.

    This class provides an interface for handling player input
    and updating the game state. Subclasses must implement
    the `typechecker` method to define specific input handling behavior.
    """

    def __init__(self, player):
        """
        Initialize the TypeRaceController with a reference to the player or
        game logic.

        Args:
            player: An object representing the player or game state manager.
        """
        self._player = player
        self.active_string = ""

    @property
    def player(self):
        """
        Return the player or game logic object associated with this controller.

        Returns:
            The player or game state object.
        """
        return self._player

    @abstractmethod
    def typechecker(self):
        """
        Abstract method for handling user input.

        Subclasses must implement this method to define how user input
        is processed and how the game state should be updated accordingly.
        """


class TextController(TypeRaceController):
    """
    Concrete controller class for handling keyboard input in a typing game.

    Captures letter keystrokes, spaces, and backspaces,
    builds the current input string, and updates the game state based on the typed text.
    """

    def typechecker(self):
        """
        Handle keyboard events to build the player's active input string.

        Listens for keypress events:
        - Appends typed alphabet letters to the active input string.
        - Handles backspace to delete the last character.
        - Adds a space character when the spacebar is pressed.

        After processing input, updates the player's displayed text.
        """
        player = self._player
        letters = [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
        ]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                player.game_over = True
            if event.type == pygame.KEYDOWN:
                if event.unicode.lower() in letters:
                    self.active_string += event.unicode
                if (
                    event.key == pygame.K_BACKSPACE
                    and len(self.active_string) > 0
                ):
                    self.active_string = self.active_string[:-1]
                if event.key == pygame.K_SPACE:
                    self.active_string += " "
        player.update_text(self.active_string)
