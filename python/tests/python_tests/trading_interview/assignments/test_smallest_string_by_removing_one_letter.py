import pytest
from src.python_projects.trading_interview.assignments.smallest_string_by_removing_one_letter import (
    get_smallest_string_by_removing_one_letter,
)

pytestmark = pytest.mark.unit


@pytest.mark.parametrize(
    "s, expected_smallest_string",
    [
        pytest.param("wedding", "edding", id="case_1"),
        pytest.param("house", "hose", id="case_2"),
        pytest.param("trading", "rading", id="case_3"),
        pytest.param("balloon", "ballon", id="case_4"),
    ],
)
def test_get_smallest_string_by_removing_one_letter(s, expected_smallest_string):
    assert get_smallest_string_by_removing_one_letter(s) == expected_smallest_string
