#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_recursive(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array: [int], item: int, index=0) -> (int, None):
    """Searches for given item in array returns 1st indx of item."""
    # base case: index out of range
    if index >= len(array):
        return None
    # base case: arr at index is item
    if array[index] == item:
        return index
    # keep looking for item
    return linear_search_recursive(array, item, index + 1)

def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    """Return index of item in sorted array or None if item is not found."""
    # set large and small pointers (each end of arr)
    small = 0
    large = len(array) - 1
    # while pointers are not the same
    while small != large:
        # set middle index
        mid = (small + large) // 2
        # check if item is at mid index
        if array[mid] == item:
            return mid
        # check if item in index greater than item
        elif array[mid] > item:
            # check if more to search
            if mid == small:
                return None
            # update large index
            large = mid - 1
        # check if item at index less than item
        elif array[mid] < item:
            # check if more array to search
            if mid == large:
                return None
            # update small index
            small = mid + 1
    # check if last item is item
    if array[large] == item:
        return large
    # item not in list
    else:
        return None


def binary_search_recursive(array, item, left=None, right=None):
    """Return index of item in sorted array or none if item not found."""
    # BASE CASE: left and right point to same index
    if left == right and left is not None:
        # not in array
        if left == len(array):
            return None
        # check if index is item
        if array[left] == item:
            return left
        else:
            return None
    # if left and right are none set to length arr
    if left is None:
        left = 0
    if right is None:
        right = len(array)
    # set the middle index
    mid = (left + right) // 2
    # check if mid index is item
    if array[mid] == item:
        return mid
    # check if index's item is greater
    elif array[mid] > item:
        # nothing left to search
        if left == mid:
            return None
        # change right to middle index - 1
        return binary_search_recursive(array, item, left, mid - 1)
    # check if item at index less than
    elif array[mid] < item:
        # nothing left to search
        if right == mid:
            return None
        # change left to middle index + 1
        return binary_search_recursive(array, item, mid + 1, right)


