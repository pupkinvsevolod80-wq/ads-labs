n = int(input())
train = list(map(int, input().split()))

stack = []
expected = 1

for car in train:
  stack.append(car)
  while stack and stack[-1] == expected:
    stack.pop()
    expected += 1

if not stack:
  print("YES")
else:
  print("NO")