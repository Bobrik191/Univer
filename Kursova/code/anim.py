import time
import random
import matplotlib
import PyQt6
from PyQt6.QtGui import QImage, QPixmap
from matplotlib.animation import FuncAnimation
from PyQt6 import QtCore, QtGui, QtWidgets
import matplotlib.animation as animation

from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QWidget, QGraphicsScene, QGraphicsView, QSizePolicy
from PySide6.QtCharts import QChart, QChartView, QBarSeries, QBarSet, QValueAxis, QCategoryAxis
from PySide6.QtGui import QPainter, QBrush
from PySide6.QtCore import QCoreApplication, QThread, Signal, QRectF, Qt
from matplotlib import pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import ttk
import plotly.graph_objects as go
matplotlib.use('Qt5Agg')
class RadixSortAnimation():
    def __init__(self, array):
        self.array = array
        self.fig, self.ax = plt.subplots(2, 1, figsize=(6, 8))
        self.ax[0].set_xlim(0, len(self.array))
        self.ax[0].set_ylim(0, max(self.array))
        self.ax[1].set_xlim(0, 10)
        self.ax[1].set_ylim(0, max(self.array))
        self.rects = self.ax[0].bar(range(len(self.array)), self.array, align='edge')

    def radix_sort(self):
        max_value = max(self.array)
        num_digits = len(str(max_value))
        for digit in range(num_digits):
            buckets = [[] for _ in range(len(self.array))]  # Create empty buckets for each digit
            for num in self.array:
                # Extract the digit at the current position
                digit_value = (num // 10 ** digit) % 10
                buckets[digit_value].append(num)
                print(buckets)
                yield buckets  # Yield the current state of buckets

            # Update the array with numbers from the buckets
            self.array = [num for bucket in buckets for num in bucket]
            yield buckets  # Yield the final state of buckets

    def update(self, frame):
        buckets = frame
        self.ax[0].clear()
        self.ax[0].set_xlim(0, 10)
        self.ax[0].set_ylim(0, max(self.array))
        for i, bucket in enumerate(buckets):
            for j, num in enumerate(bucket):
                self.ax[0].bar(i, num, align='edge', color='blue')
                self.ax[0].text(i, num, f'{num}', ha='center', va='bottom')
        self.ax[0].set_xlabel('Elements')
        self.ax[0].set_ylabel('Values')
        self.ax[0].set_title('Radix Sort')

    def animate(self):
        anim = animation.FuncAnimation(self.fig, self.update, frames=self.radix_sort(), interval=10, repeat=False)

        sorted_array = sorted(self.array)
        self.ax[1].clear()
        self.ax[1].set_xlim(0, len(sorted_array))
        self.ax[1].set_ylim(0, max(sorted_array))
        for i, num in enumerate(sorted_array):
            self.ax[1].bar(i, num, align='edge', color='green')
            #self.ax[1].text(i, num, f'{num}', ha='center', va='bottom')
        self.ax[1].set_xlabel('Elements')
        self.ax[1].set_ylabel('Values')
        self.ax[1].set_title('Sorted Array')

        plt.tight_layout()
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
                print(buckets)
                yield buckets  # Yield the current state of buckets

            # Update the array with numbers from the buckets
            self.array = [num for bucket in buckets for num in bucket]
            yield buckets  # Yield the final state of buckets

    def update(self, frame):
        buckets = frame
        self.ax.clear()
        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(0, max(self.array))
        for i, bucket in enumerate(buckets):
            for j, num in enumerate(bucket):
                self.ax.bar(i, num, align='edge', color='blue', alpha=(j + 1) / len(bucket))
                self.ax.text(i, num, f'{i}', ha='center', va='bottom')
        self.ax.set_xlabel('Elements')
        self.ax.set_ylabel('Values')
        self.ax.set_title('Radix Sort')

    def animate(self):
        anim = animation.FuncAnimation(self.fig, self.update, frames=self.radix_sort(), interval=100, repeat=False)
        plt.show()

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
            self.ax.set_xlabel('Elements')
            self.ax.set_ylabel('Values')
            self.ax.set_title('Bucket Sort')
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
            self.ax.set_xlabel('Elements')
            self.ax.set_ylabel('Values')
            self.ax.set_title('Bucket Sort')

    def animate(self):
        anim = animation.FuncAnimation(self.fig, self.update, frames=self.bucket_sort(), interval=200, repeat=False)
        plt.show()
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(800, 470)
        Dialog.setStyleSheet(
            u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(28, 0, 124, 255), stop:1 rgba(0, 26, 171, 255));")

        self.retranslateUi(Dialog)

        QCoreApplication.processEvents()

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))



class SortAnim(QDialog):
    def __init__(self):
        super().__init__()
        # self.setWindowTitle("Array Dialog")
        # self.setFixedSize(800, 600)
        # self.setStyleSheet("background-color: #1c007c; color: white; font-size: 20px; font-family: Arial; font-weight: bold;")

    def block_sort_animation(self, array):
        def animate():
            nonlocal blocks
            if blocks:
                block = blocks.pop(0)
                canvas.delete('all')

                # Отрисовка текущего блока
                for i, num in enumerate(block):
                    x = i * block_width
                    y = canvas_height - (num * block_height)
                    canvas.create_rectangle(x, y, x + block_width, canvas_height, fill='blue')

                root.after(animation_speed, animate)

        root = tk.Tk()
        root.title("Block Sort Animation")

        canvas_width = 800
        canvas_height = 400

        canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
        canvas.pack()

        block_width = 20
        block_height = 5

        # Разделение элементов по блокам
        min_val = min(array)
        max_val = max(array)
        block_size = int((max_val - min_val) / len(array)) + 1

        blocks = [[] for _ in range(len(array))]
        for num in array:
            block_index = int((num - min_val) / block_size)
            blocks[block_index].append(num)

        animation_speed = 500  # Задержка между кадрами анимации (в миллисекундах)

        animate()

        root.mainloop()
    # def block_sort_animation(self, A):
    #     root = tk.Tk()
    #     root.withdraw()
    #
    #     fig, ax = plt.subplots()
    #     canvas = FigureCanvas(fig)
    #
    #     def draw_bars():
    #         ax.clear()
    #         ax.bar(range(len(A)), A)
    #         canvas.draw()
    #
    #     def block_sort():
    #         n = len(A)
    #         block_size = int(n ** 0.5)
    #
    #         for i in range(0, n, block_size):
    #             block = A[i:i + block_size]
    #             block.sort()
    #             A[i:i + block_size] = block
    #             draw_bars()
    #             QApplication.processEvents()  # Process events to update the UI
    #             root.after(500)
    #
    #     draw_bars()
    #
    #     main_widget = QWidget()
    #     main_layout = QVBoxLayout(main_widget)
    #     main_layout.addWidget(canvas)
    #
    #     window = QDialog()
    #     window.setWindowTitle("Block Sort Animation")
    #     window.show()
    #
    #     root.after(1000, block_sort)
    #     root.mainloop()


class CountAnim():
    def __init__(self):
        super().__init__()

    def counting_sort_animation(self, data):
        fig, ax = plt.subplots()
        ax.set_xlim(0, len(data))
        ax.set_ylim(0, max(data) + 1)

        bar_rects = ax.bar(range(len(data)), data, align="edge")

        def update_fig(frame):
            for rect, h in zip(bar_rects, frame):
                rect.set_height(h)

        counts = [0] * (max(data) + 1)
        for num in data:
            counts[num] += 1

        sorted_data = []
        for i, count in enumerate(counts):
            sorted_data.extend([i] * count)
        print(sorted_data)
        frames = []
        for i in range(len(data)):
            frames.append(sorted_data[:i + 1])

        anim = animation.FuncAnimation(fig, update_fig, frames=frames, repeat=False)

        plt.show()
class SortingAlgorithm:

    def counting_sort(self, array):
        size = len(array)
        output = [0] * size

        # Find the maximum value in the array
        max_value = max(array)

        # Initialize count array
        count = [0] * (max_value + 1)

        # Store the count of each element in count array
        for i in range(size):
            count[array[i]] += 1

        # Store the cumulative count
        for i in range(1, max_value + 1):
            count[i] += count[i - 1]

        i = size - 1
        while i >= 0:
            output[count[array[i]] - 1] = array[i]
            count[array[i]] -= 1
            i -= 1

        sorted_array = output

        #sorted_array = output.copy()

        return sorted_array
    def animate_counting_sort(self, array):
        fig, ax = plt.subplots()

        def update(frame):
            if frame > 0:
                ax.cla()

            sub_array = array[:frame+1]
            sorted_sub_array = self.counting_sort(sub_array)

            ax.bar(range(len(sorted_sub_array)), sorted_sub_array)
            ax.set_title("Counting Sort - Step {}".format(frame+1))
            ax.set_xlabel("Index")
            ax.set_ylabel("Value")

        animation = FuncAnimation(fig, update, frames=len(array), interval=1000, repeat=False)
        plt.show()
    def countingSort(self, array, place):
        size = len(array)
        output = [0] * size

        max_value = max(array)

        count = [0] * (max_value + 1)

        # Calculate count of elements
        for i in range(0, size):
            index = array[i] // place
            count[index % 10] += 1

        # Calculate cumulative count
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Place the elements in sorted order
        i = size - 1
        while i >= 0:
            index = array[i] // place
            output[count[index % 10] - 1] = array[i]
            count[index % 10] -= 1
            i -= 1

        # Create a new array to store the sorted elements
        sorted_array = output

        return sorted_array

    def radix_sort(self, array):
        # Get maximum element
        max_element = max(array)

        # Create a new array to store the sorted elements
        sorted_array = array.copy()

        # Apply counting sort to sort elements based on place value.
        place = 1
        while max_element // place > 0:
            sorted_array = self.countingSort(sorted_array, place)
            place *= 10

        return sorted_array


#
# # Generate a random array
# array = [randint(0, 100000) for _ in range(100)]
#
# # Create an instance of the SortingAlgorithm class
# sorter = SortingAlgorithm()
#
# # Perform counting sort and display the sorted array
# sorted_array = sorter.counting_sort(array)
# print("Counting Sort:", sorted_array)
#
# # Perform radix sort and display the sorted array
# sorted_array = sorter.radix_sort(array)
# print("Radix Sort:", sorted_array)
#
# # Plot the initial array
# plt.figure()
# plt.bar(range(len(array)), array)
# plt.title("Initial Array")
# plt.xlabel("Index")
# plt.ylabel("Value")
# plt.show()
#
# # Plot the sorted array after counting sort
# plt.figure()
# plt.bar(range(len(sorted_array)), sorted_array)
# plt.title("Counting Sort")
# plt.xlabel("Index")
# plt.ylabel("Value")
# plt.show()
#
# # Plot the sorted array after radix sort
# plt.figure()
# plt.bar(range(len(sorted_array)), sorted_array)
# plt.title("Radix Sort")
# plt.xlabel("Index")
# plt.ylabel("Value")
# plt.show()

class AnimationDialog:
    def __init__(self):
        super().__init__()

    def counting_sort_animation(self, array):
        min_val = min(array)
        max_val = max(array)
        range_val = max_val - min_val + 1

        count = [0] * range_val
        frames = []

        for num in array:
            count[num - min_val] += 1
            frames.append(count[:])  # Добавляем текущее состояние подсчета в список кадров

        data = []
        for i, frame in enumerate(frames):
            bars = go.Bar(x=list(range(min_val, max_val + 1)), y=frame, marker_color='lightskyblue')
            data.append(bars)

        layout = go.Layout(
            title='Counting Sort Animation',
            xaxis=dict(title='Number'),
            yaxis=dict(title='Frequency'),
            updatemenus=[dict(type='buttons', buttons=[dict(label='Play', method='animate', args=[None, {
                'frame': {'duration': 500, 'redraw': True}, 'fromcurrent': True, 'transition': {'duration': 0}}])])],
        )

        fig = go.Figure(data=data, layout=layout)
        fig.update_layout(autosize=False, width=800, height=500)

        fig.show()
class CustomDialog:
    def __init__(self):
        super().__init__()
        #self.setWindowTitle("Custom Dialog")

    def bucket_sort_animation(self, array):
        n = len(array)
        min_val = min(array)
        max_val = max(array)
        bucket_range = (max_val - min_val) / n

        buckets = [[] for _ in range(n)]

        for num in array:
            index_b = int((num - min_val) // bucket_range)
            if index_b == n:
                index_b -= 1
            buckets[index_b].append(num)

        sorted_array = []
        frames = []

        for i, bucket in enumerate(buckets):
            sorted_bucket = []
            for _ in range(len(bucket)):
                min_val = min(bucket)
                sorted_bucket.append(min_val)
                bucket.remove(min_val)
            sorted_array.extend(sorted_bucket)
            frames.append(go.Frame(data=[go.Bar(x=list(range(n)), y=sorted_array)], name=f'Frame {i + 1}'))

        fig = go.Figure(data=[go.Bar(x=list(range(n)), y=array)], frames=frames)
        fig.update_layout(title_text="Bucket Sort Animation")
        fig.update_layout(updatemenus=[dict(type='buttons', showactive=False,
                                            buttons=[dict(label='Play',
                                                          method='animate',
                                                          args=[None, {'frame': {'duration': 500, 'redraw': True},
                                                                       'fromcurrent': True,
                                                                       'transition': {'duration': 0}}]),
                                                     dict(label='Pause',
                                                          method='animate',
                                                          args=[[None], {'frame': {'duration': 0, 'redraw': False},
                                                                         'mode': 'immediate',
                                                                         'transition': {'duration': 0}}])])])

        fig.write_html("bucket_sort_animation.html", auto_open=True)

    # def bucket_sort_animation(self, array):
    #     max_val = max(array)
    #     min_val = min(array)
    #     range_val = max_val - min_val
    #
    #     num_buckets = len(array)
    #     bucket_size = range_val / num_buckets
    #
    #     buckets = [[] for _ in range(num_buckets)]
    #
    #     for num in array:
    #         index_b = int((num - min_val) // bucket_size)
    #         if index_b == num_buckets:
    #             index_b -= 1
    #         buckets[index_b].append(num)
    #
    #     sorted_array = []
    #     frames = []
    #
    #     for bucket in buckets:
    #         # Сортировка вставками внутри каждой корзины
    #         for i in range(1, len(bucket)):
    #             key = bucket[i]
    #             j = i - 1
    #             while j >= 0 and bucket[j] > key:
    #                 bucket[j + 1] = bucket[j]
    #                 j -= 1
    #             bucket[j + 1] = key
    #         sorted_array.extend(bucket)
    #         frames.append(sorted_array.copy())
    #
    #     fig, ax = plt.subplots()
    #     ax.set_xlim(0, len(array))
    #     ax.set_ylim(min(array), max(array))
    #     rects = ax.bar(range(len(array)), array, align='edge')
    #
    #     def update(frame):
    #         heights = frames[frame]
    #         for rect, h in zip(rects, heights):
    #             rect.set_height(h)
    #
    #     anim = animation.FuncAnimation(fig, update, frames=len(frames), repeat=False)
    #     anim.save('bucket_sort.gif', writer='pillow', fps=1)
    #     plt.show()
#class AnimationDialog:
#     def __init__(self, array):
#         self.fig, self.ax = plt.subplots()
#         self.rects = None
#         self.array = array
#
#     def update_histogram(self, frame):
#         self.ax.clear()
#         counts = [0] * (max(self.array[frame]) + 1)
#         for num in self.array[frame]:
#             counts[num] += 1
#         x = range(len(counts))
#         self.rects = self.ax.bar(x, counts, align='center')
#
#     def animate(self):
#         anim = animation.FuncAnimation(
#             self.fig, self.update_histogram, frames=len(self.array), interval=1000, repeat=False
#         )
#         plt.show()

