from pathlib import Path
import pytest
from projects.python_projects.trading_interview.assignments.word_frequency import (
    read_file,
    word_frequency,
    filter_text,
)


@pytest.fixture
def text():
    return read_file(Path(__file__).parent / "test_word_frequency_text.txt")


def test_filter_text(text):
    expected_output = "this text is test text for word frequency aim of word frequency function is to count number of words file return dictionary mapping words this file to how many times word appears newline characters digits special characters generally everything non alphabetic must be removed additionally all capitals will be made lowercase from this to this function may also remove common prepositions such well see what did there so on so forth"
    assert filter_text(text) == expected_output


@pytest.fixture
def filtered_text(text):
    test_filter_text(text)
    return filter_text(text)


def test_word_frequency(filtered_text):
    expected_output = {}
    assert word_frequency(filtered_text)
