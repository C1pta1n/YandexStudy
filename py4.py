A = []
n = int(input())
for i in range (n):
    A[i] = int(input)



def MaxPairwiseProductFast(A[1..n]):
    index = 1
    for i from 2 to n:
        if A[i] > A[index]:
            index = i
    swap(A[index], A[n]) 
    index = 1:
    for i from 2 to n - 1
        if A[i] > A[index]:
            index = i
    swap(A[index], A[n - 1]) 
    return A[n - 1] * A[n]
MaxPairwiseProductBySorting(A[1..n]):
    Sort(A)
    return A[n-1]*A[n]