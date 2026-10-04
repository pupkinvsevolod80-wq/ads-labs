def good(x):
    cnt = 0
    for ln in a:
        cnt += ln // x
    return cnt >= k


n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]

l = 0
r = 10**7 + 1

while r - l > 1:
    m = (l + r) // 2
    if good(m):
        l = m
    else:
        r = m

print(l)