import json
import pytest
from pathlib import Path
from src.python_projects.trading_interview.assignments.word_frequency import (
    group_words_by_frequency,
    read_text_file,
    filter_text,
    word_frequency,
)
from src.python_projects.utils.utils import read_file

pytestmark = pytest.mark.unit

ROOT_DIR = Path(__file__).parent / "cases"


@pytest.mark.parametrize(
    "test_dir, expected_output",
    [
        pytest.param(ROOT_DIR / "empty_text_file", "", id="empty_text_file"),
        pytest.param(ROOT_DIR / "no_text_file", None, id="no_text_file"),
        pytest.param(
            ROOT_DIR / "text_file_exists",
            "this text is test text for word frequency aim of word frequency function is to count number of words file return dictionary mapping words this file to how many times word appears newline characters digits special characters generally everything non alphabetic must be removed additionally all capitals will be made lowercase from this to this function may also remove common prepositions such well see what did there so on so forth now now will add add add add add more words for for for sake of beefing up up up up up up up up frequency frequency frequency frequency frequency frequency frequency frequency frequency frequency",
            id="text_file_exists",
        ),
    ],
)
def test_filter_text(test_dir, expected_output):
    text = read_text_file(test_dir / "text.txt")
    actual_output = filter_text(text)
    assert actual_output == expected_output
    if actual_output:
        with open(ROOT_DIR / "filtered_text.txt", "r+") as file:
            if actual_output != file.read():
                file.write(actual_output)


def test_word_frequency(test_name, expected_output):
    filtered_text = read_text_file(ROOT_DIR / "filtered_text.txt")
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
    actual_output = word_frequency(filtered_text)
    assert actual_output == expected_output
    if actual_output:
        with open(ROOT_DIR / "word_frequency_output.json", "r+") as file:
            if actual_output != json.load(file):
                file.write(json.dumps(actual_output))


def test_group_words_by_frequency(test_name, expected_output):
    word_freq = read_file(ROOT_DIR / "word_frequency_output.json")
    expected_output = {
        (
            "additionally",
            "aim",
            "all",
            "alphabetic",
            "also",
            "appears",
            "beefing",
            "capitals",
            "common",
            "count",
            "dictionary",
            "did",
            "digits",
            "everything",
            "forth",
            "from",
            "generally",
            "how",
            "lowercase",
            "made",
            "many",
            "mapping",
            "may",
            "more",
            "must",
            "newline",
            "non",
            "number",
            "on",
            "prepositions",
            "remove",
            "removed",
            "return",
            "sake",
            "see",
            "special",
            "such",
            "test",
            "there",
            "times",
            "well",
            "what",
        ): 1,
        ("be", "characters", "file", "function", "is", "now", "so", "text", "will"): 2,
        ("of", "to", "word", "words"): 3,
        ("for", "this"): 4,
        "add": 5,
        "up": 8,
        "frequency": 12,
    }
    actual_output = group_words_by_frequency(word_freq)
    assert actual_output == expected_output
