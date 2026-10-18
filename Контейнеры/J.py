t = int(input())

for _ in range(t):
  data = input().split()
  k = int(data[0])
  arr = [float(x) for x in data[1:]]

  target = sorted(arr)
  stack = []
  idx = 0

  for x in arr:
    stack.append(x)
    while stack and stack[-1] == target[idx]:
      stack.pop()
      idx += 1

  if not stack:
    print(1)
  else:
    print(0)