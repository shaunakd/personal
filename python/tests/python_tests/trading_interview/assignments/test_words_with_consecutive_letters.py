import pytest
from src.python_projects.trading_interview.assignments.words_with_consecutive_letters import (
    get_words_with_consecutive_letters,
)


@pytest.mark.parametrize(
    "words, n, expected",
    [
        # All consecutive
        pytest.param(
            ["abc", "def", "ghi"], 3, ["abc", "def", "ghi"], id="all_consecutive"
        ),
        pytest.param(
            ["abcd", "efgh", "ijkl"],
            4,
            ["abcd", "efgh", "ijkl"],
            id="all_consecutive_4",
        ),
        pytest.param(
            ["abc", "def", "xyz"], 2, ["abc", "def", "xyz"], id="all_consecutive_2"
        ),
        # Some consecutive
        pytest.param(["abc", "def", "bed"], 3, ["abc", "def"], id="some_consecutive"),
        # None consecutive
        pytest.param(["ab", "cd", "ef"], 3, [], id="none_consecutive"),
        # Single letter
        pytest.param(["a", "b", "c"], 1, ["a", "b", "c"], id="single_letter"),
        # Actual words
        pytest.param(
            ["definitive", "random", "example"], 3, ["definitive"], id="actual_words"
        ),
        pytest.param(
            ["laughing", "hello", "world"], 3, ["laughing"], id="actual_words_2"
        ),
    ],
)
def test_get_words_with_consecutive_letters(words, n, expected):
    assert get_words_with_consecutive_letters(words, n) == expected
