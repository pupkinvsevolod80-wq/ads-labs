def BubbleSort(A):
    n = len(A)
    cnt = 0
    for iter in range(n):
        swapped = False
        for i in range(n - iter - 1):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                swapped = True
                cnt += 1
        if not swapped:
            break
    return cnt

N = int(input())
arr = list(map(int, input().split()))
print(BubbleSort(arr))