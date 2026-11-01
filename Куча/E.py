import heapq

n = int(input())
h = list(map(int, input().split()))

heapq.heapify(h)

total_sum = 0
while len(h) > 1:
    x = heapq.heappop(h)
    y = heapq.heappop(h)
    s = x + y
    total_sum += s
    heapq.heappush(h, s)

ans = total_sum * 0.05
print(f"{ans:.2f}")