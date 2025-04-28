"""Class definitions for model"""

from abc import ABC, abstractmethod
from datetime import datetime
#from text_gen import random_paragraph


class TypeRacePlayer(ABC):
    """
    Create an abstract base class representing the state of Type Race player.

    Attributes:
        _start_time: datetime object representing the time the game was started

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
        beginning of a new game.

        Args:
            time_limit: int representing the number of seconds to start the game
                with. If not provided, default to 60 seconds.
        """
        self._time_remaining = time_limit
        self._typed_text = ""
        self._prompt_text = self.generate_paragraph()
        self._wpm = 0

    def update_text(self, text):
        """
        Called by the controller when a new user input is received

        Args:
            text: string representing all typed text by the user
        """
        self._typed_text = text

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

    @abstractmethod
    def generate_paragraph(self):
        """Generic method to generate the prompt text paragraph"""


class SinglePlayer(TypeRacePlayer):
    def generate_paragraph(self):
        """
        Generate a random paragraph to use as the the prompt for the typing race
        """
        self._prompt_text = """
            Cloud amber window stream fabric circle wander jungle paper breeze 
            silver giant button cradle violet candle motion flame garden bridge 
            silent lunar glow travel sunset whisper canvas shadow moment ocean 
            crystal whistle marble castle dream echo ribbon forest hidden puzzle
             rocket anchor valley thread boulder flicker gentle feather hazel 
            wool nectar canyon drift hollow latch grain wanderer bubble streamer
             twilight dew petal granite serene lantern meadow ember cotton 
            harbor magnet vine stone cabin dust ripple carpet nest loop cloak 
            sapphire firefly fern shimmer paddle flute wheat ladder icicle 
            blossom glisten raven echoes sparkle cliff cork beacon horizon cave 
            tunnel cloakroom reed lilac breeze island branch crush path butter 
            fog saddle twig reed apron daisy cloak moss rubble hill cobble 
            sprout slope mint coral twig nestle shell current boulder sketch 
            scroll quartz reed latch parchment silk shard pebble swirl dune echo
             gleam murmur breeze wood puddle twig thicket veil drizzle frost 
            cypress branch oak maple straw torch grove tide clay knoll stream 
            trail log pebble smoke chime veil marsh mist root fern shade brook 
            bark bramble wisp bloom flick lumen gust zephyr glade briar ridge 
            flint mire reed
        """

    @property
    def prompt_text(self):
        return self._prompt_text


class HostPlayer(TypeRacePlayer):

    def generate_paragraph(self):
        """
        Generate a random paragraph to use as the the prompt for the typing race
        """
        self._prompt_text = random_paragraph()


class ClientPlayer(TypeRacePlayer):
    pass
