"""
Class definitions for the controller component of a typing game.

Defines abstract and concrete controller classes for managing player input
and updating the game state based on keyboard interactions.
"""

from abc import ABC, abstractmethod
import pygame


class TypeRaceController(ABC):
    """
    Abstract base class for a typing game's controller.

    This class provides an interface for handling player input
    and updating the game state. Subclasses must implement
    the `typechecker` method to define specific input handling behavior.

    Attributes:
        _player: Instance of TypeRacePlayer associated with the controller
        _active_string: string representing all text typed by the user
    """

    def __init__(self, player):
        """
        Initialize the TypeRaceController with a reference to the player or
        game logic.

        Args:
            player: An object representing the player or game state manager.
        """
        self._player = player
        self._active_string = ""

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

        # Iterate through each 'event' recorded by pygame
        for event in pygame.event.get():
            # If the user closed the game window, set the game_over flag to True
            if event.type == pygame.QUIT:
                self._player.game_over = True

            # If the user pressed a key on the keyboard
            if event.type == pygame.KEYDOWN:
                # If the key pressed was a letter, add to active string
                if event.unicode.lower().isalpha():
                    self._active_string += event.unicode

                # If backspace was pressed and the user has previously typed
                # input, remove the last typed input from the active string
                if (
                    event.key == pygame.K_BACKSPACE
                    and len(self._active_string) > 0
                ):
                    self._active_string = self._active_string[:-1]

                # If the spacebar was pressed, add a space to the active string
                if event.key == pygame.K_SPACE:
                    self._active_string += " "
        # Update the player with the new active string
        self._player.update_text(self._active_string)
