from PySide6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect, QEasingCurve,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QShowEvent, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QMainWindow, QPushButton,QMessageBox,QFileDialog,QVBoxLayout, QDialog,
    QTextEdit, QWidget)
from PySide6 import QtCharts
import time
from animation import BucketAnimation, RadixSortAnimation, CountingSortAnimation
from graphic import BucketTime, CountingTime, RadixTime
from random import randint
from mas import Ui_MainWindow
from dialog import ArrayDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Generate.clicked.connect(self.generate_array)
        self.ui.Sort.clicked.connect(self.sort_array)
        self.ui.Clear.clicked.connect(self.clear_arrays)
        self.ui.Save.clicked.connect(self.save_array)
        self.ui.Graph.clicked.connect(self.draw_graph)
        self.ui.Animation.clicked.connect(self.draw_animation)



        self.generated_array = []
        self.sorted_array = []
        self.file_name = ""


    def update_color(self, name, title, text):
        name = QMessageBox(self)
        #name.setFixedSize(500, 500)
        name.setWindowTitle(f"{title}")
        name.setText(f"{text}")
        name.setTextInteractionFlags(Qt.TextSelectableByMouse)
        name.setStyleSheet("QLabel {color: white;}""QMessageBox QPushButton {background-color: white;}")
        name.exec_()

    def generate_array(self):
        if not self.generated_array:
            min_text = self.ui.MinEdit.toPlainText()
            max_text = self.ui.MaxEdit.toPlainText()

            if min_text == '' or max_text == '':
                war_box = QMessageBox(self)
                self.update_color(war_box, "Invalid Input", "Please enter values for minimum and maximum values.")
                return

            min_value = int(min_text)
            max_value = int(max_text)

            if min_value >= max_value:
                war_box = QMessageBox(self)
                self.update_color(war_box, "Invalid Input", "Minimal value should be less than maximum.")
                self.ui.MinEdit.clear()
                self.ui.MaxEdit.clear()
                return
            # if min_value < 0 or max_value < 0:
            #     self.ui.MinEdit.clear()
            #     self.ui.MaxEdit.clear()
            #     war_box = QMessageBox(self)
            #     self.update_color(war_box, "Invalid Input", "Please enter positive values.")
            #     return

            text = self.ui.NumEdit.toPlainText()
            try:
                num_chars = int(text)
                if num_chars < 100 or num_chars > 50000:
                    war_box = QMessageBox(self)
                    self.update_color(war_box,"Invalid Input", "Please enter number more than 100 and less than 50000.")
                    self.ui.NumEdit.clear()
                    #QMessageBox.warning(self, "Invalid Input", "Please enter a valid number of characters.")
                else:
                    #self.generated_array = [uniform(min_value, max_value) for _ in range(num_chars)]
                    self.generated_array = [randint(min_value, max_value) for _ in range(num_chars)]
                    self.show_array(self.generated_array)
            except ValueError:
                war_box = QMessageBox(self)
                self.update_color(war_box,"Invalid Input", "Please enter a valid number of characters.")
                #QMessageBox.warning(self, "Invalid Input", "Please enter a valid number of characters.")
        else:
            gen_box = QMessageBox
            self.update_color(gen_box, "Array Generated", f"Your array has already been generated")
            self.show_array(self.generated_array)


    def bucket_animation(self):
        bucket = BucketAnimation(self.generated_array)
        bucket.animate()

    def clear_arrays(self):
        # Очистка массивов
        self.generated_array = []
        self.sorted_array = []
        self.clear_file()
        msg = QMessageBox(self)
        self.update_color(msg, "Очищення масива", "Масиви очищено")

    def show_array(self, array):
        dialog = ArrayDialog(array)
        dialog.exec()

    def sort_array(self):
        if not self.generated_array:
            war_box = QMessageBox(self)
            self.update_color(war_box, "Array Not Generated", "Please generate an array first.")
            #QMessageBox.warning(self, "Array Not Generated", "Please generate an array first.")
            return

        if not self.sorted_array:
            # Получение выбранного метода сортировки из QComboBox
            selected_sorting_method = self.ui.ComboSort.currentText()

            # Применение выбранного метода сортировки
            if selected_sorting_method == "Блочне сортування":
                self.sorted_array = self.bucket_sort(self.generated_array)
            elif selected_sorting_method == "Сортування підрахунком":
                self.sorted_array = self.counting_sort(self.generated_array)
            elif selected_sorting_method == "Порозрядне сортування":
                self.sorted_array = self.radix_sort(self.generated_array)
            else:
                self.sorted_array = self.generated_array
        self.show_array(self.sorted_array)

    def draw_animation(self):
        if not self.generated_array:
            msg = QMessageBox(self)
            self.update_color(msg, "Array Not Generated", "Please generate an array first.")
            return
        if len(self.generated_array) > 300:
            msg = QMessageBox(self)
            self.update_color(msg, "Too many elements", "Please generate less than 300 elements.")
            return

        #window = CustomDialog()
        select_method = self.ui.ComboSort.currentText()
        if select_method == "Блочне сортування":
            bucket = BucketAnimation(self.generated_array)
            bucket.animate()
        elif select_method == "Сортування підрахунком":
            counting = CountingSortAnimation(self.generated_array)
            counting.animate()
        elif select_method == "Порозрядне сортування":
            radix = RadixSortAnimation(self.generated_array)
            radix.animate()

    def clear_file(self):
        if self.file_name:
            try:
                open(self.file_name, 'w').close()
                msg = QMessageBox(self)
                self.update_color(msg, "Очищення файлу", "Файл успішно очищено: {}".format(self.file_name))
            except IOError:
                err = QMessageBox()
                self.update_color(err, "Помилка", "Помилка при очищенні файлу.")
    def save_array(self):
        self.file_name, _ = QFileDialog.getSaveFileName(self, "Save Array", "", "Text Files (*.txt)")
        if self.file_name:
            try:
                with open(self.file_name, 'w') as file:
                    file.write('Generated Array:')
                    for i, element in enumerate(self.generated_array):
                        if i == len(self.generated_array) - 1:
                            file.write(str(element))
                        else:
                            file.write(str(element) + ', ')
                    file.write('\n\n')
                    file.write("Sorted Array:")
                    for i, element in enumerate(self.sorted_array):
                        if i == len(self.sorted_array) - 1:
                            file.write(str(element))
                        else:
                            file.write(str(element) + ', ')
                msg = QMessageBox(self)
                self.update_color(msg, "Зберігання масиву", "Масив збережено в файлі: {}".format(self.file_name))
            except IOError:
                err = QMessageBox()
                self.update_color(err, "Помилка", "Помилка при збереженні масиву в файлі.")

    def draw_graph(self):
        if not self.generated_array:
            war_box = QMessageBox(self)
            self.update_color(war_box, "Array Not Generated", "Please generate an array first.")
            #QMessageBox.warning(self, "Array Not Generated", "Please generate an array first.")
            return

        # Получение выбранного метода сортировки из QComboBox
        selected_sorting_method = self.ui.ComboSort.currentText()

        # Применение выбранного метода сортировки
        if selected_sorting_method == "Блочне сортування":
            graph = BucketTime()
            arr, operations = graph.bucket_sort(self.generated_array)
            msg = QMessageBox(self)
            self.update_color(msg, "Кількість елементарних операцій", f"Кількість елементарних операцій: {operations}")
            graph.plot_complexity(self.generated_array)
        elif selected_sorting_method == "Сортування підрахунком":
            graph = CountingTime()
            arr, operations = graph.counting_sort(self.generated_array)
            msg = QMessageBox(self)
            self.update_color(msg, "Кількість елементарних операцій", f"Кількість елементарних операцій: {operations}")
            graph.plot_complexity(self.generated_array)
        elif selected_sorting_method == "Порозрядне сортування":
            graph = RadixTime()
            arr, operations = graph.radix_sort(self.generated_array)
            msg = QMessageBox(self)
            self.update_color(msg, "Кількість елементарних операцій", f"Кількість елементарних операцій: {operations}")
            graph.plot_complexity(self.generated_array)

    # def radix_graph(self):
    #     graph = RadixTime()
    #     graph.plot_complexity(self.generated_array)
    #
    # def bucket_graph(self):
    #     graph = BucketTime()
    #     graph.plot_complexity(self.generated_array)
    #
    # def counting_graph(self):
    #     graph = CountingTime()
    #     sizes = range(1, len(self.generated_array) + 1)
    #     graph.plot_complexity(sizes)

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

        # Розподілим елементи у масиві по блоках
        for num in array:
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
                bucket[j + 1] = key

            #sorted_array.extend(bucket)
            sorted_array += bucket

        return sorted_array

    def counting_sort(self, array):
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

        # Вычисляем накопленное количество
        for i in range(1, range_array + 1):
            count[i] += count[i - 1]

        # Восстанавливаем отсортированный массив
        i = size - 1
        while i >= 0:
            output[count[array[i] - min_value] - 1] = array[i]
            count[array[i] - min_value] -= 1
            i -= 1

        sorted_array = output

        return sorted_array

    def countingSort(self, array, place):
        size = len(array)
        output = [0] * size

        min_value = min(array)
        adjusted_array = [num - min_value for num in array]

        max_value = max(adjusted_array)

        count = [0] * (max_value + 1)

        # Calculate count of elements
        for i in range(0, size):
            index = adjusted_array[i] // place
            count[index % 10] += 1

        # Calculate cumulative count
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Place the elements in sorted order
        i = size - 1
        while i >= 0:
            index = adjusted_array[i] // place
            output[count[index % 10] - 1] = adjusted_array[i]
            count[index % 10] -= 1
            i -= 1

        # Adjust the sorted elements back to their original values
        sorted_array = [num + min_value for num in output]

        return sorted_array

    def radix_sort(self, array):
        # Get maximum and minimum elements
        max_element = max(array)
        min_element = min(array)

        # Create a new array to store the sorted elements
        sorted_array = array

        # Apply counting sort to sort elements based on place value.
        place = 1
        while (max_element - min_element) // place > 0:
            sorted_array = self.countingSort(sorted_array, place)
            place *= 10

        return sorted_array

