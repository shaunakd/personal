import pytest

from src.python_projects.hackerrank.problem_solving.algorithms.easy.breaking_records import (
    get_number_of_broken_records,
)


pytestmark = pytest.mark.unit


@pytest.mark.parametrize(
    "scores, expected_output",
    [
        pytest.param([10, 5, 20, 20, 4, 5, 2, 25, 1], (2, 4), id="case_1"),
        pytest.param([3, 4, 21, 36, 10, 28, 35, 5, 24, 42], (4, 0), id="case_2"),
    ],
)
def test_get_number_of_records_broken(scores, expected_output):
    assert get_number_of_broken_records(scores) == expected_output
