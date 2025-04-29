"""Generate a paragraph of text for all players to type."""

import random
from model.word_list import words


def random_paragraph():
    """
    Generate a random paragraph of 200 words from the word list in word_list.py.

    Returns a string representing all the words in the paragraph.
    """
    # Create a list of 200 randomly chosen words from the word list
    random_words = random.choices(words, k=200)
    # Join all words in the list and separate with spaces.
    return " ".join(random_words)


def sample_paragraph():
    """
    Pre-set paragraph of 200 words without punctuation.

    Returns a string representing all the words in the paragraph.
    """

    return """cloud amber window stream fabric circle wander jungle paper breeze
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
