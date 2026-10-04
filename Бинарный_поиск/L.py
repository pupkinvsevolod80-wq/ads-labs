def good(d):
    cnt = 0
    i = 0
    while i + c - 1 < n:
        if a[i + c - 1] - a[i] <= d:
            cnt += 1
            i += c
        else:
            i += 1
    return cnt >= R_count


n, R_count, c = map(int, input().split())
a = [int(input()) for _ in range(n)]
a.sort()

l = -1
r = a[-1] - a[0]

while r - l > 1:
    m = (l + r) // 2
    if good(m):
        r = m
    else:
        l = m

print(r)