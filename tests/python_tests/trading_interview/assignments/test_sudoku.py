import pytest
from src.python_projects.trading_interview.assignments.sudoku import Sudoku


@pytest.mark.parametrize(
    "sudoku, expected",
    [
        # Valid Sudoku Test Cases
        pytest.param(
            [
                [5, 3, 4, 6, 7, 8, 9, 1, 2],
                [6, 7, 2, 1, 9, 5, 3, 4, 8],
                [1, 9, 8, 3, 4, 2, 5, 6, 7],
                [8, 5, 9, 7, 6, 1, 4, 2, 3],
                [4, 2, 6, 8, 5, 3, 7, 9, 1],
                [7, 1, 3, 9, 2, 4, 8, 5, 6],
                [9, 6, 1, 5, 3, 7, 2, 8, 4],
                [2, 8, 7, 4, 1, 9, 6, 3, 5],
                [3, 4, 5, 2, 8, 6, 1, 7, 9],
            ],
            True,
            id="valid_9x9_sudoku",
        ),
        pytest.param(
            [[1, 2, 3, 4], [3, 4, 1, 2], [2, 3, 4, 1], [4, 1, 2, 3]],
            True,
            id="valid_4x4_sudoku",
        ),
        pytest.param(
            [
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [4, 5, 6, 7, 8, 9, 1, 2, 3],
                [7, 8, 9, 1, 2, 3, 4, 5, 6],
                [2, 3, 4, 5, 6, 7, 8, 9, 1],
                [5, 6, 7, 8, 9, 1, 2, 3, 4],
                [8, 9, 1, 2, 3, 4, 5, 6, 7],
                [3, 4, 5, 6, 7, 8, 9, 1, 2],
                [6, 7, 8, 9, 1, 2, 3, 4, 5],
                [9, 1, 2, 3, 4, 5, 6, 7, 8],
            ],
            True,
            id="valid_9x9_sudoku_alternate",
        ),
        # Invalid Sudoku Test Cases
        pytest.param(
            [
                # Invalid: last number in the last row should be 9
                [5, 3, 4, 6, 7, 8, 9, 1, 2],
                [6, 7, 2, 1, 9, 5, 3, 4, 8],
                [1, 9, 8, 3, 4, 2, 5, 6, 7],
                [8, 5, 9, 7, 6, 1, 4, 2, 3],
                [4, 2, 6, 8, 5, 3, 7, 9, 1],
                [7, 1, 3, 9, 2, 4, 8, 5, 6],
                [9, 6, 1, 5, 3, 7, 2, 8, 4],
                [2, 8, 7, 4, 1, 9, 6, 3, 5],
                [3, 4, 5, 2, 8, 6, 1, 7, 8],
            ],
            False,
            id="invalid_9x9_sudoku_duplicate_in_row",
        ),
        pytest.param(
            [
                # Invalid: last two numbers in the last row should be swapped
                [1, 2, 3, 4],
                [3, 4, 1, 2],
                [2, 3, 4, 1],
                [4, 1, 3, 2],
            ],
            False,
            id="invalid_4x4_sudoku_duplicate_in_subgrid",
        ),
        pytest.param(
            [
                # Invalid: grid cannot be divided into subgrids
                [1, 2],
                [1, 2],
            ],
            False,
            id="invalid_2x2_sudoku_cannot_divide_into_subgrids",
        ),
        pytest.param(
            [
                # Invalid: grid cannot be divided into subgrids
                [1, 2, 3],
                [3, 1, 2],
                [2, 1, 3],
            ],
            False,
            id="invalid_3x3_sudoku_cannot_divide_into_subgrids",
        ),
        pytest.param(
            [
                # Invalid: duplicate numbers in the last row
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [4, 5, 6, 7, 8, 9, 1, 2, 3],
                [7, 8, 9, 1, 2, 3, 4, 5, 6],
                [2, 3, 4, 5, 6, 7, 8, 9, 1],
                [5, 6, 7, 8, 9, 1, 2, 3, 4],
                [8, 9, 1, 2, 3, 4, 5, 6, 7],
                [3, 4, 5, 6, 7, 8, 9, 1, 2],
                [6, 7, 8, 9, 1, 2, 3, 4, 5],
                [9, 1, 2, 3, 4, 5, 6, 7, 7],
            ],
            False,
            id="invalid_9x9_sudoku_duplicate_in_row_alternate",
        ),
        pytest.param(
            [
                # Invalid: duplicate numbers in the last row
                [1, 2, 3, 4],
                [3, 4, 1, 2],
                [2, 3, 4, 1],
                [4, 1, 2, 2],
            ],
            False,
            id="invalid_4x4_sudoku_duplicate_in_row",
        ),
        pytest.param(
            [
                # Invalid: zero is not a valid number in Sudoku
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [4, 5, 6, 7, 8, 9, 1, 2, 3],
                [7, 8, 9, 1, 2, 3, 4, 5, 6],
                [2, 3, 4, 5, 6, 7, 8, 9, 1],
                [5, 6, 7, 8, 9, 1, 2, 3, 4],
                [8, 9, 1, 2, 3, 4, 5, 6, 7],
                [3, 4, 5, 6, 7, 8, 9, 1, 2],
                [6, 7, 8, 9, 1, 2, 3, 4, 5],
                [9, 1, 2, 3, 4, 5, 6, 7, 0],
            ],
            False,
            id="invalid_9x9_sudoku_with_zero",
        ),
        pytest.param(
            [
                # Invalid: number 5 is out of range for a 4x4 Sudoku
                [1, 2, 3, 4],
                [3, 4, 1, 2],
                [2, 3, 4, 1],
                [4, 1, 2, 5],
            ],
            False,
            id="invalid_4x4_sudoku_number_out_of_range",
        ),
        pytest.param([], False, id="invalid_no_sudoku"),  # Invalid: no Sudoku grid
        pytest.param(
            [[]],
            False,
            id="invalid_empty_sudoku",  # Invalid: empty Sudoku grid
        ),
    ],
)
def validate_sudoku(sudoku, expected):
    assert Sudoku(sudoku).is_valid_sudoku() == expected
