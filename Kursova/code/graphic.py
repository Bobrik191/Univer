import matplotlib.pyplot as plt
import numpy as np
import random
import PyQt6
import time
import matplotlib
matplotlib.use('TkAgg')


class RadixTime():
    def countingSort(self, array, place):
        size = len(array)
        output = [0] * size
        operations = 0
        max_value = max(array)

        count = [0] * (max_value + 1)

        # Calculate count of elements
        for i in range(0, size):
            index = array[i] // place
            count[index % 10] += 1
            # Увеличиваем счетчик операций
            operations += 1

        # Calculate cumulative count
        for i in range(1, 10):
            count[i] += count[i - 1]
            # Увеличиваем счетчик операций
            operations += 1

        # Place the elements in sorted order
        i = size - 1
        while i >= 0:
            index = array[i] // place
            output[count[index % 10] - 1] = array[i]
            count[index % 10] -= 1
            i -= 1
            # Увеличиваем счетчик операций
            operations += 4

        # Create a new array to store the sorted elements
        sorted_array = output.copy()

        # Увеличиваем счетчик операций
        operations += size

        return sorted_array, operations

    def radix_sort(self, array):
        # Get maximum element
        max_element = max(array)

        # Create a new array to store the sorted elements
        sorted_array = array.copy()

        # Initialize transition counter
        operations = 0

        # Apply counting sort to sort elements based on place value.
        place = 1
        while max_element // place > 0:
            sorted_array, count = self.countingSort(sorted_array, place)
            operations += count
            place *= 10

        return sorted_array, operations

    def measure_time(self, array):
        start_time = time.time()
        sorted_arr = self.radix_sort(array)
        end_time = time.time()

        return end_time - start_time

    def plot_complexity(self, array):
        sizes = range(1, len(array) + 1)
        avg_times = []

        # for size in sizes:
        #     times = []
        #     for _ in range(10):
        #         time_taken = self.measure_time(array)
        #         times.append(time_taken)
        #     avg_time = np.mean(times)
        #     avg_times.append(avg_time)

        #plt.plot(sizes, operat, 'b', label='Average Time')
        plt.plot(sizes, [size for size in sizes], 'r', linestyle='dashdot', label='Best Case')
        plt.plot(sizes, [size for size in sizes], 'g--', label='Worst Case')
        plt.plot(sizes, [size for size in sizes], 'y--', label='Average Case')

        plt.title('Algorithm Complexity: Radix Sort')
        plt.xlabel('Input Size')
        plt.ylabel('Average Time (seconds)')
        plt.legend(loc='upper left')
        plt.show()


class CountingTime():
    def __init__(self):
        super().__init__()
    def counting_sort(self, array):
        operations = 0
        size = len(array)
        output = [0] * size

        # Find the maximum value in the array
        max_value = max(array)
        min_value = min(array)
        range_array = max_value - min_value

        # Initialize count array
        count = [0] * (range_array + 1)

        # Считаем количество каждого элемента в массиве
        for i in range(size):
            count[array[i] - min_value] += 1
            operations += 1

        # Вычисляем накопленное количество
        for i in range(1, range_array + 1):
            count[i] += count[i - 1]
            operations += 1

        # Восстанавливаем отсортированный массив
        i = size - 1
        while i >= 0:
            output[count[array[i] - min_value] - 1] = array[i]
            count[array[i] - min_value] -= 1
            i -= 1
            operations += 3

        sorted_array = output

        return sorted_array, operations

    def measure_time(self, array):
        start_time = time.time()
        sorted_arr = self.counting_sort(array)
        end_time = time.time()

        return end_time - start_time

    def plot_complexity(self, array):
        sizes = range(1, len(array) + 1)
        avg_times = []
        k = (max(array) - min(array)) // len(array)

        # for size in sizes:
        #     times = []
        #     for _ in range(10):
        #         time_taken = self.measure_time(array)
        #         times.append(time_taken)
        #     avg_time = np.mean(times)
        #     avg_times.append(avg_time)

        #plt.plot(sizes, avg_times, 'b', label='Average case')
        plt.plot(sizes, [size for size in sizes], 'r', linestyle='dashdot', label='Best case')
        plt.plot(sizes, [size for size in sizes], 'g', label='Worst case')
        plt.plot(sizes, [size for size in sizes], 'y--', label='Average case')

        plt.title('Algorithm Complexity: Counting Sort')
        plt.xlabel('Input Size')
        plt.ylabel('Average Time (seconds)')
        plt.legend(loc='upper left')
        plt.show()

class BucketTime():
    def __init__(self):
        super().__init__()
        # self.setWindowTitle("Sorting Visualization")
        # self.resize(800, 600)

    def measure_time(self, array):
        start_time = time.time()
        sorted_arr = self.bucket_sort(array)
        end_time = time.time()

        return end_time - start_time

    def plot_complexity(self, array):
        sizes = range(1, len(array) + 1)
        avg_times = []
        k = (max(array) - min(array)) // len(array)

        # for size in sizes:
        #     times = []
        #     for _ in range(len(array)):
        #         time_taken = self.measure_time(array)
        #         times.append(time_taken)
        #
        #     avg_time = np.mean(times)
        #     avg_times.append(avg_time)

        #plt.plot(sizes, avg_times, 'b', label='Random case')
        plt.plot(sizes, [size for size in sizes], 'g', label='Best case')
        plt.plot(sizes, [size ** 2 for size in sizes], 'r--', label='Worst case')
        plt.plot(sizes, [size + 10 for size in sizes], 'y', linestyle='dashdot', label='Average case')

        plt.title('Algorithm Complexity: Bucket Sort')
        plt.xlabel('Input Size')
        plt.ylabel('Average Time (seconds)')
        plt.legend(loc='upper left')
        plt.show()
    def bucket_sort(self, array):
        # Знайдемо максимальне та мінімальне значення у масиві
        max_val = max(array)
        min_val = min(array)
        range_val = max_val - min_val

        # Визначимо кількість блоків та розмір кожного блоку
        size = len(array)
        bucket_size = range_val / size

        # Створимо порожні блоки
        buckets = [[] for _ in range(size)]
        operations = 0
        # Розподілим елементи у масиві по блоках
        for num in array:
            operations += 1
            if min_val < 0:
                index_b = int((num - min_val) // range_val * (size - 1))
            else:
                index_b = int((num - min_val) // range_val * size)
            if index_b == size:
                index_b -= 1
            buckets[index_b].append(num)

        # Зіберемо відсортовані елементи з блоків
        sorted_array = []
        for bucket in buckets:
            # Використовуємо сортування вставкою у кожному блоку
            for i in range(1, len(bucket)):
                key = bucket[i]
                j = i - 1
                while j >= 0 and bucket[j] > key:
                    bucket[j + 1] = bucket[j]
                    j -= 1
                    operations += 2
                bucket[j + 1] = key
                operations += 1

            sorted_array.extend(bucket)
            #sorted_array += bucket
        return sorted_array, operations

