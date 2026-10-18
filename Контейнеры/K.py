n = int(input())
a = list(map(int, input().split()))

pref = [0] * (n + 1)
for i in range(n):
  pref[i + 1] = pref[i] + a[i]

a.append(-1)
stack = []
ans_val = -1
ans_l = 1
ans_r = 1

for i in range(n + 1):
  while stack and a[stack[-1]] >= a[i]:
    cur = stack.pop()
    l = stack[-1] + 1 if stack else 0
    r = i - 1
    val = a[cur] * (pref[r + 1] - pref[l])
    if val > ans_val:
      ans_val = val
      ans_l = l + 1
      ans_r = r + 1
  stack.append(i)

print(ans_val)
print(ans_l, ans_r)