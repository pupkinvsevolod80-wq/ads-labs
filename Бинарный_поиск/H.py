def good(x, w, h, n):
    return (x // w) * (x // h) >= n


w, h, n = map(int, input().split())
l = 0
r = 1
while not good(r, w, h, n):
    r *= 2
while r - l > 1:
    m = (l + r) // 2
    if good(m, w, h, n):
        r = m
    else:
        l = m
print(r)