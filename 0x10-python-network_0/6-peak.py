#!/usr/bin/python3
"""
finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    finds a peak in a list of unsorted integers.

    Args:
        list_of_integers (List[int]): list of unsorted integers from which to
            find the peak
    """

    n = len(list_of_integers)
    if n == 0:
        return []
    left, right = 0, n - 1

    while left != right:
        mid = left + (right - left) // 2
        if ((mid == 0
            or list_of_integers[mid - 1] <= list_of_integers[mid])
            and (mid == n - 1
                 or list_of_integers[mid + 1] <= list_of_integers[mid])):
            return list_of_integers[mid]
        elif (list_of_integers[mid - 1] >
                list_of_integers[mid] >
                list_of_integers[mid + 1]):
            right = mid - 1
        else:
            left = mid + 1

    return list_of_integers[left]
