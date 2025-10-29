import pytest
from src.python_projects.trading_interview.assignments.sorting_without_sort import (
    merge_sorted_lists,
)


@pytest.mark.parametrize(
    "list1, list2, expected",
    [
        pytest.param([], [], [], id="both_empty"),
        pytest.param([], [1, 2, 3], [1, 2, 3], id="first_empty"),
        pytest.param([1, 2, 3], [], [1, 2, 3], id="second_empty"),
        pytest.param([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6], id="interleaved"),
        pytest.param([1, 2, 3], [2, 3, 4], [1, 2, 2, 3, 3, 4], id="overlapping"),
        pytest.param([1, 1, 1], [1, 1, 1], [1, 1, 1, 1, 1, 1], id="all_same"),
        pytest.param([1, 3, 5, 7], [2, 4], [1, 2, 3, 4, 5, 7], id="different_lengths"),
        pytest.param(
            [-3, -2, -1], [-5, -4, 0], [-5, -4, -3, -2, -1, 0], id="negative_numbers"
        ),
        pytest.param(
            [1000000, 1000001],
            [999999, 1000002],
            [999999, 1000000, 1000001, 1000002],
            id="large_numbers",
        ),
        pytest.param([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6], id="mixed_order"),
        pytest.param(
            [1, 2, 3, 4], [5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8], id="first_smaller"
        ),
        pytest.param(
            [5, 6, 7, 8], [1, 2, 3, 4], [1, 2, 3, 4, 5, 6, 7, 8], id="second_smaller"
        ),
        pytest.param([1, 2, 3], [1, 2, 3], [1, 1, 2, 2, 3, 3], id="identical_lists"),
        pytest.param(
            [1, 3, 5], [2, 4, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8], id="second_longer"
        ),
        pytest.param(
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            id="consecutive_numbers",
        ),
        pytest.param(
            [1, 2, 2, 3], [2, 2, 3, 4], [1, 2, 2, 2, 2, 3, 3, 4], id="duplicates"
        ),
        pytest.param([1], [2], [1, 2], id="single_elements"),
        pytest.param([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6], id="non_overlapping"),
        pytest.param(
            [1, 2, 3, 4, 5],
            [5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 5, 6, 7, 8, 9],
            id="overlapping_end",
        ),
    ],
)
def test_merge_sorted_lists(list1, list2, expected):
    assert merge_sorted_lists(list1, list2) == expected
