n = int(input())
a = list(range(1, n + 1))
for i in range(2, n):
    mid = i // 2
    a[i], a[mid] = a[mid], a[i]

print(*a)