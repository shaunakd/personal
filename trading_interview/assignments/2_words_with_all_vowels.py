def get_words_with_all_vowels(words: list[str]) -> list[str]:
  words_with_all_vowels = [
    word for word in words
    if {'a', 'e', 'i', 'o', 'u'} <= set(word)
  ]
  return words_with_all_vowels
