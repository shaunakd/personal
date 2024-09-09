import pytest

from src.python_projects.hackerrank.problem_solving.algorithms.easy.between_two_sets import (
    get_numbers_between,
)

pytestmark = pytest.mark.unit


@pytest.mark.parametrize(
    "factors, multiples, expected_output",
    [
        pytest.param([2, 4], [16, 32, 96], [4, 8, 16], id="case_1"),
        pytest.param([3, 4], [24, 48], [12, 24], id="case_2"),
    ],
)
def test_get_numbers_between(factors, multiples, expected_output):
    assert get_numbers_between(factors, multiples) == expected_output
