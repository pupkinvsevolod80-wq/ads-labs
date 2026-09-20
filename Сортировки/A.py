def SelectionSort(arr):
    n = len(arr)
    for i in range(n-1):
        key = arr[i]
        ind = i
        for j in range(i + 1, n):
            if arr[j] > key:
                key = arr[j]
                ind = j
        if  i != ind:
            arr[i], arr[ind] = arr[ind], arr[i]
    return arr           

numbers = list(map(int, input().split()))
SelectionSort(numbers)
print(*numbers)
