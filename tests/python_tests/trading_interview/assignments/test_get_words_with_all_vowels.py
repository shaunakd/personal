import pytest
from projects.python_projects.trading_interview.assignments.words_with_all_vowels import get_words_with_all_vowels

pytestmark = pytest.mark.unit

@pytest.mark.parametrize(
    "words, expected_output",
    [
        pytest.param(["car", "multidirectional", "hello", "overqualified", "university"], ["multidirectional", "overqualified"], id="case_1")
    ]
)
def test_get_words_with_all_vowels(words, expected_output):
    assert get_words_with_all_vowels(words) == expected_output