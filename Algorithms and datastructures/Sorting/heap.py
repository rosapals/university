def sort(A):
    n = len(A)
    build_max_heap(A, n)
    for i in range(n-1, -1, -1):
        A.swap(0,i)
        bubble_down(A, 0, i)
    return A

def bubble_down(A, i, n):
    largest = i
    left = 2*i+1
    right = 2*i+2

    if left < n and A[largest] < A[left]:
        largest, left = left, largest

    if right < n and A[largest] < A[right]:
        largest, right = right, largest

    if i != largest:
        A.swap(i, largest)
        bubble_down(A, largest, n)

def build_max_heap(A, n):
    for i in range(n//2, -1, -1):
        bubble_down(A, i, n)

