import pytest
import pandas as pd
from datetime import timedelta
from src.python_projects.forage.jpmc_quantitative_research.task_1_natural_gas.test import (
    estimate_price,
    data,
    polynomial,
)


@pytest.mark.parametrize(
    "input_date, expected_price",
    [
        (
            "2023-06-15",
            11.165743784950237,
        ),  # Replace `3.45` with the expected interpolated price
        (
            "2022-01-01",
            11.385035503444263,
        ),  # Replace `2.75` with the expected interpolated price
    ],
)
def test_estimate_price_interpolation(input_date, expected_price):
    """
    Test that the estimate_price function correctly interpolates prices for dates within the range.
    """
    estimated_price = estimate_price(input_date)
    assert pytest.approx(estimated_price, rel=1e-2) == expected_price


def test_estimate_price_invalid_date():
    """
    Test that the estimate_price function raises a ValueError for dates outside the range.
    """
    with pytest.raises(ValueError):
        estimate_price("2010-01-01")  # Date before the range
    with pytest.raises(ValueError):
        estimate_price("2030-01-01")  # Date after the range


def test_extrapolation():
    """
    Test that the polynomial extrapolation produces reasonable results for future dates.
    """
    future_dates = pd.date_range(
        start=data.index.max() + timedelta(days=1), periods=12, freq="M"
    )
    future_normalized_dates = (future_dates - data.index.min()).days
    future_prices = polynomial(future_normalized_dates)

    # Ensure extrapolated prices are within a reasonable range
    assert all(price > 0 for price in future_prices)  # Prices should be positive
    assert len(future_prices) == 12  # Ensure 12 months of extrapolated data


def test_visualization_data():
    """
    Test that the data used for visualization matches the expected format.
    """
    normalized_dates = (data.index - data.index.min()).days
    polynomial_fit_prices = polynomial(normalized_dates)

    # Ensure the polynomial fit produces the same number of points as the historical data
    assert len(polynomial_fit_prices) == len(data)
    assert all(isinstance(price, float) for price in polynomial_fit_prices)
