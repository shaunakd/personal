def get_smallest_string_by_removing_one_letter(S: str) -> str:
  """Returns the alphabetically smallest string that can be obtained by removing exactly one letter from S."""
  max_letter = max(S)
  # removes the maximum letter
  smallest_string = S.replace(max_letter, "", 1)
  return smallest_string
