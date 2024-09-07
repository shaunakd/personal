import json
from pathlib import Path
from src.python_projects.trading_interview.assignments.word_frequency import (
    read_text_file,
    filter_text,
    word_frequency,
)
from src.python_projects.utils.utils import read_file

DATA_DIR = Path(__file__).parent / "data"


def test_filter_text():
    text = read_text_file(DATA_DIR / "text.txt")
    expected_output = "this text is test text for word frequency aim of word frequency function is to count number of words file return dictionary mapping words this file to how many times word appears newline characters digits special characters generally everything non alphabetic must be removed additionally all capitals will be made lowercase from this to this function may also remove common prepositions such well see what did there so on so forth now now will add add add add add more words for for for sake of beefing up up up up up up up up frequency frequency frequency frequency frequency frequency frequency frequency frequency frequency"
    actual_output = filter_text(text)
    assert actual_output == expected_output
    with open(DATA_DIR / "filtered_text.txt", "w") as file:
        file.write(actual_output)


def test_word_frequency():
    filtered_text = read_text_file(DATA_DIR / "filtered_text.txt")
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
    with open(DATA_DIR / "word_frequency_output.json", "w") as file:
        file.write(json.dumps(actual_output))


def test_group_words_by_frequency():
    word_freq = read_file(DATA_DIR / "word_frequency_output.json")
