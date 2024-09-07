import pytest
from src.python_projects.trading_interview.assignments.pairs_with_sum import (
    find_pairs_with_sum,
)

pytestmark = pytest.mark.unit


@pytest.mark.parametrize(
    "numbers, target, expected_output",
    [
        pytest.param([3, 4, 2, 5], 7, [(2, 5), (3, 4)], id="case_1"),
        pytest.param([2, 4, 1, 5], 9, [(4, 5)], id="case_2"),
        pytest.param([7, 1, 2, 3, 4, -2, 5], 5, [(1, 4), (2, 3), (7, -2)], id="case_3"),
    ],
)
def test_find_pairs_with_sum(numbers, target, expected_output):
    assert find_pairs_with_sum(numbers, target) == expected_output
