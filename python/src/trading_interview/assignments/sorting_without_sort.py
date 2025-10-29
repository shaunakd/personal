"""
Project 30: Sorting Without Sort()

Given two sorted lists, write a function to merge them into one sorted list. You can't use sort() or any other inbuilt sorting function. Please write the solution as efficient as possible.

Bonus: What's the time complexity?
"""


def merge_sorted_lists(list1: list, list2: list) -> list:
    merged_list = []
    while list1 and list2:
        (
            merged_list.append(list1.pop(0))
            if list1[0] < list2[0]
            else merged_list.append(list2.pop(0))
        )
    merged_list.extend(list1)
    merged_list.extend(list2)
    return merged_list
