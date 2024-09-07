"""Project 4"""


def find_missing_number(numbers: list[int], n: int) -> int:
    """Finds the single missing number in a given array supposed to contain all integers from 1 to n."""
    assert len(numbers) == n - 1, "The length of numbers should be n - 1"
    if n in numbers:
        missing_number = sum(range(max(numbers) + 1)) - sum(
            numbers
        )  # all terms will cancel out except the missing term, thus avoiding loops
    else:
        missing_number = (
            n  # if the numbers are all consecutive, the missing number is n
        )
    numbers = sorted(numbers)

    # checks that there is only one missing number
    first_section = numbers[: missing_number - 1]
    second_section = numbers[missing_number - 1 :]
    assert first_section == list(
        range(1, missing_number)
    ), "There should be only one missing number"
    assert second_section == list(
        range(missing_number + 1, n + 1)
    ), "There should be only one missing number"

    return missing_number
