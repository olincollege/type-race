"""
Class definitions for the view component of a typing game.

Defines an abstract TextView class that sets up and manages 
the graphical display for the game using Pygame.
"""

import pygame
from abc import ABC, abstractmethod

class TextView(ABC):
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

    def start(self):
        """
        Initialize the Pygame window and display a basic start screen.

        Sets up the screen size, background color, and draws initial elements
        (e.g., a colored rectangle). This method prepares the visual environment
        where the rest of the game will be displayed.
        """
        pygame.init()
        screen_width = 800
        screen_height = 600
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("My Game View")
        screen.fill((0, 0, 0))  # Fill background with black

        # Draw a placeholder red square
        pygame.draw.rect(screen, (255, 0, 0), (100, 100, 50, 50))

        pygame.display.flip()
