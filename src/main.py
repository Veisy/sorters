import time

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randint
from numpy.random import seed

from algorithms.bubble_sorter import BubbleSorter
from algorithms.counter_sorter import CounterSorter
from algorithms.heap_sorter import HeapSorter
from algorithms.insertion_sorter import InsertionSorter
from algorithms.merge_sorter import MergeSorter
from algorithms.quick_sorter import QuickSorter
from algorithms.radix_sorter import RadixSorter

matplotlib.use('TkAgg')

# NAME: VEYSEL YUSUF YILMAZ, NO: 190403062
# This is the Homework 1 of Introduction to Algorithms course.
# Several sorting algorithms are implemented and analyzed in Python.
# TODO: User Interface implementation.

# Map operations to indexes for managing program flow.
# Since these constants are used in the whole program,
# it is better to declare and edit from one place in terms of bug risk and ease.
INSERTION_INDEX = "1"
MERGE_INSERTION_INDEX = "2"
MERGE_INDEX = "3"
BUBBLE_INDEX = "4"
QUICK_INDEX = "5"
HEAP_INDEX = "6"
COUNTER_INDEX = "7"
RADIX_INDEX = "8"
SORTER_INDEXES = [INSERTION_INDEX, MERGE_INSERTION_INDEX, MERGE_INDEX,
                  BUBBLE_INDEX, QUICK_INDEX, HEAP_INDEX, COUNTER_INDEX, RADIX_INDEX]
COMPARISON_INDEX = "9"
EXIT_INDEX = "0"


def main():
    # Main menu is opened.
    # Repeat over and over until the repeat_main flag is false.

    repeat_main = True
    while repeat_main:

        operation = input("\nPlease select the operation you want to do:\n" +
                          INSERTION_INDEX + "-)Insertion Sort\n" +
                          MERGE_INSERTION_INDEX + "-)Merge-Insertion Sort\n" +
                          MERGE_INDEX + "-)Merge Sort\n" +
                          BUBBLE_INDEX + "-)Bubble Sort\n" +
                          QUICK_INDEX + "-)Quick Sort\n" +
                          HEAP_INDEX + "-)Heap Sort\n" +
                          COUNTER_INDEX + "-)Counter Sort\n" +
                          RADIX_INDEX + "-)Radix Sort\n" +
                          COMPARISON_INDEX + "-)Comparison Test\n" +
                          EXIT_INDEX + "-)Exit\n")

        # Initially check if user wants to quit.
        if operation == EXIT_INDEX:
            repeat_main = False

        elif operation == COMPARISON_INDEX:
            comparison_test()

        elif operation in SORTER_INDEXES:
            manual_entrance(operation)

        else:
            print("Please enter a valid operation.")


def comparison_test():
    # Declare sorter objects.
    insertion_sorter = InsertionSorter()
    merge_insertion_sorter = MergeSorter(True)
    merge_sorter = MergeSorter()
    bubble_sorter = BubbleSorter()
    quick_sorter = QuickSorter()
    heap_sorter = HeapSorter()
    counter_sorter = CounterSorter()
    radix_sorter = RadixSorter()

    # All sorters objects stored in one array to simplify access and loop.
    sorters = [insertion_sorter, merge_insertion_sorter, merge_sorter,
               bubble_sorter, quick_sorter, heap_sorter, counter_sorter, radix_sorter]

    different_array_sizes_print = [10, 20, 40, 60, 80, 100, 200, 400, 600, 800, 1000]
    different_array_sizes_small = np.arange(2, 100, 1)
    different_array_sizes_medium = np.arange(100, 1050, 50)

    different_array_sizes = np.concatenate([different_array_sizes_small, different_array_sizes_medium])
    # different_array_sizes = different_array_sizes_small

    for array_size in different_array_sizes:
        # We need to use exactly same array to compare different algorithms
        # If we create different random arrays, the execution time did not differ noticeably in this case ,
        # but still it would not be a full comparison.
        # We seed with the same value to all Sorter objects,
        # which means all generated random arrays will be same.
        seed(1)

        # Print the analyze result if the array_size one of the different_array_sizes_print elements.
        will_be_printed = False

        if array_size in different_array_sizes_print:
            print("\n\nArray size: " + str(array_size) + "\n")
            will_be_printed = True

        # Analyze algorithms.
        for sorter in sorters:
            sorter.number_array = randint(1, array_size, array_size)
            sort_analyzer(sorter, will_be_printed)

    # Plot execution times versus array sizes
    for sorter in sorters:
        plt.plot(different_array_sizes, sorter.execution_timings, label=sorter.get_algorithm_name)

    plt.xlabel('Array sizes')
    plt.ylabel('Execution timings')
    plt.title('Sorter Algorithms Comparison')
    plt.legend()
    # show graph
    plt.show()


def manual_entrance(operation):
    print("\nPlease enter the value you want to sort:\n" +
          "Press 'q' to sorting.")

    # Add numbers in list to sort.
    number_array = []

    # Check if the 'q' key is pressed and receiving inputs is done.
    controller = True
    while controller:
        input_string = check_input()
        if not input_string == "q":
            number_input = float(input_string)
            number_array.append(number_input)
        else:
            controller = False

    if operation == INSERTION_INDEX:
        sorter = InsertionSorter()
    elif operation == MERGE_INSERTION_INDEX:
        sorter = MergeSorter(True)
    elif operation == MERGE_INDEX:
        sorter = MergeSorter()
    elif operation == BUBBLE_INDEX:
        sorter = BubbleSorter()
    elif operation == QUICK_INDEX:
        sorter = QuickSorter()
    elif operation == HEAP_INDEX:
        sorter = HeapSorter()
    elif operation == COUNTER_INDEX:
        sorter = CounterSorter()
    else:
        sorter = RadixSorter()

    sorter.number_array = number_array
    sorter.sort()

    print(sorter.number_array)


# Function to compare and analyze algorithms
def sort_analyzer(sorter_object, is_printed):
    # If array size is bigger than 10 thousand, we can not use Insertion and Bubble Sort anymore.
    if not (((sorter_object.get_algorithm_name == InsertionSorter.INSERTION_SORT
              or sorter_object.get_algorithm_name == BubbleSorter.BUBBLE_SORT)
             and len(sorter_object.number_array) > 100000)
            or (sorter_object.get_algorithm_name == MergeSorter.MERGE_INSERTION_SORT
                and len(sorter_object.number_array) > 200000)):

        start = time.time()
        sorter_object.sort()
        end = time.time()

        execution_time = end - start

        # Store execution times, by appending to overall timings pool.
        sorter_object.execution_timings.append(execution_time)

        if is_printed:
            print(sorter_object.get_algorithm_name + " execution time: " + str(execution_time))


# Function to check keyboard input.
def check_input():
    keyboard_input = input()
    while True:
        try:
            if keyboard_input == "q":
                break
            float(keyboard_input)
            break
        except ValueError:
            print("Please enter a valid number.")
            keyboard_input = input()

    return keyboard_input


if __name__ == '__main__':
    main()
