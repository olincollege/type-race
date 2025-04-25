"Class definitions for view"
import pygame

from abc import ABC, abstractmethod


class TextView(ABC):
    """
    Abstract base class for a Tic Tac Toe
      game view.

    This class defines the interface for a Tic
      Tac Toe view, which is responsible
    for displaying the game board to the player.
    Subclasses must implement the `draw`
    method to define how the board is presented.
    """

    def __init__(self, player):
        """
        Initialize the Tic Tac Toe view with a game board.

        Args:
            board: An instance of a board class that
            represents the Tic Tac Toe game board.
        """
        self._player = player
        pygame.init()

    @property
    def player(self):
        """
        Get the current game board.

        Returns:
            The current state of the game board.
        """
        return self._player

    @abstractmethod
    def draw(self):
        """
        Abstract method to draw the game board.

        Subclasses must implement this method to
        define how the game board is displayed
        to the player.
        """


class GameScreen(TextView):
    """
    A text-based view for a Tic Tac Toe game.

    This view displays the game board and indicates
    whose turn it is using text output.
    """

    def draw(self):
        """
        Display the current game board and indicate
        the next player's turn.

        This method prints the current state of the
          game board and informs the player
        whose turn it is to make the next move.
        """

        # Set up display (this is your view)
        screen_width = 800
        screen_height = 600
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("My Game View")
        # Fill screen with a background color
        screen.fill((0, 0, 0))  # black

        pygame.draw.rect(screen, (255, 0, 0), (100, 100, 50, 50))  # red square

        # Update the screen
        pygame.display.flip()
