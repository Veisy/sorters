import matplotlib
import numpy

from numpy.random import randint

from algorithms.bubble_sorter import BubbleSorter
from algorithms.insertion_sorter import InsertionSorter
from algorithms.merge_sorter import MergeSorter
from algorithms.heap_sorter import HeapSorter
from algorithms.counting_sorter import CountingSorter
from algorithms.radix_sorter import RadixSorter
from algorithms.quick_sorter import QuickSorter

from src.utils.comparison import comparison_test

matplotlib.use('TkAgg')


# NAME: VEYSEL YUSUF YILMAZ, NO: 190403062
# This is a homework project of the Introduction to Algorithms course.
# Several sorting algorithms are implemented and analyzed in Python.
# TODO: User Interface implementation.


def main():
    # Main menu is opened.
    # Repeat over and over until the repeat_main flag is false.

    sorter = QuickSorter(True)

    random_array = randint(1, 100, 10)
    sorter.number_array = random_array.tolist()
    sorter.sort()
    for intermediate_array in sorter.intermediate_number_arrays:
        print(intermediate_array)
    print()
    print(numpy.sort(random_array))

    # comparison_test()


if __name__ == '__main__':
    main()
