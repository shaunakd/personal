import pytest
from src.python_projects.hackerrank.problem_solving.algorithms.medium.forming_a_magic_square import (
    form_magic_square,
)


@pytest.mark.parametrize(
    "s, expected",
    [
        pytest.param([[5, 3, 4], [1, 5, 8], [6, 4, 2]], 7, id="test_case_1"),
        pytest.param([[4, 8, 2], [4, 5, 7], [6, 1, 6]], 4, id="test_case_2"),
        pytest.param([[4, 9, 2], [3, 5, 7], [8, 1, 6]], 0, id="test_case_3"),
        pytest.param([[2, 9, 8], [4, 2, 7], [5, 6, 7]], 21, id="test_case_4"),
        pytest.param([[6, 1, 6], [7, 2, 6], [5, 6, 2]], 18, id="test_case_5"),
        pytest.param([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 36, id="test_case_6"),
        pytest.param([[9, 8, 7], [6, 5, 4], [3, 2, 1]], 28, id="test_case_7"),
        pytest.param([[2, 7, 6], [9, 5, 1], [4, 3, 8]], 0, id="test_case_8"),
        pytest.param([[3, 3, 3], [3, 3, 3], [3, 3, 3]], 30, id="test_case_9"),
        pytest.param([[8, 1, 6], [3, 5, 7], [4, 9, 2]], 0, id="test_case_10"),
    ],
)
def test_form_magic_square(s, expected):
    assert form_magic_square(s) == expected
