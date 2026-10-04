def f(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x + d

a, b, c, d = map(int, input().split())
if a < 0:
    a, b, c, d = -a, -b, -c, -d
l = -2000.0
r = 2000.0

for _ in range(100):
    m = (l + r) / 2
    if f(m, a, b, c, d) < 0:
        l = m
    else:
        r = m
print(f"{m:.15f}")        