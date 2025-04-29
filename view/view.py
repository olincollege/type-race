"""
Class definitions for the view component of a typing game.

Defines an abstract TextView class that sets up and manages
the graphical display for the game using Pygame.
"""

from abc import ABC, abstractmethod
import pygame
from view.gui import style_settings


class TypeRaceView(ABC):
    """
    Abstract base class for the game's visual interface.

    Provides a framework for creating and managing the game's display window.
    Subclasses must implement additional drawing functionality as needed.

    Attributes:
        _player: TypeRacePlayer object representing the player linked to this
            view
    """

    def __init__(self, player):
        """
        Initialize the TextView with a reference to the player or game logic.

        Args:
            player: An object representing the player or the game state manager.
        """
        self._player = player

    @abstractmethod
    def draw(self):
        """
        Update the view according to the current state of the player
        """


class GUIView(TypeRaceView):
    """
    Subclass of TypeRaceView that implements the view for by creating a
    graphical user interface.

    Attributes:
        _style: dict containing style settings for GUI view
        _screen: pygame display object representing the GUI's window
        _font: pygame font object representing the chosen font
        _letter_width: int representing the length of each character of the
            font in pixels
    """

    def __init__(self, player):
        # Get the player object from the abstract base class
        super().__init__(player)
        # Start pygame
        pygame.init()
        # Get the style settings dict
        self._style = style_settings

        # Set up pygame window according to settings
        self._screen = pygame.display.set_mode(
            (self._style["window_width"], self._style["window_height"])
        )
        pygame.display.set_caption(self._style["window_caption"])

        # Set up font attribute
        self._font = pygame.font.Font(
            self._style["font_path"], self._style["font_size"]
        )
        # Determine width of characters
        letter_surface = self._font.render("a", True, (255, 255, 255))
        self._letter_width = letter_surface.get_width()

    def draw(self):
        """
        Initialize the Pygame window and display a basic start screen.

        Sets up the screen size, background color, and draws initial elements
        (e.g., a colored rectangle). This method prepares the visual environment
        where the rest of the game will be displayed.
        """

        # Draw text
        self._screen.fill(self._style["background_color"])
        text = self._font.render(
            self._player.prompt_text, False, self._style["prompt_text_color"]
        )
        move = len(self._player.typed_text) * self._letter_width
        self._screen.blit(
            text,
            (
                (self._style["window_width"]) / 2 - move,
                (self._style["window_height"]) / 2,
            ),
        )

        pygame.display.flip()
