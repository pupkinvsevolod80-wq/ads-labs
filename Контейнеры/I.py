data = list(map(int, input().split()))
balls = data[1:]
n = data[0]
groups = []
for x in balls:
  if groups and groups[-1][0] == x:
    groups[-1][1] += 1
  else:
    groups.append([x, 1])

stack = []
ans = 0
i = 0

while i < len(groups):
  color, count = groups[i]
  if count >= 3:
    ans += count
    i += 1
    while stack and i < len(groups) and stack[-1][0] == groups[i][0]:
      if stack[-1][1] + groups[i][1] >= 3:
        ans += stack[-1][1] + groups[i][1]
        stack.pop()
        i += 1
      else:
        break
  else:
    stack.append([color, count])
    i += 1

print(ans)