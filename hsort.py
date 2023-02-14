from typing import TypeVar, List, Callable
import copy

T = TypeVar("T")  # Generic type


def insertion_sort(data: List[T], compare: Callable[[T, T], bool] = lambda x, y: x <= y) -> None:
    """
    Repeatedly moves through list sorting the front half as it goes
    :param data: List of object type "T"
    :param compare: boolean function that determines what to sort by, default = ascending order
    :return: None
    """

    length = len(data)
    position = 0

    while position <= length - 1:
        element = position

        while (element-1) >= 0 and not compare(data[element-1], data[element]):
            data[element], data[element-1] = data[element-1], data[element]
            element -= 1

        position += 1


def merge(data: List[T], part1: List[T], part2: List[T], compare: Callable[[T, T], bool] = lambda x, y: x <= y) -> int:
    """
    Merges partitions together in a sorted order and calculates number of inversions.
    :param data: List of object type "T"
    :param part1: first list partition
    :param part2: second list partition
    :param compare: boolean function that determines what to sort by, default = ascending order
    :return: int representing number of inversions
    """

    i = j = inversions = 0

    while i + j < len(data):

        if j == len(part2) or (i < len(part1) and compare(part1[i], part2[j])):
            data[i+j] = part1[i]
            i += 1

        else:
            data[i+j] = part2[j]
            inversions += len(part1)-i
            j += 1

    return inversions


def merge_sort(data: List[T], thresh: int = 0, compare: Callable[[T, T], bool] = lambda x, y: x <= y) -> int:
    """
    Recursively partitions list and calls merge() to merge partitions together in a sorted order.
    Keeps tally of inversions counted my merge()
    Calls insertion sort if partition length is less than threshold.
    :param data: List of object type "T"
    :param thresh: threshold length to call insertion sort, default = 0
    :param compare: boolean function that determines what to sort by, default = ascending order
    :return: int representing number of inversions
    """

    length = len(data)
    mid = length//2   # Find the midpoint in the partition
    inversions = 0

    if length >= 2:

        if length <= thresh:
            insertion_sort(data, compare)

        else:
            part1 = data[0:mid]
            part2 = data[mid:length]
            inversions += merge_sort(part1, thresh, compare)    # Recursively sort left
            inversions += merge_sort(part2, thresh, compare)    # and right partitions
            inversions += merge(data, part1, part2, compare)    # Merge left and right partition in sorted order

    return inversions


def hybrid_sort(data: List[T], thresh: int, compare: Callable[[T, T], bool] = lambda x, y: x <= y) -> None:
    """
    Wrapper function that calls merge sort as a hybrid sorting algorithm
    Passes desired threshold value to merge sort
    :param data: List of object type "T"
    :param thresh: threshold length to call insertion sort
    :param compare: boolean function that determines what to sort by, default = ascending order
    :return: None
    """

    merge_sort(data, thresh, compare)


def count_inversions(data: List[T]) -> int:
    """
    Calls merge_sort() on a copy of inputted list
    :param data: List of object type "T"
    :return: int representing number of inversions calculated by merge_sort()
    """

    return merge_sort(copy.deepcopy(data))


def reverse_sort(data: List[T], thresh: int) -> None:
    """
    Calls merge_sort() with compare set to descending order
    :param data: List of object type "T"
    :param thresh: threshold length to call insertion sort
    :return: None
    """

    merge_sort(data, thresh, lambda x, y: x >= y)
