from random import randint

def quick_sort(arr, left, right):
    if left < right:
        val = arr[randint(left, right)]
        l, r = left, right
        while l <= r:
            while arr[l] < val:
                l += 1
            while arr[r] > val:
                r -= 1
            if l <= r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
        if left < r:
            quick_sort(arr, left, r)
        if right > l:
            quick_sort(arr, l, right)

N = int(input())
arr = list(map(int, input().split()))
quick_sort(arr, 0, len(arr) - 1)
print(*arr)