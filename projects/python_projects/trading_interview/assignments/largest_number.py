"""
Project 3: Largest Possible Number

Write a function to construct the largest possible number by rearranging the integers in a given list.
"""


def create_largest_number(numbers: list[int]) -> int:
    """Function to rearrange a list of numbers into the largest number possible"""
    # converting all integers to strings for ease of joining later
    str_numbers = [str(number) for number in numbers]
    # sorting numbers by their first digit
    sorted_numbers = sorted(str_numbers, key=lambda x: x[0], reverse=True)
    # joining digits to create the largest number
    largest_number = int("".join(sorted_numbers))
    return largest_number
