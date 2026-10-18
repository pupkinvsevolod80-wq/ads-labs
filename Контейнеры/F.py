from collections import deque

n, k = map(int, input().split())
a = list(map(int, input().split()))

dq = deque()
ans = []

for i in range(n):
  while dq and dq[0] <= i - k:
    dq.popleft()
  while dq and a[dq[-1]] >= a[i]:
    dq.pop()
  dq.append(i)
  if i >= k - 1:
    ans.append(str(a[dq[0]]))

print("\n".join(ans))