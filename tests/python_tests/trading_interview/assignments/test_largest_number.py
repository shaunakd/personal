import pytest
from projects.python_projects.trading_interview.assignments.largest_number import create_largest_number

pytestmark = pytest.mark.unit

@pytest.mark.parametrize(
    "numbers, expected_largest_number",
    [
        pytest.param([4, 56, 6, 3], 65643, id="case_1"),
        pytest.param([6, 3, 59], 6593, id="case_2"),
        pytest.param([91, 62, 7, 12], 9176212, id="case_3")
    ]
)
def test_create_largest_number(numbers, expected_largest_number):
    assert create_largest_number(numbers) == expected_largest_number