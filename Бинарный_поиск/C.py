import math
C = float(input())
l = 0.0
r = C

for _ in range(100):
    m = (l + r) / 2
    if m * m + math.sqrt(m) < C:
        l = m
    else:
        r = m
print(f"{m:.8f}")