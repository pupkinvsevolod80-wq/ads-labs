dist = sorted(list(map(int, input().split())))
price = sorted(list(map(int, input().split())))
price_s = price[::-1]
sum = 0
for i in range(len(dist)):
    sum += dist[i] * price_s[i]
print(sum)
