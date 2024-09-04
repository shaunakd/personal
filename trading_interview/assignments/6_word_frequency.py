import re

def read_file(file_path: str) -> str:
  """Reads the contents of the file in file_path and returns a string containing the entire text."""
  file_str = ""
  with open(file_path, 'r') as file:
    file_str = file.read().replace("\n", "")
  return file_str

def word_frequency(text: str) -> dict[str, int]:
  """Returns a dictionary containing the frequency of each word in text"""
  text = text.lower()
  words_to_ignore = [
    "a", "an", "and", "in", "the"
  ]
  # removing non-alphanumeric characters from text
  re.sub("\W+", "", text)
  # removing words_to_ignore from text
  for word in words_to_ignore:
    text = text.replace(word, "")

  # creates final dictionary of word frequencies
  words = text.split()
  word_frequency = {word: words.count(word) for word in set(words)}

  return word_frequency

def sort_by_frequency(word_freq: dict[str, int]) -> list[tuple[str, int]]:
  """Returns a list of tuples containing the words and their frequencies, sorted in descending order by frequency"""
  word_freq = list(word_freq.items())
  sorted_word_freq = sorted(word_freq, key=lambda x: x[1], reverse=True)
  return sorted_word_freq
  
