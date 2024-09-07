"""
Project 2: All Vowels

Write a function to filter out words from a given list that contain all the vowels ('a', 'e', 'i', 'o', 'u'). The function should be case insensitive.
"""


def get_words_with_all_vowels(words: list[str]) -> list[str]:
    """Returns words which contain all five vowels"""
    words_with_all_vowels = [
        word
        for word in words
        if {"a", "e", "i", "o", "u"} <= set(word.lower())  # case-insensitive filter
    ]
    return words_with_all_vowels
