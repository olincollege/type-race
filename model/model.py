"""Class definitions for model"""

from abc import ABC
from text_gen import random_paragraph

class TypeRacePlayer(ABC):
    """
    Create an abstract base class representing the state of Type Race player.

    Properties:
        _typed_text: string representing all the text the user has typed up to
            the current point in the game
        _time_remaining: int representing the number of seconds left before time
            is up
        _wpm: integer representing the user's current wpm adjusted for errors
    """
    def __init__(self, view, time_limit=60):
        """
        Create a new model representing the state of a player at the 
        beginning of a new game.

        Args:
            view: instance of the view class used to update the user interface
            time_limit: int representing the number of seconds to start the game
                with. If not provided, default to 60 seconds.
        """
        self._time_remaining = time_limit
        self._typed_text = ""
        self._wpm = 0

    def new_char(self, char):
        """
        Update the typed text when the controller receives a new input from the
        user.

        Args:
            char: string representing the last character typed by a user
        """
        self._typed_text += char

    def update_wpm(self):
        """
        Calculate the user's current wpm by comparing the prompt text to the
        typed text of the user. Update the wpm property.
        """
        pass

    @property
    def time_remaining(self):
        return self._time_remaining
    
    @property
    def typed_text(self):
        return self._typed_text
    
    @property
    def wpm(self):
        return self._wpm
    
class SinglePlayer(TypeRacePlayer):
    def generate_paragraph(self):
        """
        Generate a random paragraph to use as the the prompt for the typing race
        """
        self._prompt_text = random_paragraph()

class HostPlayer(TypeRacePlayer):
    def generate_paragraph(self):
        """
        Generate a random paragraph to use as the the prompt for the typing race
        """
        self._prompt_text = random_paragraph()

class ClientPlayer(TypeRacePlayer):
    pass
