"""
Class definitions for the view component of a typing game.

Defines an abstract TextView class that sets up and manages
the graphical display for the game using Pygame.
"""

import pygame
from abc import ABC, abstractmethod


class TypeRaceView(ABC):
    """
    Abstract base class for the game's visual interface.

    Provides a framework for creating and managing the game's display window.
    Subclasses must implement additional drawing functionality as needed.
    """

    def __init__(self, player):
        """
        Initialize the TextView with a reference to the player or game logic.

        Args:
            player: An object representing the player or the game state manager.
        """
        self._player = player

    @property
    def player(self):
        """
        Return the player or game logic object associated with this view.

        Returns:
            The player or game state object.
        """
        return self._player

    @abstractmethod
    def draw(self):
        """
        Update the view according to the current state of the player
        """


class GUIView(TypeRaceView):
    """
    Subclass of TypeRaceView that implements the view for by creating a
    graphical user interface.
    """

    def __init__(self, player):
        super().__init__(player)
        pygame.init()
        screen_width = 800
        screen_height = 600
        self._screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("My Game View")

        self._font = pygame.font.Font(None, 32)
        self._white = (255, 255, 255)
        self._black = (0, 0, 0)

    def draw(self):
        """
        Initialize the Pygame window and display a basic start screen.

        Sets up the screen size, background color, and draws initial elements
        (e.g., a colored rectangle). This method prepares the visual environment
        where the rest of the game will be displayed.
        """

        # Draw text
        self._screen.fill(self._black)  # Fill background with black
        text = self._font.render(
            self._player.typed_text, True, self._white, self._black
        )
        text_rect = text.get_rect()
        text_rect.center = (400, 300)
        self._screen.blit(text, text_rect)

        pygame.display.flip()
