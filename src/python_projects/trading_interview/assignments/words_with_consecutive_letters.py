"""
Project 8: Consecutive Letters

Write a function that takes a list of words and returns a list containing only those words that have n consecutive letters of the alphabet.
"""


def get_words_with_consecutive_letters(words: list[str], n: int) -> list[str]:
    """Returns a list containing only the words that have n consecutive letters of the alphabet"""
    assert n >= 0, "Only nonnegative integer values of n are allowed."
    words_with_consecutive_letters = []
    
    if n == 1:
        words_with_consecutive_letters = words
    elif n > 1:
        for word in words:
            count = 1
            for i in range(1, len(word)):
                if ord(word[i]) - ord(word[i - 1]) == 1:
                    count += 1
                    if count == n:
                        words_with_consecutive_letters.append(word)
                        break
                else:
                    count = 1  # Reset count if characters are not consecutive
    
    return words_with_consecutive_letters
