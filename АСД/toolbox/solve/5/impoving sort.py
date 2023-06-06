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

arr = [5, 2, 8, 3, 9, 4, 6, 7, 1]
sorted_arr = QuickSort(arr)
print(sorted_arr)
