"""Project 5"""


def get_smallest_string_by_removing_one_letter(s: str) -> str:
    """Returns the alphabetically smallest string that can be obtained by removing exactly one letter from s."""
    max_letter = max(s)
    # removes the maximum letter
    smallest_string = s.replace(max_letter, "", 1)
    return smallest_string
