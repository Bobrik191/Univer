import random

def QuickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = []
    right = []
    middle = []
    for num in arr:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            middle.append(num)
    return QuickSort(left) + middle + QuickSort(right)

n = int(input())
arr = list(map(int, input().split()))
sorted_arr = QuickSort(arr)
print(' '.join(map(str, sorted_arr)))
