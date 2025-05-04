"""Class definitions for model"""

from datetime import datetime
from model.text_gen import random_paragraph
from model.server import Host, Client


class TypeRacePlayer:
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
        _prompt_text: string representing the paragraph for the user to type

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
        self._start_time = datetime.now()  # Will be overwritten on game start
        self._time_limit = time_limit
        self.game_over = False
        self._typed_text = ""
        self._prompt_text = self.generate_paragraph()
        self._time_remaining = time_limit
        self._wpm = 0
        self._mistake_indexes = [0] * len(self._prompt_text)

    def set_start_time(self):
        """
        Set the start time of the game to the current time.
        """
        self._start_time = datetime.now()

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
        Calculate the user's current wpm by determining how many correct words
        have been typed within the time elapsed.

        Update the wpm property with the new wpm.
        """
        correct_words = self.check_accuracy()

        # Calculate the new wpm
        elapsed_minutes = (self._time_limit - self._time_remaining) / 60
        # Avoid zero division on start up (when the elapsed minutes would be
        # zero)
        if elapsed_minutes > 0:
            self._wpm = int(correct_words // elapsed_minutes)

    def check_accuracy(self):
        """
        Compare the typed text with the prompt text to determine what mistakes
        the user has made and how many correct words have been typed. Update
        the mistake index to indicate which characters are incorrect.

        Return an int representing the number of correct words.
        """
        correct_words = 0
        incorrect_word = False  # Tracks if the current word is incorrect

        for i, typed_char in enumerate(self._typed_text):
            prompt_char = self._prompt_text[i]

            if typed_char == prompt_char:
                self._mistake_indexes[i] = 0
            else:
                incorrect_word = True
                self._mistake_indexes[i] = 1

            if prompt_char == " ":  # End of the word has been reached
                if not incorrect_word:
                    correct_words += 1
                # Reset the incorrect word flag only if the user matched the
                # space, otherwise keep the incorrect word flag set to true for
                # the next word
                if typed_char == " ":
                    incorrect_word = False  # Reset the incorrect word flag
        return correct_words

    def generate_paragraph(self):
        """
        Generate a random paragraph to use as the the prompt for the typing
        race.

        Returns a string representing the entire prompt paragraph for the user
        to type.
        """
        return random_paragraph()

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

    @property
    def prompt_text(self):
        """Get prompt_text"""
        return self._prompt_text


class HostPlayer(TypeRacePlayer):
    """
    Subclass of TypeRacePlayer to represent the host player. Extends the base
    class by printing the local IP address and starting the server.

    Attributes:
        opponent_wpm: int represent the words per minute of the opposing player
        _host: Host object containing the connection to the client
    """

    def __init__(self, time_limit=60):
        """
        Initialize a new host player.
        """
        super().__init__(time_limit)
        self.opponent_wpm = 0
        self._host = Host(self)
        self.display_local_ip()
        self.start_server()

    def display_local_ip(self):
        """
        Print the host's IPv4 address to the terminal so that the client can
        connect.
        """
        print("\nThe host's IPv4 address is:", self._host.get_host_ip(), "\n")

    def start_server(self):
        """
        Instruct Host to start the server and start the thread that will
        continuously exchange words per minute with the client.
        """
        self._host.start_server()


class ClientPlayer(TypeRacePlayer):
    """
    Subclass of TypeRacePlayer to represent the client player. Extends the base
    class by connecting to the server.

    Attributes:
        opponent_wpm: int represent the words per minute of the opposing player
        _client: Client object containing the connection to the host
    """

    def __init__(self, time_limit=60):
        """
        Initialize a new client player.
        """
        super().__init__(time_limit)
        self.opponent_wpm = 0
        self._client = Client(self)
        self.connect_server()

    def connect_server(self):
        """
        Instruct Client to connect to the server and start the thread that will
        continuously exchange words per minute with the host.
        """
        self._client.connect_server()
