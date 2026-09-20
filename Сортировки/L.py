km = sorted(list(map(int, input().split())))
price = sorted(list(map(int, input().split())))
price_s = price[::-1]
summa = 0
for i in range(len(km)):
    summa += km[i] * price_s[i]
print(summa)