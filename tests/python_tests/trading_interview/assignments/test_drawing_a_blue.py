import pytest
from src.python_projects.trading_interview.assignments.drawing_a_blue import run_simulation

@pytest.mark.parametrize(
    "n_simulations, n_cards, expected_range",
    [
        pytest.param(1000000, 13, (0.34, 0.36),id="many_simulations"),
        pytest.param(10, 13, (0, 1), id="few_simulations"),
        pytest.param(100000, 0, (0, 0), id="no_cards"),
        pytest.param(100000, 1, (0, 0), id="one_card"),
    ]
)
def test_run_simulation(n_simulations, n_cards, expected_range):
    prob = run_simulation(n_simulations, n_cards)
    assert expected_range[0] <= prob <= expected_range[1], f"Probability out of expected range: {prob:.4f}"
