def lower_bound(arr, x): # первый элемент >= x
    l = -1
    r = len(arr)
    while r - l > 1:
        m = (l + r) // 2
        if arr[m] < x:
            l = m
        else:
            r = m
    return r

def upper_bound(arr, x): # первый элемент > x
    l = -1
    r = len(arr)
    while r - l > 1:
        m = (l + r) // 2
        if arr[m] <= x:
            l = m
        else:
            r = m
    return r

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())
queries = list(map(int, input().split()))
ans = []
for x in queries:
    cnt = upper_bound(arr, x) - lower_bound(arr, x)
    ans.append(cnt)
print(*ans)