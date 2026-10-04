def good(days):
    dmitry = (days - days // k) * a
    fedor = (days - days // m) * b
    return dmitry + fedor >= x


a, k, b, m, x = map(int, input().split())

l = 0
r = 2 * x // a + 1

while r - l > 1:
    mid = (l + r) // 2
    if good(mid):
        r = mid
    else:
        l = mid

print(r)