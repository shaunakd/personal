from pathlib import Path
import pytest
from src.python_projects.trading_interview.assignments.word_frequency import (
    read_file,
    word_frequency,
    filter_text,
)


@pytest.fixture
def text():
    return read_file(Path(__file__).parent / "test_word_frequency_text.txt")


@pytest.fixture
def filtered_text(text):
    return filter_text(text)


def test_filter_text(text):
    expected_output = """this text is test text for word frequency aim of word frequency function is to count number of words file return dictionary mapping words
                    this file to how many times word appears newline characters digits special characters generally everything non alphabetic must be removed additionally
                    all capitals will be made lowercase from this to this function may also remove common prepositions such well see what did there so on so forth"""
    assert filter_text(text) == expected_output


def test_word_frequency(filtered_text):
    expected_output = {
        "remove": 1,
        "generally": 1,
        "be": 2,
        "now": 2,
        "non": 1,
        "such": 1,
        "aim": 1,
        "made": 1,
        "test": 1,
        "did": 1,
        "so": 2,
        "more": 1,
        "appears": 1,
        "all": 1,
        "is": 2,
        "alphabetic": 1,
        "removed": 1,
        "number": 1,
        "for": 4,
        "there": 1,
        "dictionary": 1,
        "special": 1,
        "function": 2,
        "many": 1,
        "everything": 1,
        "newline": 1,
        "up": 8,
        "text": 2,
        "to": 3,
        "what": 1,
        "sake": 1,
        "capitals": 1,
        "file": 2,
        "will": 2,
        "may": 1,
        "times": 1,
        "count": 1,
        "well": 1,
        "digits": 1,
        "prepositions": 1,
        "characters": 2,
        "this": 4,
        "return": 1,
        "common": 1,
        "on": 1,
        "mapping": 1,
        "of": 3,
        "additionally": 1,
        "word": 3,
        "add": 5,
        "lowercase": 1,
        "words": 3,
        "beefing": 1,
        "frequency": 12,
        "also": 1,
        "forth": 1,
        "from": 1,
        "must": 1,
        "how": 1,
        "see": 1,
    }
    with open(Path(__file__).parent / "test.txt", "w") as file:
        file.write(str(word_frequency(filtered_text)))
    assert word_frequency(filtered_text) == expected_output
