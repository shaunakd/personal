import pytest
from src.python_projects.trading_interview.assignments.missing_number import (
    find_missing_number,
)

pytestmark = pytest.mark.unit


@pytest.mark.parametrize(
    "numbers, n, expected_missing_number",
    [
        pytest.param([1, 2, 4, 5, 6], 6, 3, id="case_1"),
        pytest.param([1, 2, 3, 5, 6], 6, 4, id="case_2"),
        pytest.param([1, 2, 3, 4, 6], 6, 5, id="case_3"),
    ],
)
def test_find_missing_number(numbers, n, expected_missing_number):
    assert find_missing_number(numbers, n) == expected_missing_number
