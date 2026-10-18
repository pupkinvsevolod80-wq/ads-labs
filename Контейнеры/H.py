from collections import deque
n = int(input())
left = deque()
right = deque()
ans = []

for _ in range(n):
  cmd = input().split()
  if cmd[0] == "+":
    right.append(cmd[1])
  elif cmd[0] == "*":
    right.appendleft(cmd[1])
  elif cmd[0] == "-":
    ans.append(left.popleft())

  if len(left) < len(right):
    left.append(right.popleft())

print("\n".join(ans))