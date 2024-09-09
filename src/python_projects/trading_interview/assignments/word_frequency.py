"""
Project 6: Word Frequency

Objective:

In this programming assignment, you will create a Python script that counts the frequency of words in a given text file. Your script should be able to read a text file, process its content, and output the word frequencies in descending order.

Instructions:

-   Write a function called read_text_file(file_path) that takes a single argument, file_path, which is a string representing the path to the text file.
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
from typing import Optional, Union
from src.python_projects.utils.utils import (
    invert_injective_dictionary,
    invert_non_injective_dictionary,
    read_file,
)


def read_text_file(file_path: str) -> str:
    """Reads the contents of the file in file_path and returns a string containing the entire text."""
    file = read_file(file_path)
    if file:
        file = file.replace("\n", " ")
    return file


def filter_text(text: Optional[str]) -> Optional[str]:
    """Filters text"""
    if text:
        text = text.lower()
        alphabet = list("abcdefghijklmnopqrztuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        words_to_ignore = [*alphabet, "an", "and", "as", "in", "the"]
        # removing non-alphabetic characters from text
        text = re.sub("[^a-zA-Z]+", " ", text)
        # removing words_to_ignore from text
        for word in words_to_ignore:
            text = re.sub(f" {word} ", " ", text)
        # removing whitespace
        text = text.strip()
    return text


def word_frequency(filtered_text: Optional[str]) -> Optional[dict[str, int]]:
    """Returns a dictionary containing the frequency of each word in text"""
    # creates final dictionary of word frequencies
    word_frequency = None
    if filtered_text:
        words = filtered_text.split()
        word_frequency = {word: words.count(word) for word in set(words)}
        word_frequency = {word: word_frequency[word] for word in sorted(word_frequency)}
    return word_frequency


def group_words_by_frequency(
    word_freq: Optional[dict[str, int]],
) -> Optional[dict[Union[str, tuple[str, ...]], int]]:
    """Groups the words from word_frequency by frequency"""
    grouped_word_freq = None
    if word_freq:
        frequency_word = invert_non_injective_dictionary(word_freq)
        grouped_word_freq = invert_injective_dictionary(frequency_word)
        grouped_word_freq = {
            words: grouped_word_freq[words]
            for words in sorted(grouped_word_freq, key=grouped_word_freq.__getitem__)
        }
    return grouped_word_freq


def sort_by_frequency(
    word_freq: Optional[dict[str, int]],
) -> Optional[list[tuple[str, int]]]:
    """Returns a list of tuples containing the words and their frequencies, sorted in descending order by frequency"""
    sorted_word_freq = None
    if word_freq:
        sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
        sorted_word_freq = sorted(sorted_word_freq, key=lambda x: x[0])
    return sorted_word_freq
