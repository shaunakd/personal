"""
Project 1: All Pairs

Write a function that takes in an array of integers, which can be both positive and negative, along with a target integer.
The function should return all unique pairs of integers from the array that sum up to the target integer.
"""


def find_pairs_with_sum(numbers: list[int], target: int) -> list[tuple[int, int]]:
    """Finds pairs of numbers in the numbers list which sum to the target"""
    pairs: list[tuple[int, int]] = []
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            n1, n2 = numbers[i], numbers[j]
            if n1 + n2 == target:
                pairs.append((n1, n2))

    pairs = sorted(pairs, key=lambda pair: pair[0])
    return pairs
