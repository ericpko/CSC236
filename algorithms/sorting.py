""" Searching & Sorting Algorithms

=== University of Toronto ===
Department of Computer Science
__author__ = 'Eric K'

=== Module Description ===
This module contains some searching and sorting algorithms.
"""
from typing import List, Tuple


# Remark: recall that len([1, 2, 3]) == 3 and
# len(lst) - 1 is the last index of the list <lst>. Also,
# range(len(lst)) takes you from index 0 to len(lst) - 1
# because range is not inclusive.


def linear_search(lst: list, value: object) -> int:
    """
    Return the index <i> of the first occurance of <value>
    in the list <lst>, else return -1.

    >>> linear_search([1, 2, 3, 4], 3)
    2
    >>> linear_search([1, 2, 3, 4], 5)
    -1
    >>> linear_search([1, 2, 3, 4], 4)
    3
    >>> linear_search([1, 2, 3, 4], 1)
    0
    """
    i = 0
    lst_length = len(lst)

    while i != lst_length and value != lst[i]:
        i += 1

    if i == lst_length:
        return -1
    else:
        return i


def binary_search(lst: list, value: object) -> int:
    """
    Return the index <i> of the first occurance of <value>
    in the list <lst>, else return -1.

    Precondition: assume that the list is sorted
    """
    start = 0
    end = len(lst) - 1

    while start <= end:
        mid = (start + end) // 2

        if lst[mid] < value:
            start = mid + 1
        else:
            end = mid - 1

    if start == len(lst) or lst[start] != value:
        return -1
    else:
        return start


def bubble_sort(lst: list) -> None:
    """ Modify list <lst> from smallest to largest.

    >>> L = [7, 3, 5, 2]
    >>> bubble_sort(L)
    [2, 3, 5, 7]
    """

    # Index of the last unsorted item
    end = len(lst) - 1   # The index of the last element in the list

    while end != 0:

        # Bubble once through the unsorted section of the list to move the
        # largest item to index end
        for i in range(end):        # index 0 to len(lst) - 2 because lst[i + 1]
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]  # Swap the elements

        end -= 1


def get_index_of_smallest(lst: list, i: int) -> int:
    """ Return the index <i> of the smallest item in lst[i:].

    >>> get_index_of_smallest([2, 7, 3, 5], 1)
    2
    """
    # Index of the smallest item so far
    index_of_smallest = i
    len_lst = len(lst)

    for j in range(i + 1, len_lst):

        if lst[j] < lst[index_of_smallest]:
            index_of_smallest = j

    return index_of_smallest


def selection_sort(lst: list) -> None:
    """ Modify list L from smallest to largest.

    >>> L = [7, 3, 5, 2]
    >>> selection_sort(L)
    [2, 3, 5, 7]
    """
    len_lst = len(lst)

    for i in range(len_lst):  # from index 0 to index len(lst) - 1
        # Find the index of the smallest item in L[i:] and swap that item with
        # the item at index i.
        index_of_smallest = get_index_of_smallest(lst, i)
        lst[index_of_smallest], lst[i] = lst[i], lst[index_of_smallest]

    return None


def insertion_sort(lst: list) -> None:
    """ Modify list L from smallest to largest.

    >>> L = [7, 3, 5, 2]
    >>> insertion_sort(L)
    >>> L
    [2, 3, 5, 7]
    """
    len_lst = len(lst)

    for i in range(len_lst):
        _insert(lst, i)

    return None


def _insert(lst: list, i: int) -> None:
    """ Move L[i] to where it belongs in L[i + 1]

    Precondition: L[:i] is sorted from smallest to largest.

    >>> L = [7, 3, 5, 2]
    >>> _insert(L, 1)
    >>> L
    [3, 7, 5, 2]
    """
    # The value to be inserted into the sorted part of the list
    value = lst[i]

    # Find the index, j, where the value belongs.
    # Make room for the value by shifting
    while i > 0 and lst[i - 1] > value:
        # Shift L[j - 1] one position to the right
        lst[i] = lst[i - 1]
        i -= 1

    # Put the value where it belongs
    lst[i] = value

    return None

    # Alternative version
    # j = i
    # while j != 0 and lst[j - 1] > value:

    # Shift L[j - 1] one position to the right
    # lst[j] = lst[j - 1]
    # j -= 1

    # Put the value where it belongs
    # lst[j] = value

    # return None


def find_value_indexes(item_list: list, index_list: List[int],
                       v: object) -> List[int]:
    """v may appear multiple times in item_list.  index_list contains zero or
    more indexes.  Return a list of the indexes from index_list at which v
    appears in item_list.
    Precondition: the values in index_list are valid indexes in item_list.

    >>> find_value_indexes([6, 8, 8, 5, 8], [0, 2, 4], 8)
    [2, 4]
    """
    indices = []

    for i in range(len(item_list)):

        if (item_list[i] == v) and (i in index_list):
            indices.append(i)

    return indices


def bubble_up(lst: list, start: int, end: int) -> None:
    """Bubble up through L[start:end], swapping items that are out of order.

    >>> L = [4, 3, 2, 1, 0]
    >>> bubble_up(L, 0, 3)
    >>> L
    [3, 2, 1, 4, 0]
    >>> L = [4, 3, 2, 1, 0]
    >>> bubble_up(L, 2, 4)
    >>> L
    [4, 3, 1, 0, 2]
    """
    for i in range(start, end):

        if lst[i] > lst[i + 1]:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]

    return None


def bubble_down(lst: list, start: int, end: int) -> None:
    """Bubble down through <lst> from indexes <end> through <start>, swapping
    items that are out of place.

    >>> L = [4, 3, 2, 1, 0]
    >>> bubble_down(L, 1, 3)
    >>> L
    [4, 1, 3, 2, 0]
    """
    i = end
    while i > start:

        if lst[i] < lst[i - 1]:
            lst[i], lst[i - 1] = lst[i - 1], lst[i]

        i -= 1

    return None


def insert(lst: List[int], v: int) -> None:
    """Insert v into lst just before the rightmost item greater than v, or at
    index 0 if no items are greater than v.

    >>> my_list = [3, 10, 4, 2]
    >>> insert(my_list, 5)
    >>> my_list
    [3, 5, 10, 4, 2]
    >>> my_list = [5, 4, 2, 10]
    >>> insert(my_list, 20)
    >>> my_list
    [20, 5, 4, 2, 10]
    """

    if len(lst) == 0:
        lst.append(v)
        return None

    i = len(lst) - 1
    while i != 0:

        if lst[i] > v:
            lst.insert(i, v)
            return None

        i -= 1

    if i == 0:
        lst.insert(0, v)

    return None


# *******************************************************
#             Recursive sorting algorithms
# *******************************************************
def mergesort(lst: list) -> list:
    """Return a sorted list with the same elements as <lst>.

    This is a *non-mutating* version of mergesort; it does not mutate the
    input list.
    """
    if len(lst) < 2:
        return lst[:]
    else:
        # Divide the list into two parts, and sort them recursively.
        mid = len(lst) // 2
        left_sorted = mergesort(lst[:mid])
        right_sorted = mergesort(lst[mid:])

        # Merge the two sorted halves. Need a helper here!
        return _merge(left_sorted, right_sorted)


def _merge(lst1: list, lst2: list) -> list:
    """Return a sorted list with the elements in <lst1> and <lst2>.

    Precondition: <lst1> and <lst2> are sorted.
    """
    index1 = 0
    index2 = 0
    merged = []
    while index1 < len(lst1) and index2 < len(lst2):
        if lst1[index1] <= lst2[index2]:
            merged.append(lst1[index1])
            index1 += 1
        else:
            merged.append(lst2[index2])
            index2 += 1

    # Now either index1 == len(lst1) or index2 == len(lst2).
    assert index1 == len(lst1) or index2 == len(lst2)
    # The remaining elements of the other list
    # can all be added to the end of <merged>.
    # Note that at most ONE of lst1[index1:] and lst2[index2:]
    # is non-empty, but to keep the code simple, we include both.
    return merged + lst1[index1:] + lst2[index2:]


def quicksort(lst: list) -> list:
    """Return a sorted list with the same elements as <lst>.

    This is a *non-mutating* version of quicksort; it does not mutate the
    input list.
    """
    if len(lst) < 2:
        return lst[:]
    else:
        # Pick pivot to be first element.
        # Could make lots of other choices here (e.g., last, random)
        pivot = lst[0]

        # Partition rest of list into two halves
        smaller, bigger = _partition(lst[1:], pivot)

        # Recurse on each partition
        smaller_sorted = quicksort(smaller)
        bigger_sorted = quicksort(bigger)

        # Return! Notice the simple combining step
        return smaller_sorted + [pivot] + bigger_sorted


def _partition(lst: list, pivot: object) -> Tuple[list, list]:
    """Return a partition of <lst> with the chosen pivot.

    Return two lists, where the first contains the items in <lst>
    that are <= pivot, and the second is the items in <lst> that are > pivot.
    """
    smaller = []
    bigger = []

    for item in lst:
        if item <= pivot:
            smaller.append(item)
        else:
            bigger.append(item)

    return smaller, bigger


if __name__ == '__main__':
    import doctest
    doctest.testmod()
