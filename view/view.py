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
        """
        Initialize the game view with player data and style settings.

        Sets up the Pygame environment, loads style configuration,
        creates the game window, initializes the font, and calculates
        character width for alignment purposes.

        Args:
            player: The player object containing game state information.
        """
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
        # Determine width of characters with surface that is never displayed
        letter_surface = self._font.render("a", True, (255, 255, 255))
        self._letter_width = letter_surface.get_width()

    def text(self):
        """
        Render the main prompt text centered on the screen.

        Fills the background with the specified color, renders the full prompt
        text, and shifts it horizontally based on the number of typed
        characters. Draws a white rectangle to represent the current typing
        position (caret).
        """
        # Draw background
        self._screen.fill(self._style["background_color"])
        # Draw text
        text = self._font.render(
            self._player.prompt_text, False, self._style["text_color"]
        )
        move = (
            len(self._player.typed_text) * self._letter_width
        )  # how much letters shift
        self._screen.blit(
            text,
            (
                (self._style["window_width"]) / 2 - move,
                (self._style["window_height"]) / 2,
            ),
        )
        # Draw rectangle cursor
        pygame.draw.rect(
            self._screen,
            self._style["cursor_color"],
            [415 - self._letter_width, 300, self._letter_width + 5, 40],
            1,
        )

    def underlines(self):
        """
        Draw underlines beneath typed characters to indicate correctness.

        Renders red underlines for mistakes and white underlines for correct
        letters, based on the player's mistake index list. Each underline is
        positioned relative to the typed text and adjusted as more letters are
        typed.
        """
        # Creating either red or white underline under typed letters
        add = self._letter_width  # how much the letters need to shift
        mistakes = self._player.mistake_indexes[: len(self._player.typed_text)][
            ::-1
        ]  # formatting mistakes array
        for i in range(len(self._player.typed_text)):
            color = self._style["correct_underline"]
            if mistakes[i]:
                color = self._style["mistake_underline"]
            pygame.draw.rect(
                self._screen,
                color,
                [417 - self._letter_width - add, 338, self._letter_width, 2],
                19,
            )
            add += self._letter_width

    def info(self):
        """
        Display player stats such as words per minute (WPM) and remaining time.

        Renders and places the WPM and countdown timer text in the top-left
        corner of the screen using the game's font and color settings.
        """
        # The following is for the timer
        time = f"{self._player.time_remaining} seconds left"
        timer = self._font.render(time, False, self._style["text_color"])
        self._screen.blit(
            timer,
            (
                20,
                20,
            ),
        )
        # For player's wpm
        wpm_text = f"{self._player.wpm} WPM"
        wpm = self._font.render(wpm_text, False, self._style["text_color"])
        self._screen.blit(
            wpm,
            (
                20,
                60,
            ),
        )
        # For opponent's wpm
        if hasattr(self._player, "opponent_wpm"):  # If multiplayer game
            color = self._style["text_color"]
            if self._player.opponent_wpm > self._player.wpm:
                color = self._style["alternate_text_color"]
            opp_wpm_text = f"{self._player.opponent_wpm} Opponent WPM"
            opp_wpm = self._font.render(opp_wpm_text, False, color)
            self._screen.blit(
                opp_wpm,
                (
                    20,
                    100,
                ),
            )

    def draw(self):
        """
        Draw all visual elements of the game screen.

        Clears the screen and renders the prompt text, correctness underlines,
        and player information (WPM and timer). Updates the display to show the
        changes.
        """

        self.text()  # text and square around character
        self.underlines()  # Makes underlines
        self.info()  # Makes timer and wpm

        pygame.display.flip()
