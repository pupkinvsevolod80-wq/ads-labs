def check(d, n, a, b, w, h):
    mod_w = a + 2 * d
    mod_h = b + 2 * d
    cnt1 = (w // mod_w) * (h // mod_h)
    cnt2 = (w // mod_h) * (h // mod_w)

    return cnt1 >= n or cnt2 >= n

n, a, b, w, h = map(int, input().split())

l = 0
r = max(w, h) + 1

while r - l > 1:
    m = (l + r) // 2
    if check(m, n, a, b, w, h):
        l = m
    else:
        r = m

print(l)