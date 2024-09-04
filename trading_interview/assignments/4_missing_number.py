def find_missing_number(numbers: list[int]) -> int:
  """Finds the single missing number in a given array supposed to contain all integers from 1 to n."""
  missing_number = sum(range(max(numbers))) - sum(numbers) # all terms will cancel out except the missing term
  return missing_number
