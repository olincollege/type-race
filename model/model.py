"""Class definitions for model"""

from abc import ABC, abstractmethod
from datetime import datetime
from model.text_gen import random_paragraph


class TypeRacePlayer(ABC):
    """
    Create an abstract base class representing the state of Type Race player.

    Attributes:
        _start_time: datetime object representing the time the game was started
        _time_limit: int representing the number of seconds the game should
            play for. Defaults to 60, but can be overridden upon the definition
            of the class
        game_over: bool representing whether or not the game is over

    Properties:
        _typed_text: string representing all the text the user has typed up to
            the current point in the game
        _prompt_text: string representing the paragraph for the user to copy
        _time_remaining: int representing the number of seconds left before time
            is up
        _wpm: integer representing the user's current wpm adjusted for errors
    """

    def __init__(self, time_limit=60):
        """
        Create a new model representing the state of a player at the
        beginning of a new game. Set all attributes and properties to their
        default values.

        Args:
            time_limit: int representing the number of seconds to start the game
                with. If not provided, default to 60 seconds.
        """
        self._start_time = datetime.now()
        self._time_limit = time_limit
        self.game_over = False
        self._typed_text = ""
        self._prompt_text = self.generate_paragraph()
        self._time_remaining = time_limit
        self._wpm = 0
        self._mistake_indexes = []

    def update_text(self, text):
        """
        Called by the controller when a new user input is received. Acts as a
        setter method.

        Args:
            text: string representing all text entered by the user
        """
        self._typed_text = text

    def update_time(self):
        """
        Update the amount of time remaining by comparing the current system
        time with the start time.

        Update the time_remaining property. If there is no more time remaining,
        set the game over flag to True.
        """
        # Compare the current time with the start time to determine how much
        # time has elapsed
        time_delta = datetime.now() - self._start_time
        # Turn time elapsed into time remaining
        self._time_remaining = self._time_limit - time_delta.seconds

        # If there is no time remaining, set the game over flag to True
        if self._time_remaining <= 0:
            self.game_over = True

    def update_wpm(self):
        """
        Calculate the user's current wpm by comparing the prompt text to the
        typed text of the user.

        Update the wpm property with the new wpm. Store all mistakes in a list containing the index corresponding to the word where the user made a mistake.
        """
        # Split the prompt and typed text into a list of words, removing blank
        # spaces and new lines
        prompt_list = self._prompt_text.replace("\n", "").split(" ")
        typed_list = self._typed_text.strip().split(" ")

        correct_words = 0

        # Iterate through the number of words that have been typed
        for i, typed_word in enumerate(typed_list):
            if typed_word == prompt_list[i]:  # If the typed word was correct
                correct_words += 1
            else:  # If the typed word was incorrect
                self._mistake_indexes.append(i)

        

        # Calculate the new wpm
        elapsed_minutes = (self._time_limit - self._time_remaining) / 60
        # Avoid zero division on start up (when the elapsed minutes would be
        # zero)
        if elapsed_minutes > 0:
            self._wpm = correct_words // elapsed_minutes

    @property
    def time_remaining(self):
        """Get time_remaining"""
        return self._time_remaining

    @property
    def typed_text(self):
        """Get typed_text"""
        return self._typed_text

    @property
    def wpm(self):
        """Get wpm"""
        return self._wpm

    @property
    def mistake_indexes(self):
        """Get error array"""
        return self._mistake_indexes

    @abstractmethod
    def generate_paragraph(self):
        """
        Generic method to generate the prompt text paragraph. Must be
        implemented in a subclass.

        Returns a string representing the entire prompt paragraph for the user
        to type.
        """


class SinglePlayer(TypeRacePlayer):
    """
    Subclass of TypeRacePlayer to play a single player game of Type Player.

    Properties:
        _prompt_text: string representing the paragraph for the user to type
    """

    def generate_paragraph(self):
        """
        Generate a random paragraph to use as the the prompt for the typing
        race.

        Returns a string representing the entire prompt paragraph for the user
        to type.
        """
        return random_paragraph()

    @property
    def prompt_text(self):
        """Get prompt_text"""
        return self._prompt_text
