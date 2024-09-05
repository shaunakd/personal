"""Project 3"""

def create_largest_number(numbers: list[int]) -> int:
  """Function to rearrange a list of numbers into the largest number possible"""
  # converting all integers to strings for ease of joining later
  numbers = list(map(str, numbers))
  # sorting numbers by their first digit
  sorted_numbers = sorted(
    numbers, key=lambda x: x[0], reverse=True
  )
  # joining digits to create the largest number
  largest_number = int(''.join(sorted_numbers))
  return largest_number