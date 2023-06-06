import matplotlib.pyplot as plt
import numpy as np
import random
import math

def InsertionSort(arr, flag):
    count = count2 = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0:
            count += 1
            if key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
                count2 += 1
            else:
                break
        arr[j + 1] = key
    if flag:
        return count
    else:
        return count + count2

def partition(arr, low, high, flag):
    pivot = arr[high]
    i = low - 1
    count = 0
    count2 = 0
    for j in range(low, high):
        count += 1
        if arr[j] <= pivot:
            i += 1
            count2 += 1
            arr[i], arr[j] = arr[j], arr[i]
    count2 += 1
    arr[i+1], arr[high] = arr[high], arr[i+1]
    if flag:
        return i + 1, count
    else:
        return i + 1, count + count2

def median(arr, r, l):
    mid = (r + l) // 2
    if arr[r] < arr[mid] < arr[l] or arr[l] < arr[mid] < arr[r]:
        return mid
    elif arr[mid] <= arr[r] <= arr[l] or arr[l] <= arr[r] <= arr[mid]:
        return r
    else:
        return l

def partition_median(array, left, right, flag):
    count = 0
    count2 = 0
    mid = median(array, left, right)
    array[mid], array[right] = array[right], array[mid]
    pivot = array[right]
    i = left - 1
    for j in range(left, right):
        count += 1
        if array[j] <= pivot:
            i += 1
            count2 += 1
            array[i], array[j] = array[j], array[i]
    count2 += 1
    array[i+1], array[right] = array[right], array[i+1]
    if flag:
        return i + 1, count
    else:
        return i + 1, count + count2

def OuickSort(arr, low, high, flag):
    if low < high:
        pivot_index, comparison = partition(arr, low, high, flag)
        comparison += OuickSort(arr, low, pivot_index-1, flag)[1]
        comparison += OuickSort(arr, pivot_index+1, high, flag)[1]
        return arr, comparison
    else:
        return arr, 0

def OuickSortWithMedian(array, left, right, flag):
    result = 0
    if right - left > 2:
        pivotindex, result1 = partition_median(array, left, right, flag)
        result += result1
        result += OuickSortWithMedian(array, left, pivotindex-1, flag)
        result += OuickSortWithMedian(array, pivotindex + 1, right, flag)
    else:
        result += InsertionSort(array[left:right + 1], flag)
    return result

def apr(sizes, arr):
    fp = np.polyfit(sizes, arr, 2)
    f = np.poly1d(fp)
    return f

def choice():
    print("1. File input")
    print("2. Enter manually")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        file_add()
    elif ch == 2:
        graph()
    return

def graph():
    n = int(input("Enter the size of the array: "))
    a1 = list(range(1, n + 1))
    a2 = list(range(n, 0, -1))
    a3 = random.sample(range(1, n+1), n)
    sizes = range(1, n + 1)
    flag = False
    w = [i ** 2 for i in sizes]
    b = [i * math.log(i) for i in sizes]
    o1 = [OuickSort(a1[:size], 0, size-1, flag) for size in sizes]
    o2 = [OuickSort(a2[:size], 0, size-1, flag) for size in sizes]
    o3 = [OuickSort(a3[:size], 0, size-1, flag) for size in sizes]
    op1 = [tup[1] for tup in o1]
    op2 = [tup[1] for tup in o2]
    op3 = [tup[1] for tup in o3]
    op1_m = [OuickSortWithMedian(a1[:size], 0, size-1, flag) for size in sizes]
    op2_m = [OuickSortWithMedian(a2[:size], 0, size-1, flag) for size in sizes]
    op3_m = [OuickSortWithMedian(a3[:size], 0, size-1, flag) for size in sizes]
    gr1 = apr(sizes, op1)
    gr2 = apr(sizes, op2)
    gr3 = apr(sizes, op3)
    gr1_m = apr(sizes, op1_m)
    gr2_m = apr(sizes, op2_m)
    gr3_m = apr(sizes, op3_m)
    plt.title('Quick Sort')
    plt.plot(sizes, w, 'm', label="Worst time asymptote", linewidth=0.8)
    plt.plot(sizes, b, 'y', label="Best time asymptote", linewidth=0.8)
    plt.plot(sizes, gr1(sizes), 'r', label="Best", linewidth=0.8)
    plt.plot(sizes, gr2(sizes), 'k', label="Worst", linewidth=0.8)
    plt.plot(sizes, gr3(sizes), 'c', label="Random", linewidth=0.8)
    plt.xlabel('Elements')
    plt.ylabel('Operations')
    plt.legend(loc="upper left")
    plt.show()
    plt.title('Quick Sort with median')
    plt.plot(sizes, w, 'm', label="Worst time asymptote",linewidth=0.8)
    plt.plot(sizes, b, 'y', label="Best time asymptote", linewidth=0.8)
    plt.plot(sizes, gr1_m(sizes), 'r', label="Best", linewidth=0.8)
    plt.plot(sizes, gr2_m(sizes), 'k', label="Worst", linewidth=0.8)
    plt.plot(sizes, gr3_m(sizes), 'c', label="Random", linewidth=0.8)
    plt.xlabel('Elements')
    plt.ylabel('Operations')
    plt.legend(loc="upper left")
    plt.show()

def file_add():
    name = input("Enter the file name: ")
    file_path = name

    with open(file_path, 'r') as file:
        numbers = [int(line.strip()) for line in file.readlines()]
    del numbers[0]
    size = len(numbers)
    numbers2 = numbers.copy()
    flag = True
    array, comp = OuickSort(numbers, 0, size - 1, flag)
    comp2 = OuickSortWithMedian(numbers2, 0, size - 1, flag)
    newname = name[5:-4]
    newname = "Zubarev_ip23" + newname + "_output.txt"

    with open(newname, 'w') as out:
        out.write(str(comp) + " " + str(comp2))
        out.write("\n")
    out.close()
    print(str(comp) + " " + str(comp2))

if __name__ == '__main__':
    choice()
