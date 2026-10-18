ls = input().split()
stack = []

for c in ls:
    if c in ['+', '-', '*']:
        b = stack.pop()
        a = stack.pop()
        if c == '+':
            res = a + b
        elif c == '-':
            res = a - b
        elif c == '*':
            res = a * b
        stack.append(res)
    else:
        stack.append(int(c))

print(stack[0])