import matplotlib.pyplot as plt
import matplotlib.animation as animation

class BucketAnimation():
    def __init__(self, array):
        self.array = array
        self.fig, self.ax = plt.subplots()

    def bucket_sort(self):
        num_buckets = len(self.array)
        buckets = [[] for _ in range(num_buckets)]
        min_val = min(self.array)
        max_val = max(self.array)
        bucket_range = (max_val - min_val) / num_buckets

        for i, num in enumerate(self.array):
            index_b = int((num - min_val) // bucket_range)
            if index_b == num_buckets:
                index_b -= 1
            buckets[index_b].append(num)
            #print(buckets)
            yield buckets, i

        sorted_array = []
        for bucket in buckets:
            sorted_array.extend(sorted(bucket))
            yield buckets, sorted_array

    def update(self, frame):
        buckets, result = frame
        if isinstance(result, list):
            self.ax.clear()
            self.ax.set_xlim(0, len(result))
            self.ax.set_ylim(0, max(result))
            self.ax.bar(range(len(result)), result, align='edge', color='green')
            self.ax.set_xlabel('Елементи')
            self.ax.set_ylabel('Значення')
            self.ax.set_title('Блочне сортування')
            for i, val in enumerate(result):
                self.ax.text(i, val, f'{val}', ha='center', va='bottom')
        else:
            index = result
            self.ax.clear()
            self.ax.set_xlim(0, len(self.array))
            self.ax.set_ylim(0, max(self.array))
            for i, bucket in enumerate(buckets):
                for j, num in enumerate(bucket):
                    if i <= index:
                        self.ax.bar(i, num, align='edge', color='blue', alpha=(j + 1) / len(bucket))
                    else:
                        self.ax.bar(i, num, align='edge', color='gray', alpha=(j + 1) / len(bucket))
                    #self.ax.text(i, num, f'{num}', ha='center', va='bottom')
            self.ax.set_xlabel('Кошики')
            self.ax.set_ylabel('Значення')
            self.ax.set_title('Блочне сортування')

    def animate(self):
        anim = animation.FuncAnimation(self.fig, self.update, frames=self.bucket_sort(), interval=100, repeat=False)
        plt.show()

class CountingSortAnimation:
    def __init__(self, arr):
        self.arr = arr
        self.fig, self.ax = plt.subplots()
        self.bar_rects = self.ax.bar(range(len(arr)), arr, align="edge")
        # self.ax.set_xlim(0, len(arr))
        # self.ax.set_ylim(0, max(arr))
        self.anim = None

    def counting_sort_animation(self):
        min_val = min(self.arr)
        max_val = max(self.arr)
        count = [0] * (max_val - min_val + 1)

        # Підрахунок кількості входжень кожного елемента
        for num in self.arr:
            count[num - min_val] += 1

        # Анімація швидкого проходження сортувального лічильника по несортованому масиву
        for i in range(len(self.arr)):
            self.highlight_bar(i)
            yield self.arr

        for i in range(len(self.arr)-1, -1, -1):
            self.highlight_bar(i)
            yield self.arr

        # Створення відсортованого масиву за допомогою підрахунку
        sorted_arr = []
        for i, freq in enumerate(count):
            sorted_arr.extend([i + min_val] * freq)

        # Анімація показу відсортованого масиву
        for i in range(len(sorted_arr)):
            self.highlight_bar_sorted(i)
            yield sorted_arr[:i+1]

    def highlight_bar(self, index):
        for i, rect in enumerate(self.bar_rects):
            if i == index:
                rect.set_color('salmon')  # Зміна кольору поточного стовпця
                rect.set_edgecolor('black')
                rect.set_linewidth(0.5)
            else:
                rect.set_color('royalblue')  # Використання стандартного коліру всіх інших стовпців
                rect.set_edgecolor('white')
                rect.set_linewidth(0.5)

    def highlight_bar_sorted(self, index):
        for i, rect in enumerate(self.bar_rects):
            if i <= index:
                rect.set_color('blue')  # Зміна кольору відсортованих стовпців
                rect.set_edgecolor('white')
                rect.set_linewidth(0.5)
            else:
                rect.set_color('royalblue')
                rect.set_edgecolor('white')
                rect.set_linewidth(0.5)

    def update_fig(self, frame):
        for rect, val in zip(self.bar_rects, frame):
            rect.set_height(val)
        self.ax.set_title('Сортування підрахунком')
        self.ax.set_xlabel('Елементи')
        self.ax.set_ylabel('Значення')

    def animate(self):
        frames = self.counting_sort_animation()
        self.anim = animation.FuncAnimation(self.fig, self.update_fig, frames=frames, repeat=False)
        plt.show()


class RadixSortAnimation():
    def __init__(self, array):
        self.array = array
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim(0, len(self.array))
        self.ax.set_ylim(0, max(self.array))
        self.rects = self.ax.bar(range(len(self.array)), self.array, align='edge')

    def radix_sort(self):
        max_value = max(self.array)
        num_digits = len(str(max_value))
        for digit in range(num_digits):
            buckets = [[] for _ in range(len(self.array))]  # Create empty buckets for each digit
            for num in self.array:
                # Extract the digit at the current position
                digit_value = (num // 10 ** digit) % 10
                buckets[digit_value].append(num)
                yield buckets  # Yield the current state of buckets

            # Update the array with numbers from the buckets
            self.array = [num for bucket in buckets for num in bucket]
            yield self.array  # Yield the final state of the array

    def update(self, frame):
        if isinstance(frame[0], list):
            # Update the histogram with buckets
            self.ax.clear()
            self.ax.set_xlim(0, 10)
            self.ax.set_ylim(0, max(self.array))
            for i, bucket in enumerate(frame):
                for j, num in enumerate(bucket):
                    self.ax.bar(i, num, align='edge', color='blue', alpha=(j + 1) / len(bucket))
                    self.ax.text(i, num, f'{i}', ha='center', va='bottom')
        else:
            # Update the histogram with the sorted array
            self.ax.clear()
            self.ax.set_xlim(0, len(frame))
            self.ax.set_ylim(0, max(frame))
            for i, num in enumerate(frame):
                self.ax.bar(i, num, align='edge', color='blue')
                #self.ax.text(i, num, f'{num}', ha='center', va='bottom')
            plt.pause(1)

        self.ax.set_xlabel('Elements')
        self.ax.set_ylabel('Values')
        self.ax.set_title('Radix Sort')

    def animate(self):
        anim = animation.FuncAnimation(self.fig, self.update, frames=self.radix_sort(), interval=100, repeat=False)
        plt.show()
