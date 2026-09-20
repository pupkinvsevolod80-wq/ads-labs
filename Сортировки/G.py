def CountSort(A):
    k = max(A)
    counter = [0] * (k + 1)
    for x in A:
        counter[x] += 1
    A[:] = []
    for num in range(k + 1):
        A += [num] * counter[num]
    return A
arr = list(map(int, input().split()))
print(*CountSort(arr))
