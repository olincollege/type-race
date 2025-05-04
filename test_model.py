"""
Unit tests for Sleepy Follow user account class.
"""

import pytest
from model.model import SinglePlayer
from unittest.mock import patch
from datetime import timedelta

@pytest.fixture
def player():
    """
    Fixture that returns a new instance of SinglePlayer with a 60-second 
    time limit.
    """
    return SinglePlayer(time_limit=60)

def test_update_text(player):
    """
    Test that calling update_text correctly updates the player's typed_text.
    """
    sample_input = "This is a test"
    player.update_text(sample_input)
    assert player.typed_text == sample_input

@patch("model.model.datetime")
def test_update_time_game_over(mock_datetime, player):
    """
    Test that update_time sets game_over to True when time runs out.
    """
    mock_datetime.now.return_value = player._start_time + timedelta(seconds=70)
    player.update_time()
    assert player.time_remaining <= 0
    assert player.game_over is True


@patch("model.model.datetime")
def test_wpm(mock_datetime, player):
    """
    Test that update_wpm correctly calculates WPM based on typed correct 
    words and elapsed time.
    """
    mock_datetime.now.return_value = player._start_time + timedelta(seconds=30)
    player.update_time()
    player._prompt_text = 'this is my test sentence '
    player.update_text('this is my test sentence ')
    player.update_time()
    player.update_wpm()
    assert player.time_remaining == 30
    assert  player.wpm == 10  # 5 words in 0.5 minutes = 10 WPM

def test_check_accuracy_all_correct(player):
    """
    Test check_accuracy when all typed text matches the prompt text.
    Should result in all zeros in mistake_indexes and positive 
    correct_words count.
    """
    player.update_text(player.prompt_text)
    correct_words = player.check_accuracy()
    assert all(i == 0 for i in player.mistake_indexes)
    assert correct_words > 0

def test_check_accuracy_all_incorrect(player):
    """
    Test check_accuracy when the typed text does not match any part of the 
    prompt.

    This test ensures that if the user types a completely incorrect string,
    the method correctly identifies zero correct words and marks all necessary
    characters as incorrect.
    """
    player.update_text('Wow I am almost ten words long')
    correct_words = player.check_accuracy()
    assert correct_words == 0


def test_generate_paragraph(player):
    """
    Test that generate_paragraph returns a non-empty string.
    """
    paragraph = player.generate_paragraph()
    assert isinstance(paragraph, str)
    assert len(paragraph) > 0
