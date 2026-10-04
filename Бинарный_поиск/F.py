def good(cnt, q, s, t):
    return t // q + t // s >= cnt


n, quick, slow = map(int, input().split())
if quick > slow:
    quick, slow = slow, quick
l = 0
r = (n - 1) * slow
while r - l > 1:
    m = (l + r) // 2
    if not good(n - 1, quick, slow, m):
        l = m
    else:
        r = m
print(r + quick)