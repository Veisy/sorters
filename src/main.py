import sys
import time

import matplotlib
import numpy

from PyQt5.QtWidgets import QApplication
from numpy.random import randint, seed

from algorithms.bubble_sorter import BubbleSorter
from algorithms.insertion_sorter import InsertionSorter
from algorithms.merge_sorter import MergeSorter
from algorithms.heap_sorter import HeapSorter
from algorithms.counting_sorter import CountingSorter
from algorithms.radix_sorter import RadixSorter
from algorithms.quick_sorter import QuickSorter

from src.ui.main_sorting_window import MainSortingWindow

from src.utils.comparison import comparison_test

matplotlib.use('TkAgg')


# NAME: VEYSEL YUSUF YILMAZ, NO: 190403062
# This is a homework project of the Introduction to Algorithms course.
# Several sorting algorithms are implemented and analyzed in Python.
# TODO: User Interface implementation.

def main():
    # Main menu is opened.
    # Repeat over and over until the repeat_main flag is false.

    sorter = InsertionSorter(is_animating=True)
    seed(1)
    random_array = randint(1, 100, 20)
    sorter.number_array = random_array.tolist()
    sorter.sort()
    for intermediate_array in sorter.intermediate_number_arrays:
        print(intermediate_array)

    ui_main_window = MainSortingWindow()
    ui_main_window.show()
    canvas = set_canvas(ui_main_window)

    animate_sorting(canvas, sorter.intermediate_number_arrays)
    # comparison_test()


def set_canvas(ui_main_window):

    canvas = ui_main_window.mpl_sorting_widget.canvas
    canvas.axes.get_xaxis().set_visible(False)
    canvas.axes.get_yaxis().set_visible(False)

    return canvas


def animate_sorting(canvas, intermediate_number_arrays):
    for intermediate_array in intermediate_number_arrays:
        canvas.axes.clear()
        canvas.axes.bar(numpy.arange(len(intermediate_array)),
                        intermediate_array, color=['#ffbf00'])
        canvas.axes.patch.set_alpha(0)
        canvas.draw()
        time.sleep(0.001 * 500)
        QApplication.processEvents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main()
    app.exec_()
