n, c = map(int, input().split())
h = [int(input()) for _ in range(n - 1)]

stack = [[1, 0.0, float('inf')]]
ans = []

for i in range(n - 1):
  right_barrier = h[i]

  while c > 0:
    w, cur_h, left_barrier = stack[-1]
    target_h = min(left_barrier, right_barrier)

    if cur_h < target_h:
      needed = w * (target_h - cur_h)
      if c <= needed:
        stack[-1][1] += c / w
        c = 0
        break
      else:
        c -= needed
        stack[-1][1] = target_h
        cur_h = target_h

    if cur_h == left_barrier:
      right_block = stack.pop()
      stack[-1][0] += right_block[0]
      stack[-1][1] = cur_h
    else:
      break

  if c == 0:
    break


  stack.append([1, 0.0, right_barrier])

while c > 0:
  w, cur_h, left_barrier = stack[-1]
  if cur_h < left_barrier:
    needed = w * (left_barrier - cur_h)
    if c <= needed:
      stack[-1][1] += c / w
      c = 0
      break
    else:
      c -= needed
      stack[-1][1] = left_barrier
      cur_h = left_barrier

  if cur_h == left_barrier and len(stack) > 1:
    right_block = stack.pop()
    stack[-1][0] += right_block[0]
    stack[-1][1] = cur_h
  else:
    stack[-1][1] += c / stack[-1][0]
    c = 0
    break


levels = []
for w, cur_h, _ in stack:
  levels.extend([cur_h] * w)

while len(levels) < n:
  levels.append(0.0)

for val in levels:
  print(f"{val:.16f}")