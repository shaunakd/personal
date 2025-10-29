"""
Project 31: Sudoku

Sudoku is a well-known puzzle. A solved Sudoku grid obeys the following rules:
The grid has a valid structure: it has n rows and n columns (with n being an integer), divided sub blocks of sqrt(n) x sqrt(n)
For every row, it should contain all the numbers from 1 up to and including n.
For every column, it should contain all the numbers from 1 up to and including n.
Every sub block should contain all the numbers from 1 up to and including n.
In this assignment, you will implement the function is_valid_sudoku that takes as input a 2-dimensional list sudoku of size n x n. This function should return True if the values in the grid obey all the Sudoku rules described above. Otherwise, it should return False.

This is an example of a Sudoku you can expect as input to the sudoku function:

[
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

We suggest you use a class / multiple functions instead of just one function, but it's up to you to come up with the most efficient and clean solution.
"""


class Sudoku:
    def __init__(self, sudoku: list[list[int]]) -> None:
        self.__sudoku = sudoku
        self.__n = len(sudoku)
        self.__check_1_to_n = lambda itr: sorted(itr) == list(range(1, self.__n + 1))

    # checks if grid is well-defined, non-empty, square and divisible into subgrids
    def _is_valid_sudoku_grid(self) -> bool:
        is_square_grid = all(self.__n == len(row) for row in self.__sudoku)
        try:
            sqrt = int(self.__n**0.5)
        except ValueError:
            sqrt = self.__n**0.5
        return all(
            (self.__sudoku, all(self.__sudoku), is_square_grid, isinstance(sqrt, int))
        )

    # checks rows
    def _check_rows(self) -> bool:
        return all(self.__check_1_to_n(row) for row in self.__sudoku)

    # checks columns
    def _check_columns(self) -> bool:
        return all(self.__check_1_to_n(col) for col in zip(*self.__sudoku))

    # checks subgrids
    def _check_subgrids(self) -> bool:
        sqrt = int(self.__n**0.5)
        return all(
            self.__check_1_to_n(
                self.__sudoku[x][y]
                for x in range(i, i + sqrt)
                for y in range(j, j + sqrt)
            )
            for i in range(0, self.__n, sqrt)
            for j in range(0, self.__n, sqrt)
        )

    def is_valid_sudoku(self) -> bool:
        # the self._is_valid_sudoku_grid() condition is separate from the other conditions to avoid unnecessary checks and to handle empty grids
        return self._is_valid_sudoku_grid() and all(
            (self._check_rows(), self._check_columns(), self._check_subgrids())
        )
