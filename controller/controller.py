"""Class definitions for controller"""
import pygame
from abc import ABC, abstractmethod


class TypeRaceController(ABC):
    """
    Abstract base class for a Tic Tac Toe game controller.

    This class defines the interface for a Tic Tac Toe
    controller, which is responsible
    for managing the game board and handling player moves.
    Subclasses must implement
    the `move` method to define how moves are made in the game.
    """

    def __init__(self, player):
        """
        Initialize the Tic Tac Toe controller with a game board.

        Args:
            board: An instance of a board class that represents
              the Tic Tac Toe game board.
        """
        self._player = player
        self.active_string = ''

    @property
    def player(self):
        """
        Get the current game board.

        Returns:
            The current state of the game board.
        """
        return self._player

    @abstractmethod
    def typechecker(self):
        """
        Abstract method to make a move in the game.

        Subclasses must implement this method to define
        how a player makes a move
        on the game board.
        """


class TextController(TypeRaceController):
    """
    A text-based controller for a Tic Tac Toe game.

    This controller allows players to make moves by
    entering text input in the format
    of row and column numbers. It validates the input
    and updates the game board accordingly.
    """


    def typechecker(self):
        """
        Prompt the player to enter a move and update the
        game board.

        This method repeatedly asks the player to enter
        a move in the format "row col".
        It validates the input to ensure it is within the
        board's bounds and that the
        chosen square is not already marked. If the input
        is valid, it updates the board.
        """
        player = self._player
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
           'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.unicode.lower() in letters:
                    self.active_string += event.unicode
            if event.key == pygame.K_BACKSPACE and len(self.active_string) > 0:
                self.active_string = self.active_string[:-1]
            if event.key == pygame.K_SPACE:
                self.active_string += ' '
        player.update_text(self.active_string)
        return True