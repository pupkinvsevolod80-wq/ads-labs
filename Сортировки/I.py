s1 = input()
s2 = input()

if len(s1) != len(s2):
    print("NO")
else:
    ch1 = list(s1)
    ok = True
    for j in s2:
        if j in ch1:
            ch1.remove(j)
        else:
            ok = False
            break
    print("YES" if ok else "NO")