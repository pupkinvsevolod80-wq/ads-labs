import heapq

n = int(input())
h = []
for i in range(1, n + 1):
    a = int(input())
    t = max(1000 - a, 1)
    heapq.heappush(h, (t, i, a))

cur_time = 0
cur_pos = 1

while True:
    t, pos, a = heapq.heappop(h)
    if cur_time + abs(pos - cur_pos) > t:
        print(t)
        break
    cur_time = t
    cur_pos = pos
    new_a = a + 1
    next_t = t + max(1000 - new_a, 1)
    heapq.heappush(h, (next_t, pos, new_a))