data = list(map(int, input().split()))
h = data[1:]
h.append(0)

stack = []
ans = 0

for i in range(len(h)):
  while stack and h[stack[-1]] >= h[i]:
    cur = stack.pop()
    l = stack[-1] + 1 if stack else 0
    r = i - 1
    area = h[cur] * (r - l + 1)
    if area > ans:
      ans = area
  stack.append(i)

print(ans)