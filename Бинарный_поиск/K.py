def count_balloons(t, ti, zi, yi):
    block_time = zi * ti + yi
    blocks = t // block_time
    rem_time = t % block_time
    extra = min(zi, rem_time // ti)
    return blocks * zi + extra


def good(t, m, assistants):
    total = 0
    for ti, zi, yi in assistants:
        total += count_balloons(t, ti, zi, yi)
    return total >= m


m, n = map(int, input().split())
assistants = []
for _ in range(n):
    ti, zi, yi = map(int, input().split())
    assistants.append((ti, zi, yi))

l = -1
r = 15000 * 100 + 100

while r - l > 1:
    mid = (l + r) // 2
    if good(mid, m, assistants):
        r = mid
    else:
        l = mid

print(r)

res = []
left = m
for ti, zi, yi in assistants:
    cnt = count_balloons(r, ti, zi, yi)
    take = min(left, cnt)
    res.append(take)
    left -= take

print(*res)