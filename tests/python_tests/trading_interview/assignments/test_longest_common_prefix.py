import pytest
from src.python_projects.trading_interview.assignments.longest_common_prefix import (
    get_longest_common_prefix,
)

pytestmark = pytest.mark.unit


@pytest.mark.parametrize(
    "words, expected",
    [
        # Common prefix scenarios
        pytest.param(["flower", "flow", "flight"], "fl", id="common_prefix_fl"),
        pytest.param(
            ["interspecies", "interstellar", "interstate"],
            "inters",
            id="common_prefix_inters",
        ),
        pytest.param(["prefix", "pretest", "pre"], "pre", id="common_prefix_pre"),
        pytest.param(["apple", "ape", "april"], "ap", id="common_prefix_ap"),
        pytest.param(["longest", "longer", "long"], "long", id="common_prefix_long"),
        pytest.param(
            ["short", "shorter", "shortest"], "short", id="common_prefix_short"
        ),
        pytest.param(["same", "same", "same"], "same", id="all_words_same"),
        pytest.param(
            ["prefix", "prefixes", "prefixation"], "prefix", id="common_prefix_prefix"
        ),
        pytest.param(
            ["common", "commute", "communication"], "comm", id="common_prefix_comm"
        ),
        # No common prefix scenarios
        pytest.param(["dog", "racecar", "car"], "", id="no_common_prefix"),
        pytest.param(["throne", "dungeon"], "", id="completely_different_words"),
        pytest.param(["", "b"], "", id="empty_string_and_non_empty_string"),
        pytest.param(["", ""], "", id="two_empty_strings"),
        pytest.param(
            ["different", "words", "here"], "", id="no_common_prefix_different_words"
        ),
        pytest.param(["", "a", "ab"], "", id="empty_string_among_non_empty_strings"),
        # Single word scenarios
        pytest.param(["a"], "a", id="single_character_word"),
        pytest.param(["ab", "a"], "a", id="prefix_is_single_character"),
        pytest.param(["a", "a", "a"], "a", id="multiple_single_character_words"),
    ],
)
def test_get_longest_common_prefix(words, expected):
    assert get_longest_common_prefix(words) == expected
