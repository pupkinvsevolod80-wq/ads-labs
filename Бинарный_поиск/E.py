def check(dist, coords, k):
    count = 1
    last = coords[0]
    for x in coords[1:]:
        if x - last >= dist:
            count += 1
            last = x
    return count >= k

n, k = map(int, input().split())
coords = list(map(int, input().split()))

left = 0
right = coords[-1] - coords[0] + 1

while right - left > 1:
    mid = (left + right) // 2
    if check(mid, coords, k):
        left = mid
    else:
        right = mid

print(left)