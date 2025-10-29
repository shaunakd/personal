import pytest
from src.python_projects.miscellaneous.net_salary_calculator import Employee


@pytest.mark.parametrize(
    "name, salary, expected_net_salary",
    [
        pytest.param("Alice", 12000, 12000, id="within_personal_allowance"),
        pytest.param(
            "Bob", 30000, 30000 - (30000 - 12570) * 0.2, id="within_basic_rate"
        ),
        pytest.param(
            "Charlie",
            60000,
            60000 - (50270 - 12570) * 0.2 - (60000 - 50270) * 0.4,
            id="within_higher_rate",
        ),
        pytest.param(
            "Dave",
            150000,
            150000
            - (50270 - 12570) * 0.2
            - (125140 - 50270) * 0.4
            - (150000 - 125140) * 0.45,
            id="within_additional_rate",
        ),
        pytest.param("Eve", 0, 0, id="zero_salary"),
        pytest.param("Frank", 12570, 12570, id="exact_personal_allowance"),
        pytest.param(
            "Grace", 50270, 50270 - (50270 - 12570) * 0.2, id="exact_basic_rate"
        ),
        pytest.param(
            "Hank",
            125140,
            125140 - (50270 - 12570) * 0.2 - (125140 - 50270) * 0.4,
            id="exact_higher_rate",
        ),
        pytest.param(
            "Ivy",
            200000,
            200000
            - (50270 - 12570) * 0.2
            - (125140 - 50270) * 0.4
            - (200000 - 125140) * 0.45,
            id="high_salary",
        ),
    ],
)
def test_calculate_net_salary(name, salary, expected_net_salary):
    employee = Employee(name, salary)
    assert employee.calculate_net_salary() == pytest.approx(
        expected_net_salary, rel=1e-2
    )
