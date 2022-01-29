import random
import sys
import time

import matplotlib
import numpy
from PyQt5.QtWidgets import QApplication

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
from src.utils.random_array_generator import generate_random_array
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

random_default_size = 15
random_default_min = 1
random_default_max = 50

fibonacci_default_size = 10
fibonacci_max = 20


def main():
    # Main menu is opened.
    # Repeat over and over until the repeat_main flag is false.
    main_window.show()
    set_canvas()
    connect_buttons()
    set_placeholder_values()


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


def set_placeholder_values():
    main_window.lineEdit_array_size.setPlaceholderText(str(random_default_size))
    main_window.lineEdit_max_value.setPlaceholderText(str(random_default_max))
    main_window.lineEdit_min_value.setPlaceholderText(str(random_default_min))
    main_window.lineEdit_fibonacci.setPlaceholderText(str(fibonacci_default_size))


def create_random_array():
    text_size = main_window.lineEdit_array_size.text()
    seed_value = main_window.spinBox_seed.value()
    text_min_value = main_window.lineEdit_min_value.text()
    text_max_value = main_window.lineEdit_max_value.text()
    is_seed_active = main_window.checkBox_seed.isChecked()

    input_array.clear()
    random_array = generate_random_array(text_size=text_size, text_min_value=text_min_value,
                                         text_max_value=text_max_value, default_size=random_default_size,
                                         default_min=random_default_min, default_max=random_default_max,
                                         is_seed_active=is_seed_active,
                                         seed_value=seed_value)
    input_array.extend(random_array)
    draw(random_array)
    print(str(input_array))


# TODO:
# def add_manual_element():
#     if main_window.line


def create_fibonacci_array():
    text_fibonacci_size = main_window.lineEdit_fibonacci.text()

    if text_fibonacci_size != '' and fibonacci_max > int(text_fibonacci_size) > 1:
        fibonacci_size = int(text_fibonacci_size)
    else:
        fibonacci_size = fibonacci_default_size

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
    # If an array is empty, or array is already sorted, return without doing anything.
    if len(input_array) <= 0 or is_sorted(input_array):
        return

    selected_algorithm = sorting_algorithms.currentText()
    if selected_algorithm == InsertionSorter.INSERTION_SORT:
        sorter = InsertionSorter(is_animating=True)
    elif selected_algorithm == MergeSorter.MERGE_INSERTION_SORT:
        sorter = MergeSorter(is_insertion_based=True, is_animating=True)
    elif selected_algorithm == MergeSorter.MERGE_SORT:
        sorter = MergeSorter(is_animating=True)
    elif selected_algorithm == HeapSorter.HEAP_SORT:
        sorter = HeapSorter(is_animating=True)
    elif selected_algorithm == QuickSorter.QUICK_SORT:
        sorter = QuickSorter(is_animating=True)
    elif selected_algorithm == RadixSorter.RADIX_SORT and min(input_array) >= 0:
        sorter = RadixSorter(is_animating=True)
    elif selected_algorithm == CountingSorter.COUNTING_SORT and min(input_array) >= 0:
        sorter = CountingSorter(is_animating=True)
    else:
        sorter = BubbleSorter(is_animating=True)

    print(sorter.get_algorithm_name + " Clicked!")
    sort(sorter)


def sort(sorter):
    global list_of_intermediate_number_arrays
    global current_index
    current_index = 0

    toggle_views_visibility(is_visible=False)

    sorter.number_array = input_array.copy()
    sorter.sort()

    # Retrieve all intermediate steps in the sorting process. That is, the memory of the sorting process.
    list_of_intermediate_number_arrays = sorter.intermediate_number_arrays
    animate_sorting()


def animate_sorting():
    global list_of_intermediate_number_arrays
    global is_animation_active
    global current_index

    is_animation_active = True

    while len(list_of_intermediate_number_arrays) > current_index:
        # We exit here in Pause and Stop cases.
        # In the Pause case, we know where we are with the current_index variable.
        if not is_animation_active:
            break
        # 'Is this the last step?' control.
        if current_index == len(list_of_intermediate_number_arrays) - 1:
            draw(list_of_intermediate_number_arrays[current_index],
                 all_bars_color=str(main_window.color_positive_background_hover))
            toggle_views_visibility(True)
        else:
            if current_index > 0:
                compared_array = list_of_intermediate_number_arrays[current_index - 1]
            else:
                compared_array = input_array

            paint_different_elements(compared_array, list_of_intermediate_number_arrays[current_index])

        current_index += 1

        time.sleep(1 / main_window.dial_animation_speed.value())
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
        searched_element = main_window.lineEdit_search.text()

        if searched_element != '':
            index = linear_search(input_array.copy(), int(searched_element))
            draw(input_array, highlight=True, highlighted_bar_indexes=[index])


def pause_animation():
    global is_animation_active
    global current_index
    if is_animation_active:
        current_index -= 1
    is_animation_active = False


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

    if current_index > 0:
        paint_different_elements(list_of_intermediate_number_arrays[current_index],
                                 list_of_intermediate_number_arrays[current_index - 1])
    else:
        stop_animation()


def toggle_views_visibility(is_visible):
    array_independent_views = [main_window.pushButton_start_sorting, main_window.pushButton_compare,
                               main_window.comboBox_sorting_algorithms,
                               main_window.pushButton_create_array, main_window.pushButton_manuel_array,
                               main_window.pushButton_clear, main_window.lineEdit_array_size,
                               main_window.lineEdit_max_value, main_window.lineEdit_min_value,
                               main_window.label_array_size, main_window.label_max_value,
                               main_window.label_min_value, main_window.lineEdit_search, main_window.pushButton_search,
                               main_window.checkBox_seed, main_window.spinBox_seed,
                               main_window.lineEdit_fibonacci, main_window.pushButton_fibonacci,
                               main_window.frame_line, main_window.frame_line_2, main_window.frame_line_3,
                               main_window.frame_line_4, main_window.frame_line_5]
    for view in array_independent_views:
        if is_visible:
            view.setVisible(True)
            view.raise_()
        else:
            view.setVisible(False)
            view.lower()

    pause_stop_resume_back_buttons = [main_window.pushButton_pause, main_window.pushButton_resume,
                                      main_window.pushButton_stop, main_window.pushButton_back,
                                      main_window.label_speed, main_window.dial_animation_speed]
    for view in pause_stop_resume_back_buttons:
        if is_visible:
            view.setVisible(False)
            view.lower()
        else:
            view.setVisible(True)
            view.raise_()

    main_window.update()


def paint_different_elements(first_array, second_array):
    different_element_indexes = []
    if len(first_array) == len(second_array):
        for index in range(len(first_array)):
            if first_array[index] != second_array[index]:
                different_element_indexes.append(index)
    draw(second_array, highlight=True, highlighted_bar_indexes=different_element_indexes)


def set_seed_visibility():
    main_window.spinBox_seed.setVisible(main_window.checkBox_seed.isChecked())
    main_window.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainSortingWindow()
    main()

    sys.exit(app.exec_())
