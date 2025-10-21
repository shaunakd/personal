import numpy as np
from numpy.typing import NDArray


def linear_regression_data(data_inputs: NDArray) -> NDArray:
    """Construct the design matrix (data matrix) for linear regression from the given input data.

    Parameters
    ----------
    data_inputs : NDArray[np.floating]
        A 2D NumPy array containing the input features for all samples.
        Each row corresponds to one sample, and each column corresponds
        to one feature value.

    Returns
    -------
    NDArray[np.floating]
        The design matrix X, formed by adding a column of ones as the
        first column of `data_inputs`. This column represents the
        intercept term in the linear regression model.

    Notes
    -----
    The resulting matrix X has the form:

        X = [[1, x1_1, x1_2, ..., x1_d],
             [1, x2_1, x2_2, ..., x2_d],
             ...
             [1, xs_1, xs_2, ..., xs_d]]

    Mathematically, this corresponds to:

        X =
        ( 1   x₁¹   x₂¹  ...  x_d¹ )
        ( 1   x₁²   x₂²  ...  x_d² )
        ( ⋮    ⋮     ⋮    ⋱   ⋮   )
        ( 1   x₁ˢ   x₂ˢ  ...  x_dˢ )

    where:
        - s is the number of samples
        - d is the number of features
    """

    s = data_inputs.shape[0]
    x0 = np.ones(s)
    data_matrix = np.column_stack((x0, data_inputs))
    return data_matrix


def linear_regression(
    data_matrix: NDArray[np.floating], data_outputs: NDArray[np.floating]
) -> NDArray[np.floating]:
    """Computes the weights (coefficients) of a linear regression model using the normal equation.

    Parameters
    ----------
    data_matrix : NDArray[np.floating]
        Input data matrix, denoted mathematically as X.
    data_outputs : NDArray[np.floating]
        Output vector, denoted mathematically as Y.

    Returns
    -------
    NDArray[np.floating]
        The estimated weights (coefficients), denoted as W_hat.

    Notes
    -----
    The solution is obtained from the normal equation:

        (X^T X) W = X^T Y

    where:
        - X is the matrix representation of `data_matrix`
        - Y is the matrix representation of `data_outputs`
        - W is the vector of regression coefficients
    """

    X, Y = data_matrix, data_outputs
    XTX, XTY = X.T @ X, X.T @ Y
    W = np.linalg.solve(XTX, XTY)
    # the equivalent of np.matmul(np.linalg.inv(XTX), XTY), the exact solution.
    return W


def prediction_error(
    data_matrix: NDArray[np.floating],
    data_outputs: NDArray[np.floating],
    weights: NDArray[np.floating],
) -> float:
    """Compute the prediction error (mean squared error) for a linear regression model.

    Parameters
    ----------
    data_matrix : NDArray[np.floating]
        The design matrix X containing input features, where each row
        represents one sample and each column one feature (including
        the intercept term if applicable).
    data_outputs : NDArray[np.floating]
        The true output values (targets), represented as a 1D or column
        vector Y of shape (n_samples,).
    weights : NDArray[np.floating]
        The regression coefficients (W_hat) estimated by the model.

    Returns
    -------
    float
        The mean squared error (MSE) between the predicted and true
        outputs, defined as:

            MSE = (1 / (2 * s)) * || XW - Y ||²

        where s is the number of samples.
    """

    X, Y, W = data_matrix, data_outputs, weights
    s = X.shape[0]
    MSE = 1 / (2 * s) * np.linalg.norm(X @ W - Y) ** 2
    return float(MSE)
