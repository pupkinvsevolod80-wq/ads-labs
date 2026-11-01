import heapq

n = int(input())
cargos = []
for _ in range(n):
    t, l = map(int, input().split())
    cargos.append((t, l))

cargos.sort()

h = []
for t, l in cargos:
    if h and h[0] <= t:
        heapq.heappop(h)
    heapq.heappush(h, t + l)

print(len(h))