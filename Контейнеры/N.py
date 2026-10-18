from collections import deque

p1 = deque(map(int, input().split()))
p2 = deque(map(int, input().split()))

moves = 0

while p1 and p2 and moves < 1000000:
  c1 = p1.popleft()
  c2 = p2.popleft()
  moves += 1

  if c1 == 0 and c2 == 9:
    p1.append(c1)
    p1.append(c2)
  elif c1 == 9 and c2 == 0:
    p2.append(c1)
    p2.append(c2)
  elif c1 > c2:
    p1.append(c1)
    p1.append(c2)
  else:
    p2.append(c1)
    p2.append(c2)

if not p1:
  print('second', moves)
elif not p2:
  print('first', moves)
else:
  print('botva')