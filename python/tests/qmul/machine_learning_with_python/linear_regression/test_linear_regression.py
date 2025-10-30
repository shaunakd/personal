import pytest
import numpy as np
from numpy.testing import assert_array_almost_equal, assert_array_equal
from src.qmul.machine_learning_with_python.linear_regression.linear_regression import (
    linear_regression_data,
    linear_regression,
    prediction_error,
)

pytestmark = pytest.mark.unit


@pytest.mark.parametrize(
    "data_inputs, expected_data_matrix",
    [
        pytest.param(
            np.array([[1], [2], [3], [4]]),
            np.array([[1, 1], [1, 2], [1, 3], [1, 4]]),
            id="4x1 matrix",
        ),
        pytest.param(
            np.array([[1, 2], [2, 3], [3, 4], [4, 5]]),
            np.array([[1, 1, 2], [1, 2, 3], [1, 3, 4], [1, 4, 5]]),
            id="4x2 matrix",
        ),
    ],
)
def test_linear_regression_data(data_inputs, expected_data_matrix):
    assert_array_equal(linear_regression_data(data_inputs), expected_data_matrix)


@pytest.mark.parametrize(
    "data_matrix, data_outputs, expected_solution",
    [
        pytest.param(
            np.array([[1, 0.5], [1, 1.5]]),
            np.array([[1], [1]]),
            np.array([[1], [0]]),
            id="test_case_1",
        ),
        pytest.param(
            np.array([[1, 0.98], [1, 1.02]]),
            np.array([[-0.1], [0.3]]),
            np.array([[-9.9], [10]]),
            id="test_case_2",
        ),
    ],
)
def test_linear_regression(data_matrix, data_outputs, expected_solution):
    assert_array_almost_equal(
        linear_regression(data_matrix, data_outputs), expected_solution
    )


@pytest.mark.parametrize(
    "data_matrix, data_outputs, weights, expected_error",
    [
        pytest.param(
            np.array([[1, 0.98], [1, 1.02]]),
            np.array([[-0.1], [0.3]]),
            np.array([[-9.9], [10]]),
            0,
            id="test_case_1",
        ),
        pytest.param(
            np.array([[1, 1, -1], [1, 2, 2]]),
            np.array([[-1, 2], [1, 3]]),
            np.array([[0, 0], [1, 2], [3, 4]]),
            36.75,
            id="test_case_2",
        ),
    ],
)
def test_prediction_error(data_matrix, data_outputs, weights, expected_error):
    assert_array_almost_equal(
        prediction_error(data_matrix, data_outputs, weights), expected_error
    )
