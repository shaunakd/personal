"""
There will be two arrays of integers. Determine all integers that satisfy the following two conditions:
1. The elements of the first array are all factors of the integer being considered
2. The integer being considered is a factor of all elements of the second array

These numbers are referred to as being between the two arrays. Determine how many such numbers exist.

Example
`a = [2, 6]`
`b = [24, 36]`
There are two numbers between the arrays: `6` and `12`.
`6 % 2 = 0`, `6 % 6 = 0`, `24 % 6 = 0` and `36 % 6 = 0` for the first value.
`12 % 2 = 0`, `12 % 6 = 0` and `24 % 12 = 0` and `36 % 12 = 0` for the second value. Return `2`.

Function Description
Complete the getTotalX function in the editor below. It should return the number of integers that are betwen the sets.

getTotalX has the following parameter(s):
int a[n]: an array of integers
int b[m]: an array of integers

Returns
int: the number of integers that are between the sets
"""

"""
changes:
Renamed function to `get_numbers_between`, using snake_case rather than camelCase
Renamed parameters from `a` to `factors` and `b` to `multiples`
Function returns list of numbers between rather than number of numbers between
"""


def get_numbers_between(factors: list[int], multiples: list[int]) -> list[int]:
    numbers_between = [
        n
        for n in range(max(factors), min(multiples) + 1)
        if all(n % factor == 0 for factor in factors)
        and all(multiple % n == 0 for multiple in multiples)
    ]
    return numbers_between
