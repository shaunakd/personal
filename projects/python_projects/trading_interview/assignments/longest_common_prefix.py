"""Project 7"""

def get_longest_common_prefix(words: list[str]) -> str:
  """Returns a string representing the longest common prefix among all the strings in the list"""
  longest_common_prefix = ""
  for char_tuple in zip(words):
    if len(set(char_tuple)) == 1:
      # adds to longest_common_prefix if char is in all of the words
      longest_common_prefix += char_tuple[0]
    else:
      # ends the loop otherwise
      break
  return longest_common_prefix
