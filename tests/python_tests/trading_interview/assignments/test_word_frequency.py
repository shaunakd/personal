import pytest
from projects.python_projects.trading_interview.assignments.word_frequency import read_file, word_frequency, sort_by_frequency

@pytest.fixture
def text():
    return read_file("test_word_frequency_text.txt")

def test_word_frequency(text):
    expected_output = {}
    assert word_frequency(text) == expected_output