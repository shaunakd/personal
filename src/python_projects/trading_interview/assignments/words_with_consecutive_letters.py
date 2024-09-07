"""Project 8"""


def get_words_with_consecutive_letters(words: list[str], n: int) -> list[str]:
    """Returns a list containing only the words that have n consecutive letters of the alphabet"""
    assert n > 0, "Only positive integer values of n are allowed."
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    words_with_consecutive_letters = []
    for word in words:
        sorted_word = "".join(sorted(word))
        i = 0
        while i < len(word) - n:
            # checks if each substring of length n is in alphabet, i.e. checks for consecutive letters
            sub_str = sorted_word[i : i + n - 1]
            if sub_str in alphabet:
                words_with_consecutive_letters.append(word)
            i += 1
    return words_with_consecutive_letters
