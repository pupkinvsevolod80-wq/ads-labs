def find_closest(arr, x):
    l = -1
    r = len(arr)

    while r - l > 1:
        m = (l + r) // 2
        if arr[m] <= x:
            l = m
        else:
            r = m
    if l == -1:
        return arr[r]
    if r == len(arr):
        return arr[l]

    if x - arr[l] <= arr[r] - x:
        return arr[l]
    else:
        return arr[r]


n, k = map(int, input().split())
arr = list(map(int, input().split()))
queries = list(map(int, input().split()))

for x in queries:
    print(find_closest(arr, x))