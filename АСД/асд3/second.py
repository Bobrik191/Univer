import matplotlib.pyplot as plt
import numpy as np
import random
import time

def bucket_sort(arr):
    min_val = min(arr)
    max_val = max(arr)
    bucket_size = 10  # Размер ведра
    bucket_count = (max_val - min_val) // bucket_size + 1
    buckets = [[] for _ in range(bucket_count)]

    for num in arr:
        index = (num - min_val) // bucket_size
        buckets[index].append(num)

    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))

    return sorted_arr

def generate_random_array(size):
    return [random.randint(1, 100) for _ in range(size)]

def measure_time(size):
    arr = generate_random_array(size)

    start_time = time.time()
    sorted_arr = bucket_sort(arr)
    end_time = time.time()

    return end_time - start_time

def plot_complexity():
    n = int(input('Введите размер массива: '))
    sizes = range(1, n + 1)
    avg_times = []

    for size in sizes:
        times = []
        for _ in range(10):
            time_taken = measure_time(size)
            times.append(time_taken)

        avg_time = np.mean(times)
        avg_times.append(avg_time)

    plt.plot(sizes, avg_times, 'b', label='Random case')
    plt.plot(sizes, [size**2 for size in sizes], 'r--', label='Worst case')

    plt.title('Algorithm Complexity: Bucket Sort')
    plt.xlabel('Input Size')
    plt.ylabel('Average Time (seconds)')
    plt.legend(loc='upper left')
    plt.show()

plot_complexity()
