"""
Project 7: Longest Common Prefix

Write a function to find the longest common prefix among a list of strings.
"""


def get_longest_common_prefix(words: list[str]) -> str:
    """Returns a string representing the longest common prefix among all the strings in the list"""
    words = [word.lower() for word in words]  # case-insensitive
    longest_common_prefix = ""
    if len(set(words)) == 1:
        longest_common_prefix = words[0]
    elif words:
        i = 0
        # adds to longest_common_prefix if character is in all of the words
        while all(i < len(word) and word[i] == words[0][i] for word in words):
            longest_common_prefix += words[0][i]
            i += 1
    return longest_common_prefix
