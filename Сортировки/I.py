s1 = input()
s2 = input()

if len(s1) != len(s2):
    print("NO")
else:
    ch1 = list(s1)
    flag = True
    for j in s2:
        if j in ch1:
            ch1.remove(j)
        else:
            flag = False
            break
    print("YES" if flag else "NO")
