"""
Project 6: Word Frequency

Objective:

In this programming assignment, you will create a Python script that counts the frequency of words in a given text file. Your script should be able to read a text file, process its content, and output the word frequencies in descending order.

Instructions:

-   Write a function called read_file(file_path) that takes a single argument, file_path, which is a string representing the path to the text file.
    The function should read the contents of the file and return a string containing the entire text.

-   Write another function called word_frequency(text) that takes a single argument, text, which is a string containing the text to be processed.
    The function should return a dictionary containing the frequency of each word in the text.
    For example, the output could look like: {"the": 10, "cat": 3, "sat": 2}.

-   To accomplish this, you may use string manipulation techniques and/or Python's built-in string methods to split the input text into words.
    Ensure that your function ignores punctuation, capitalization, and common stopwords (e.g., "a", "an", "the", "and", "in").

-   Write a function called sort_by_frequency(word_freq) that takes a single argument, word_freq, which is a dictionary containing word frequencies.
    The function should return a list of tuples containing the words and their frequencies, sorted in descending order by frequency.
    For example, the output could look like: [("the", 10), ("cat", 3), ("sat", 2)].

-   Write a test function called test_word_frequency() that tests your word_frequency(text) and sort_by_frequency(word_freq) functions using a sample text or a small text file.
    Include test cases with different types of text, as well as edge cases (e.g., empty text, text containing only special characters, or text with only stopwords).
"""

import re

from projects.python_projects.utils import (
    invert_injective_dictionary,
    invert_non_injective_dictionary,
)


def read_file(file_path: str) -> str:
    """Reads the contents of the file in file_path and returns a string containing the entire text."""
    file_str = ""
    with open(file_path, "r") as file:
        file_str = file.read().replace("\n", " ")
    return file_str


def filter_text(text: str) -> str:
    """Filters text"""
    text = text.lower()
    alphabet = list("abcdefghijklmnopqrztuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    words_to_ignore = [*alphabet, "an", "and", "as", "in", "the"]
    # removing non-alphabetic characters from text
    text = re.sub("[^a-zA-Z]+", " ", text)
    # removing words_to_ignore from text
    for word in words_to_ignore:
        text = re.sub(f" {word} ", " ", text)

    text = text.rstrip()

    return text


def word_frequency(filtered_text: str) -> dict[str, int]:
    """Returns a dictionary containing the frequency of each word in text"""
    # creates final dictionary of word frequencies
    words = filtered_text.split()
    word_frequency = {word: words.count(word) for word in set(words)}
    frequency_word = invert_injective_dictionary(word_frequency)
    word_frequency = invert_non_injective_dictionary(frequency_word)
    return word_frequency


def sort_by_frequency(word_freq: dict[str, int]) -> list[tuple[str, int]]:
    """Returns a list of tuples containing the words and their frequencies, sorted in descending order by frequency"""
    sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    return sorted_word_freq
