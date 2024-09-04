def create_largest_number(numbers: list[int]) -> int:
  """Function to rearrange a list of numbers into the largest number possible"""
  # sorting numbers by their first digit
  sorted_numbers = sorted(
    numbers, key=lambda x: str(x[0])
  )
  # joining digits to create the largest number
  largest_number = int(''.join(sorted_numbers))
  return largest_number
