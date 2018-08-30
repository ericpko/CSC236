"""Divide and conquer algorithms

*** University of Toronto ***
Department of Computer Science,
__author__ = 'Eric K'

*** Module description ***
this module contains divide and conquer algorithm examples seen in CSC236.
"""
from typing import List, Union


def binary_search(lst: List[int], x: int) -> bool:
    """
    Pre: A is a sorted list (non-decreasing order).
    4 Post: Returns True if and only if x is in A.

    """

    if lst == []:
        return False
    elif len(lst) == 1:
        return lst[0] == x
    else:
        m = len(lst) // 2         # Rounds down, like floor
        if x <= lst[m - 1]:
            return binary_search(lst[0:m - 1], x)
        else:
            return binary_search(lst[m:len(lst) - 1], x)


def indexed_bin_search(lst: List[int], x: int, first: int, last: int) -> bool:
    """
    Index binary search. Reduces the runtime because a new list is not
    created at every slice operation.
    """
    if first > last:
        return False
    elif first == last:
        return lst[first] == x
    else:
        m = (first + last + 1) // 2
        if x <= lst[m - 1]:
            return indexed_bin_search(lst, x, first, m - 1)
        else:
            return indexed_bin_search(lst, x, m, last)


def find_min(lst: List[int]) -> int:
    """
    Return the smallest value in <lst>.

    >>> find_min([3, 4, 5, 6, 7])
    3
    >>> find_min([5, 6, 7, 3, 4])
    3
    """
    smallest = lst[0]
    for i in range(len(lst)):
        if lst[i] < smallest:
            smallest = lst[i]
    return smallest


def find_min_rec(lst: Union[List[int], int]) -> int:
    """
    Return the smallest value in <lst>.

    >>> find_min_rec([3, 4, 5, 6, 7])
    3
    >>> find_min_rec([5, 6, 7, 3, 4])
    3
    """
    if not isinstance(lst, list):
        return lst
    else:
        return min(find_min_rec(s) for s in lst)


def find_min_conquer(lst: List[int]) -> int:
    """
    Return the smallest value in <lst>. Can also be designed with parameters
    b, and e, rather than slicing the lists in the current algorithm. O(n)

    >>> find_min_conquer([3, 4, 5, 6, 7])
    3
    >>> find_min_conquer([5, 6, 7, 3, 4])
    3
    """
    n = len(lst)
    if n < 2:
        # then there is 0 or 1 items in the list.
        return lst[0]
    else:
        # divide the list in half
        m = n // 2

        # find the min of the left half and the min of the right half
        left_min = find_min_conquer(lst[0:m])
        right_min = find_min_conquer(lst[m:])

        return min(left_min, right_min)


def find_min_conquered(lst: List[int]) -> int:
    """
    Return the smallest value in <lst>. Can also be designed with parameters
    b, and e, rather than slicing the lists in the current algorithm. O(lg(n))

    >>> find_min_conquered([3, 4, 5, 6, 7])
    3
    >>> find_min_conquered([5, 6, 7, 3, 4])
    3
    >>> find_min_conquered([7, 3, 4, 5, 6])
    3
    >>> find_min_conquered([1, 2, 3, 4, 5, 6, 7, 8, 9])
    1
    >>> find_min_conquered([9, 12, 15, 17, 20, 1, 2, 3, 4, 5, 6, 7, 8])
    1
    >>> find_min_conquered([9, 12, 15, 1, 3, 4, 5, 6, 7, 8])
    1
    """
    n = len(lst)
    if n < 2:
        # then there is 1 item in the list.
        return lst[0]
    elif lst[0] < lst[-1]:
        # then the list is not rotated
        return lst[0]
    elif lst[1] < lst[0]:   # n == 2
        # there are only 2 elements
        return lst[1]

    else:
        # divide the list in half. Note: n is at least 3.
        m = n // 2

        if lst[m - 1] < lst[-1]:
            # then the smallest must be before m
            return find_min_conquered(lst[:m])
        else:
            return find_min_conquered(lst[m:])


def max_sublist_sum(lst: List[int]) -> int:
    """
    Note: there is a faster algorithm than this that runs in logn time found in David's online CSC236 youtube channel
    Pre: <lst> is a list of integers.
    Post: returns a contiguous sublist of <lst> with a maximum possible sum.

    >>> max_sublist_sum([2, -5, 8, -6, 10, -2])
    12
    """
    n = len(lst)

    # base case
    if n <= 1:
        return max(lst[0], 0)                       # empty sublist is zero, which is better than negative

    else:
        # divide the list
        mid = n // 2                                # note: n is at least 2, so mid is at least 1

        # conqueur the list
        left_sum = max_sublist_sum(lst[:mid])       # from index 0...mid - 1
        right_sum = max_sublist_sum(lst[mid:])      # from index mid...n - 1
        cross_sum = max_crossing_sum(lst, mid, n)

        return max(left_sum, right_sum, cross_sum)


def max_crossing_sum(lst: List[int], mid: int, n: int) -> int:
    """
    Parameter <mid> is the floor middle index of <lst>.
    Parameter <n> is the length of the input list <lst>.
    Pre: <lst> is a list of integers and len(lst) >= 2.
    Post: returns the maximum contiguous crossing sum starting from the middle of <lst>.

    >>> max_crossing_sum([2, -5, 8, -6, 10, -2], 3, 6)
    12
    """
    left_sum, right_sum, total = 0, 0, 0    # initialize values

    # max sum of the left half
    k = mid - 1
    i = 0
    while i < mid:
        total += lst[k - i]
        i += 1
        if total > left_sum:
            left_sum = total

    # # max sum the left half
    # for i in range(mid - 1, -1, -1):        # iterate from index mid - 1...0 backward
    #     total += lst[i]
    #     if total > left_sum:
    #         left_sum = total

    total = 0
    # max sum the right half
    for i in range(mid, n):                 # iterate from index mid...n - 1
        total += lst[i]
        if total > right_sum:
            right_sum = total

    # note: left_sum and right_sum are each at least zero
    return left_sum + right_sum


if __name__ == '__main__':
    import doctest
    doctest.testmod()
