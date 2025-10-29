import pytest
from src.python_projects.trading_interview.assignments.subarray_sum_equals_zero import (
    solution,
)


@pytest.mark.parametrize(
    "numbers, expected",
    [
        pytest.param(
            [2, -2, 3, 0, 4, -7],
            [[0], [2, -2], [3, 0, 4, -7], [2, -2, 3, 0, 4, -7]],
            id="Subarray with multiple zero-sum combinations",
        ),
        pytest.param(
            [1, 2, -3, 3, -3, 3],
            [
                [-3, 3],
                [-3, 3],
                [3, -3],
                [1, 2, -3],
                [-3, 3, -3, 3],
                [1, 2, -3, 3, -3],
            ],
            id="Multiple zero-sum pairs with duplicates",
        ),
        pytest.param(
            [0, 0, 0],
            [[0], [0], [0], [0, 0], [0, 0], [0, 0, 0]],
            id="All zeros in the array",
        ),
        pytest.param([1, 2, 3], [], id="No zero-sum subarrays present"),
        pytest.param(
            [1, -1, 1, -1],
            [[-1, 1], [1, -1], [1, -1], [1, -1, 1, -1]],
            id="Alternating positive and negative ones",
        ),
        pytest.param(
            [10000, -10000],
            [[10000, -10000]],
            id="Single zero-sum pair with large numbers",
        ),
        pytest.param(
            [1, -1, 2, -2, 3, -3],
            [
                [1, -1],
                [2, -2],
                [3, -3],
                [1, -1, 2, -2],
                [2, -2, 3, -3],
                [1, -1, 2, -2, 3, -3],
            ],
            id="Multiple zero-sum pairs with distinct values",
        ),
        pytest.param(
            [1, -1, 2, -2, 3, -3, 4, -4],
            [
                [1, -1],
                [2, -2],
                [3, -3],
                [4, -4],
                [1, -1, 2, -2],
                [2, -2, 3, -3],
                [3, -3, 4, -4],
                [1, -1, 2, -2, 3, -3],
                [2, -2, 3, -3, 4, -4],
                [1, -1, 2, -2, 3, -3, 4, -4],
            ],
            id="Multiple zero-sum pairs with larger set",
        ),
        pytest.param(
            [1, 2, 3, -6, 4, -4],
            [[4, -4], [1, 2, 3, -6], [1, 2, 3, -6, 4, -4]],
            id="Zero-sum subarrays with positive and negative mix",
        ),
        pytest.param(
            [1, 2, 3, -3, -2, -1],
            [[3, -3], [2, 3, -3, -2], [1, 2, 3, -3, -2, -1]],
            id="Zero-sum subarrays with consecutive negatives",
        ),
        pytest.param(
            [1, 2, 3, -3, -2, -1, 1, 2, 3, -3, -2, -1],
            [
                [-1, 1],
                [3, -3],
                [3, -3],
                [-2, -1, 1, 2],
                [2, 3, -3, -2],
                [2, 3, -3, -2],
                [-3, -2, -1, 1, 2, 3],
                [-2, -1, 1, 2, 3, -3],
                [-1, 1, 2, 3, -3, -2],
                [1, 2, 3, -3, -2, -1],
                [1, 2, 3, -3, -2, -1],
                [2, 3, -3, -2, -1, 1],
                [3, -3, -2, -1, 1, 2],
                [3, -3, -2, -1, 1, 2, 3, -3],
                [2, 3, -3, -2, -1, 1, 2, 3, -3, -2],
                [1, 2, 3, -3, -2, -1, 1, 2, 3, -3, -2, -1],
            ],
            id="Complex case with multiple zero-sum combinations",
        ),
    ],
)
def test_solution(numbers, expected):
    result = solution(numbers)
    if result == -1:
        assert len(expected) > 1000000
    else:
        assert result == expected
