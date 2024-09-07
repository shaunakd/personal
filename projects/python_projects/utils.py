from typing import Any


def invert_injective_dictionary(dictionary: dict[Any, Any]) -> dict[Any, Any]:
    inverted_dict = {v: k for k, v in dictionary.items()}
    return inverted_dict


def invert_non_injective_dictionary(dictionary: dict[Any, Any]) -> dict[Any, Any]:
    inverted_dict: dict[Any, Any] = {}
    for v in dictionary.values():
        inverted_dict[v] = []
        for k in dictionary.keys():
            if dictionary[k] == v and k not in inverted_dict[v]:
                inverted_dict[v].append(k)
    for k in inverted_dict:
        inverted_dict[v] = tuple(inverted_dict[v])
        if len(inverted_dict[v]) == 1:
            inverted_dict[v] = inverted_dict[v][0]
    return inverted_dict
