def binary_search(arr, x):
    l = 0
    r = len(arr)-1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == x:
            return True
        elif arr[m] < x:
            l = m + 1
        else:
            r = m - 1
    return False

n, k = map(int, input().split())
arr = list(map(int, input().split()))
queries = list(map(int, input().split()))
for x in queries:
    if binary_search(arr, x):
        print("YES")
    else:
        print("NO")
