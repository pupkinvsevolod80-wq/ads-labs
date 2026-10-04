def good(x):
    if x == 0:
        return True    
    cnt = 0
    for ln in a:
        cnt += int(ln // x)
    return cnt >= k


n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]
l, r = 0, 10**7 + 1
for i in range(100):
    m = (r + l) // 2
    if good(m):
        l = m
    else:
        r = m
print(l)