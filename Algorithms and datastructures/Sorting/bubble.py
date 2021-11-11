
def sort(A):
    for i in range(len(A)):
        for j in range(0, len(A)-i-1):
            if(A[j] > A[j+1]):
                A.swap(j, j+1)
    return A




