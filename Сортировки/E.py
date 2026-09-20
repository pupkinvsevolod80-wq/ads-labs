def mergesort(arr):
    if len(arr) <= 1:
        return arr
    ind = len(arr)//2
    left = mergesort(arr[:ind])
    right = mergesort(arr[ind:])
    return merge(left, right)

def merge(left, right):
    result = []
    i , j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i < len(left):
        result.extend(left[i:])
    if j < len(right):
        result.extend(right[j:])
    return result
N = int(input())
arr = list(map(int, input().split()))
print(*mergesort(arr))