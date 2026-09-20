def BubbleSort(A):
    n = len(A)
    for iter in range(n - 1):
        swapped = False
        for i in range(n - iter - 1):
            if A[i] < A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                swapped = True
        if not swapped:
            break
A = list(map(int, input().split()))
BubbleSort(A)
print(*A)