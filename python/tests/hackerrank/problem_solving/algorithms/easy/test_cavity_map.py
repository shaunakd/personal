import pytest

from src.hackerrank.problem_solving.algorithms.easy.cavity_map import (
    cavity_map,
    get_adjacent_cells,
)

pytestmark = pytest.mark.unit


@pytest.mark.parametrize(
    "grid, i, j, expected_output",
    [
        pytest.param(
            ["989", "191", "111"], 1, 1, ["9", "1", "1"], id="get_adjacent_cells_case_1"
        ),
        pytest.param(
            ["123", "456", "789"], 1, 1, ["2", "4", "6"], id="get_adjacent_cells_case_2"
        ),
    ],
)
def test_get_adjacent_cells(grid, i, j, expected_output):
    assert get_adjacent_cells(grid, i, j) == expected_output


@pytest.mark.parametrize(
    "grid, expected_output",
    [
        pytest.param(["989", "191", "111"], ["989", "1X1", "111"], id="simple_case"),
    ],
)
def test_cavity_map(grid, expected_output):
    assert cavity_map(grid) == expected_output
