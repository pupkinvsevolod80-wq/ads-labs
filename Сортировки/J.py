arr = []
while True:
    try:
        line = input()
    except EOFError:
        break
    if line == "":
        break
    arr.append(line)

for i in range(len(arr)):
    for j in range(len(arr) - i -1):
        if arr[j] + arr[j+1] < arr[j+1] + arr[j]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print("".join(arr))