import sys
import time

import matplotlib
import numpy
from PyQt5.QtWidgets import QApplication
from numpy.random import randint, seed

from algorithms.bubble_sorter import BubbleSorter
from algorithms.counting_sorter import CountingSorter
from algorithms.heap_sorter import HeapSorter
from algorithms.insertion_sorter import InsertionSorter
from algorithms.merge_sorter import MergeSorter
from algorithms.quick_sorter import QuickSorter
from algorithms.radix_sorter import RadixSorter
from src.ui.main_sorting_window import MainSortingWindow
from src.utils.comparison import comparison_test

matplotlib.use('TkAgg')

# NAME: VEYSEL YUSUF YILMAZ, NO: 190403062
# This is a homework project of the Introduction to Algorithms course.
# Several sorting algorithms are implemented and analyzed in Python.
# TODO: User Interface implementation.

input_array = []


def main():
    # Main menu is opened.
    # Repeat over and over until the repeat_main flag is false.
    set_canvas()
    connect_buttons()

    # animate_sorting(canvas, sorter.intermediate_number_arrays)
    # comparison_test()


def set_canvas():
    canvas = main_window.mpl_sorting_widget.canvas
    canvas.axes.get_xaxis().set_visible(False)
    canvas.axes.get_yaxis().set_visible(False)


def connect_buttons():
    main_window.pushButton_start_sorting.clicked.connect(lambda: clicked_sort(main_window.comboBox_sorting_algorithms))
    main_window.pushButton_create_array.clicked.connect(create_random_array)
    main_window.pushButton_clear.clicked.connect(clear_input_array)


# Create random array with default parameters.
def create_random_array():
    text_size = main_window.lineEdit_array_size.text()
    seed_value = main_window.spinBox_seed.value()
    text_min_value = main_window.lineEdit_min_value.text()
    text_max_value = main_window.lineEdit_max_value.text()
    is_seed_active = main_window.checkBox_seed.isChecked()

    # Default size is 20.
    if text_size != '' and int(text_size) > 0:
        size = int(text_size)
    else:
        size = 20

    if is_seed_active:
        seed(seed_value)

    # Default min value is 1, and max value is 10.
    if text_min_value != '' and text_max_value != '' and int(text_max_value) > int(text_min_value):
        min_value = int(text_min_value)
        max_value = int(text_max_value)
    else:
        min_value = 1
        max_value = 10

    input_array.clear()
    random_array = randint(min_value, max_value, size).tolist()
    input_array.extend(random_array)
    draw(random_array)
    print(str(input_array))


def clear_input_array():
    input_array.clear()
    draw(input_array)


def clicked_sort(sorting_algorithms):
    # If an array is empty, return without doing anything.
    if len(input_array) <= 0:
        return

    selected_algorithm = sorting_algorithms.currentText()
    if selected_algorithm == InsertionSorter.INSERTION_SORT:
        sorter = InsertionSorter(True)
    elif selected_algorithm == MergeSorter.MERGE_INSERTION_SORT:
        sorter = MergeSorter(is_insertion_based=True, is_animating=True)
    elif selected_algorithm == MergeSorter.MERGE_SORT:
        sorter = MergeSorter(is_animating=True)
    elif selected_algorithm == HeapSorter.HEAP_SORT:
        sorter = HeapSorter(True)
    elif selected_algorithm == QuickSorter.QUICK_SORT:
        sorter = QuickSorter(True)
    elif selected_algorithm == RadixSorter.RADIX_SORT and min(input_array) >= 0:
        sorter = RadixSorter(True)
    elif selected_algorithm == CountingSorter.COUNTING_SORT and min(input_array) >= 0:
        sorter = CountingSorter(True)
    else:
        sorter = BubbleSorter(True)

    print(sorter.get_algorithm_name + " Clicked!")
    sort(sorter)


def sort(sorter):
    sorter.number_array = input_array.copy()
    sorter.sort()
    animate_sorting(sorter.intermediate_number_arrays)


def animate_sorting(intermediate_number_arrays):
    print_intermediate_arrays(intermediate_number_arrays)

    for intermediate_array in intermediate_number_arrays:
        draw(intermediate_array)
        time.sleep(0.001 * (100 - main_window.dial_animation_speed.value()))
        QApplication.processEvents()


def draw(array):
    canvas = main_window.mpl_sorting_widget.canvas
    canvas.axes.clear()
    canvas.axes.bar(numpy.arange(len(array)),
                    array, color=['#ffbf00'])
    canvas.axes.patch.set_alpha(0)
    canvas.draw()


def print_intermediate_arrays(intermediate_number_arrays):
    for element in intermediate_number_arrays:
        print(element)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainSortingWindow()
    main_window.show()

    main()

    sys.exit(app.exec_())
