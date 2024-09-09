"""
We define a magic square to be an  matrix of distinct positive integers from  to  where the sum of any row, column, or diagonal of length  is always equal to the same number: the magic constant.
You will be given a `3x3` matrix `s` of integers in the inclusive range `[1,9]`. We can convert any digit `a` to any other digit `b` in the range `[1,9]` at cost of `|a-b|`. Given `s`, convert it into a magic square at minimal cost. Print this cost on a new line.
Note: The resulting magic square must contain distinct integers in the inclusive range `[1,9]`.

Example
s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]

The matrix looks like this:
5 3 4
1 5 8
6 4 2
We can convert it to the following magic square:
8 3 4
1 5 9
6 7 2
This took three replacements at a cost of `|5-8|+|8-9|+|4-7|=7`.

Function Description
Complete the formingMagicSquare function in the editor below.

formingMagicSquare has the following parameter(s):
int s[3][3]: a `3x3` array of integers

Returns
int: the minimal total cost of converting the input square to a magic square
"""


def form_magic_square(s):
    # All possible 3x3 magic squares
    magic_squares = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
    ]

    # Compute the cost of transforming s into the first magic square
    min_cost = sum(
        abs(s[i][j] - magic_squares[0][i][j]) for i in range(3) for j in range(3)
    )

    # Compare costs for the remaining magic squares
    for magic_square in magic_squares[1:]:
        cost = sum(
            abs(s[i][j] - magic_square[i][j]) for i in range(3) for j in range(3)
        )
        min_cost = min(min_cost, cost)

    return min_cost
