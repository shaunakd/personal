from typing import Union

"""
Project 19: Develop a Python function named solution that takes an array A of N integers as input and returns the subarrays (or fragments) of A whose elements sum to zero.
Specifically, you need to identify pairs (P,Q) where P ≤ Q and the sum of the elements from index P to Q (inclusive) is zero.
If the number of such subarrays exceeds 1000000, the function should return -1.

Examples
For the array A = [2,-2,3,0,4,-7], the function should return 4. The four subarrays that sum to zero are:
    [2,-2]
    [3,0,4,-7]
    [0]
    [2,-2,3,0,4,-7]

Constraints:
N is an integer within the range [1, 100000].
Each element of the array  is an integer within the range [-10000, 10000].
Write an efficient algorithm to solve this problem.
"""

"""
changes:
Function now returns the subarrays instead of the count of subarrays
"""


# # nested loop approach: O(n^3) time complexity
# def solution(numbers: list[int]) -> Union[list[list[int]], int]:
#     """Returns the subarrays whose elements sum to zero"""
#     subarrays = []
#     for i in range(len(numbers)):
#         for j in range(i, len(numbers)):
#             if sum(numbers[i : j + 1]) == 0:
#                 subarrays.append(numbers[i : j + 1])
#             if len(subarrays) > 1000000:
#                 return -1
#     subarrays = sorted(
#         subarrays, key=lambda subarray: (len(subarray), subarray[0])
#     )
#     return subarrays


# # nested loop approach with prefix sum: O(n^2) time complexity
# def solution(numbers: list[int]) -> Union[list[list[int]], int]:
#     """Returns the subarrays whose elements sum to zero"""
#     subarrays = []
#     for i in range(len(numbers)):
#         prefix_sum = 0
#         for j in range(i, len(numbers)):
#             prefix_sum += numbers[j]
#             if prefix_sum == 0:
#                 subarrays.append(numbers[i : j + 1])
#             if len(subarrays) > 1000000:
#                 return -1
#     subarrays = sorted(
#         subarrays, key=lambda subarray: (len(subarray), subarray[0])
#     )
#     return subarrays


# hash map approach with prefix sum: O(n) time complexity
def solution(numbers: list[int]) -> Union[list[list[int]], int]:
    """Returns the subarrays whose elements sum to zero"""
    subarrays = []
    prefix_sum = 0
    prefix_sum_map = {0: [-1]}
    for i in range(len(numbers)):
        prefix_sum += numbers[i]
        if prefix_sum in prefix_sum_map:
            indices = prefix_sum_map[prefix_sum]
            for index in indices:
                subarrays.append(numbers[index + 1 : i + 1])
        prefix_sum_map.setdefault(prefix_sum, []).append(i)
        if len(subarrays) > 1000000:
            return -1
    subarrays = sorted(subarrays, key=lambda subarray: (len(subarray), subarray[0]))
    return subarrays
