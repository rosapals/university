# oblig3 by Lyra, Erlend and Rosa
# Last updated: 27/10/2021
import random

def sort(A):
    # Call quick(A, low, high) with low = 0 and high = n-1 to sort the whole array
    # where n is number of elements in A
    return quick(A, 0, len(A)-1)

def quick(A, low, high):
    """Sorts an array of numbers
    Inputs
        A (array): Unsorted array of numbers
        low, high (int): Lowest and highest indexes of A
    Returns
        A (array): Sorted array of numbers
    """
    if low >= high:
        return A
    p = partition(A, low, high)
    quick(A, low, p-1)
    quick(A, p+1, high)
    return A

def partition(A, low, high):
    """Moves elements smaller than and to the right of some index to the left of the index.
    Moves elements bigger than and to the left of the same index to the right of the index.
    Inputs
        A (array): Unsorted array of numbers
        low, high (int): Lowest and highest index of A to work on
    Returns
        The index mentioned above
    """
    p = choosePivot(low, high)
    A.swap(high, p)
    pivot = A[high]
    left = low
    right = high - 1

    while left <= right:
        while (left <= right) and (A[left] <= pivot):
            left += 1
        while (right >= left) and (A[right] >= pivot):
            right -= 1
        if left < right:
            A.swap(right, left)
    A.swap(high, left)
    return left

def choosePivot(low, high):
    """Finds a random index between low and high
    Input
        low, high (int): Indexes, indicating the range of where to find a random index
    Returns
        Random index (int)
    """
    return random.randint(low, high-1)