import random
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
from src.utils.fibonacci_generator import generate_fibonacci
from src.utils.is_sorted import is_sorted
from src.utils.searchers import linear_search

matplotlib.use('TkAgg')

# NAME: VEYSEL YUSUF YILMAZ, NO: 190403062
# This is a homework project of the Introduction to Algorithms course.
# Several sorting algorithms are implemented and analyzed in Python.
# TODO: User Interface implementation.

input_array = []
list_of_intermediate_number_arrays = [[]]
current_index = 0
is_animation_active = False


def main():
    # Main menu is opened.
    # Repeat over and over until the repeat_main flag is false.
    main_window.show()
    set_canvas()
    connect_buttons()


def set_canvas():
    canvas = main_window.mpl_sorting_widget.canvas
    canvas.axes.get_xaxis().set_visible(False)
    canvas.axes.get_yaxis().set_visible(False)
    return canvas


def connect_buttons():
    main_window.pushButton_start_sorting.clicked.connect(lambda: clicked_sort(main_window.comboBox_sorting_algorithms))
    main_window.pushButton_create_array.clicked.connect(create_random_array)
    # main_window.pushButton_manuel_array.clicked.connect(add_manual_element)
    main_window.pushButton_fibonacci.clicked.connect(create_fibonacci_array)
    main_window.pushButton_clear.clicked.connect(clear_input_array)
    main_window.checkBox_seed.stateChanged.connect(set_seed_visibility)
    main_window.pushButton_compare.clicked.connect(compare_algorithms)
    main_window.pushButton_search.clicked.connect(search)
    main_window.pushButton_pause.clicked.connect(pause_animation)
    main_window.pushButton_resume.clicked.connect(resume_animation)
    main_window.pushButton_stop.clicked.connect(stop_animation)
    main_window.pushButton_back.clicked.connect(back)


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
    elif text_max_value != '' and int(text_max_value) > 1:
        min_value = 1
        max_value = int(text_max_value)
    elif text_min_value != '':
        min_value = int(text_min_value)
        max_value = 50 + int(text_min_value)
    else:
        min_value = 1
        max_value = 50

    input_array.clear()
    random_array = randint(min_value, max_value, size).tolist()
    input_array.extend(random_array)
    draw(random_array)
    print(str(input_array))


# def add_manual_element():
#     if main_window.line


def create_fibonacci_array():
    text_fibonacci_size = main_window.lineEdit_fibonacci.text()

    if text_fibonacci_size != '' and 20 > int(text_fibonacci_size) > 1:
        fibonacci_size = int(text_fibonacci_size)
    else:
        fibonacci_size = 15
    fibonacci_sequence = generate_fibonacci(fibonacci_size)
    input_array.clear()
    input_array.extend(fibonacci_sequence)
    random.shuffle(input_array)
    draw(input_array)


def clear_input_array():
    global list_of_intermediate_number_arrays
    global is_animation_active
    global current_index
    is_animation_active = False
    current_index = 0
    list_of_intermediate_number_arrays.clear()

    input_array.clear()
    draw(input_array)


def clicked_sort(sorting_algorithms):
    # If an array is empty, return without doing anything.
    if len(input_array) <= 0 or is_sorted(input_array):
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
    global list_of_intermediate_number_arrays
    global current_index
    current_index = 0

    toggle_views_visibility(False)

    sorter.number_array = input_array.copy()
    sorter.sort()

    list_of_intermediate_number_arrays = sorter.intermediate_number_arrays
    animate_sorting()


def animate_sorting():
    global list_of_intermediate_number_arrays
    global is_animation_active
    global current_index

    is_animation_active = True
    print_intermediate_arrays()

    for _ in range(len(list_of_intermediate_number_arrays) - current_index):
        if not is_animation_active:
            break

        if current_index == len(list_of_intermediate_number_arrays) - 1:
            default_bar_color = str(main_window.color_positive_background_hover)
            toggle_views_visibility(True)
        else:
            default_bar_color = str(main_window.color_neutral_background)

        if current_index > 0:
            paint_different_elements(list_of_intermediate_number_arrays[current_index - 1],
                                     list_of_intermediate_number_arrays[current_index])
        else:
            draw(list_of_intermediate_number_arrays[current_index], default_bar_color)

        current_index += 1

        time.sleep(0.001 * (100 - main_window.dial_animation_speed.value()))
        QApplication.processEvents()

    is_animation_active = False
    set_seed_visibility()


def draw(array, all_bars_color='#3949ab', highlighted_bar_indexes=None, highlight=False):
    canvas = set_canvas()
    canvas.axes.clear()
    canvas.axes.bar(numpy.arange(len(array)),
                    array, color=[all_bars_color])
    if highlight and len(highlighted_bar_indexes) > 0:
        for index in highlighted_bar_indexes:
            canvas.axes.bar(numpy.arange(len(array))[index],
                            array[index], color=main_window.color_complementary)

    canvas.axes.patch.set_alpha(0)
    canvas.draw()


def compare_algorithms():
    canvas = main_window.mpl_sorting_widget.canvas
    canvas.axes.clear()
    comparison_test(canvas)


def search():
    global input_array

    if len(input_array) > 0:
        element = main_window.lineEdit_search.text()

        if element != '':
            index = linear_search(input_array.copy(), int(element))
            draw(input_array.copy(), highlight=True, highlighted_bar_indexes=[index])


def pause_animation():
    global is_animation_active
    global current_index
    is_animation_active = False
    current_index -= 1


def resume_animation():
    animate_sorting()


def stop_animation():
    global input_array
    global current_index
    global is_animation_active
    is_animation_active = False
    toggle_views_visibility(True)
    current_index = 0
    draw(input_array)


def back():
    global list_of_intermediate_number_arrays
    global current_index
    global is_animation_active
    if is_animation_active:
        pause_animation()
    current_index -= 1
    if current_index < 0:
        stop_animation()

    if current_index > 1:
        paint_different_elements(list_of_intermediate_number_arrays[current_index],
                                 list_of_intermediate_number_arrays[current_index - 1])


def toggle_views_visibility(is_visible):
    array_independent_views = [main_window.pushButton_start_sorting, main_window.pushButton_compare,
                               main_window.comboBox_sorting_algorithms, main_window.menuBar,
                               main_window.pushButton_create_array, main_window.pushButton_manuel_array,
                               main_window.pushButton_clear, main_window.lineEdit_array_size,
                               main_window.lineEdit_max_value, main_window.lineEdit_min_value,
                               main_window.label_array_size, main_window.label_max_value,
                               main_window.label_min_value, main_window.lineEdit_search, main_window.pushButton_search,
                               main_window.checkBox_seed, main_window.spinBox_seed]
    for view in array_independent_views:
        if is_visible:
            view.setVisible(True)
        else:
            view.setVisible(False)

    pause_stop_resume_back_buttons = [main_window.pushButton_pause, main_window.pushButton_resume,
                                      main_window.pushButton_stop, main_window.pushButton_back,
                                      main_window.label_speed, main_window.dial_animation_speed]
    for view in pause_stop_resume_back_buttons:
        if is_visible:
            view.setVisible(False)
        else:
            view.setVisible(True)


def paint_different_elements(first_array, second_array):
    different_element_indexes = []
    if len(first_array) == len(second_array):
        for index in range(len(first_array)):
            if first_array[index] != second_array[index]:
                different_element_indexes.append(index)
    draw(second_array, highlight=True, highlighted_bar_indexes=different_element_indexes)


def set_seed_visibility():
    main_window.spinBox_seed.setVisible(main_window.checkBox_seed.isChecked())


def print_intermediate_arrays():
    global list_of_intermediate_number_arrays
    for element in list_of_intermediate_number_arrays:
        print(element)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainSortingWindow()
    main()

    sys.exit(app.exec_())
