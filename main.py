import time

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randint
from numpy.random import seed

from bubble_sorter import BubbleSorter
from heap_sorter import HeapSorter
from insertion_sorter import InsertionSorter
from merge_sorter import MergeSorter
from quick_sorter import QuickSorter

matplotlib.use('TkAgg')

# NAME: VEYSEL YUSUF YILMAZ, NO: 190403062
# This is the Homework 1 of Introduction to Algorithms course.
# Several sorting algorithms are implemented and analyzed in Python.
# TODO: User Interface implementation.

# Arrays to store execution times.
insertion_timing_list = []
merge_timing_list = []
merge_insertion_timing_list = []
bubble_timing_list = []
quick_timing_list = []
heap_timing_list = []


def main():
    # Main menu is opened.
    # Repeat over and over until the repeat_main flag is false.
    repeat_main = True
    while repeat_main:

        operation = input("\nPlease select the operation you want to do:\n" +
                          "1-)Insertion Sort\n" +
                          "2-)Merge-Insertion Sort\n" +
                          "3-)Merge Sort\n" +
                          "4-)Bubble Sort\n" +
                          "5-)Quick Sort\n" +
                          "6-)Heap Sort\n" +
                          "7-)Comparison Test\n" +
                          "8-)Exit\n")

        # Initially check if user wants to quit.
        if operation == str(8):
            repeat_main = False

        elif operation == str(7):
            different_array_sizes_print = [10, 20, 40, 60, 80, 100, 200, 400, 600, 800, 1000]
            different_array_sizes_small = np.arange(2, 100, 1)
            different_array_sizes_medium = np.arange(100, 1050, 50)

            different_array_sizes = np.concatenate([different_array_sizes_small, different_array_sizes_medium])
            # different_array_sizes = different_array_sizes_small

            insertion_timing_list.clear()
            merge_insertion_timing_list.clear()
            merge_timing_list.clear()
            bubble_timing_list.clear()
            quick_timing_list.clear()

            for array_size in different_array_sizes:
                # We need to use exactly same array to compare different algorithms
                # If we create different random arrays, the execution time did not differ noticeably in this case ,
                # but still it would not be a full comparison.
                # We seed with the same value to all Sorter objects,
                # which means all generated random arrays will be same.
                seed(1)

                insertion_sorter = InsertionSorter(randint(1, array_size, array_size))
                merge_insertion_sorter = MergeSorter(randint(1, array_size, array_size), True)
                merge_sorter = MergeSorter(randint(1, array_size, array_size))
                bubble_sorter = BubbleSorter(randint(1, array_size, array_size))
                quick_sorter = QuickSorter(randint(1, array_size, array_size))
                heap_sorter = HeapSorter(randint(1, array_size, array_size))

                # Print the analyze result if the array_size one of the different_array_sizes_print elements.
                will_be_printed = False

                if array_size in different_array_sizes_print:
                    print("\n\nArray size: " + str(array_size) + "\n")
                    will_be_printed = True

                # Analyze algorithms.
                sort_analyzer(insertion_sorter, will_be_printed)
                sort_analyzer(merge_insertion_sorter, will_be_printed)
                sort_analyzer(merge_sorter, will_be_printed)
                sort_analyzer(bubble_sorter, will_be_printed)
                sort_analyzer(quick_sorter, will_be_printed)
                sort_analyzer(heap_sorter, will_be_printed)

            # Plot execution times versus array sizes
            plt.plot(different_array_sizes, bubble_timing_list, label="Bubble Sort")
            plt.plot(different_array_sizes, insertion_timing_list, label="Insertion Sort")
            plt.plot(different_array_sizes, merge_insertion_timing_list, label="Merge-Insertion Sort")
            plt.plot(different_array_sizes, merge_timing_list, label="Merge Sort")
            plt.plot(different_array_sizes, quick_timing_list, label="Quick Sort")
            plt.plot(different_array_sizes, heap_timing_list, label="Heap Sort")

            plt.xlabel('Array sizes')
            plt.ylabel('Execution timings')
            plt.title('Sorter Algorithms Comparison')
            plt.legend()
            # show graph
            plt.show()

        else:
            if operation == str(1) or operation == str(2) or operation == str(3) \
                    or operation == str(4) or operation == str(5) or operation == str(6):
                print("\nPlease enter the value you want to sort:\n" +
                      "Press 'q' to sorting.")

                # Add numbers in list to sort.
                float_array = []

                # Check if the 'q' key is pressed and receiving inputs is done.
                controller = True
                while controller:
                    input_string = check_input()
                    if not input_string == "q":
                        float_input = float(input_string)
                        float_array.append(float_input)
                    else:
                        controller = False

                if operation == str(1):
                    sorter = InsertionSorter(float_array)
                elif operation == str(2):
                    sorter = MergeSorter(float_array, True)
                elif operation == str(3):
                    sorter = MergeSorter(float_array)
                elif operation == str(4):
                    sorter = BubbleSorter(float_array)
                elif operation == str(5):
                    sorter = QuickSorter(float_array)
                else:
                    sorter = HeapSorter(float_array)

                sorter.sort()

                print(sorter.float_array)


# Function to compare and analyze algorithms
def sort_analyzer(sorter_object, is_printed):
    # If array size is bigger than 10 thousand, we can not use Insertion and Bubble Sort anymore.
    if not (((sorter_object.get_algorithm_name == InsertionSorter.INSERTION_SORTER
              or sorter_object.get_algorithm_name == BubbleSorter.BUBBLE_SORT)
             and len(sorter_object.float_array) > 100000)
            or (sorter_object.get_algorithm_name == MergeSorter.MERGE_INSERTION_SORT
                and len(sorter_object.float_array) > 200000)):

        start = time.time()
        sorter_object.sort()
        end = time.time()

        execution_time = end - start

        # Store execution times.
        algorithm_name = sorter_object.get_algorithm_name
        if algorithm_name == InsertionSorter.INSERTION_SORTER:
            insertion_timing_list.append(execution_time)
        elif algorithm_name == MergeSorter.MERGE_INSERTION_SORT:
            merge_insertion_timing_list.append(execution_time)
        elif algorithm_name == MergeSorter.MERGE_SORT:
            merge_timing_list.append(execution_time)
        elif algorithm_name == BubbleSorter.BUBBLE_SORT:
            bubble_timing_list.append(execution_time)
        elif algorithm_name == QuickSorter.QUICK_SORT:
            quick_timing_list.append(execution_time)
        elif algorithm_name == HeapSorter.HEAP_SORT:
            heap_timing_list.append(execution_time)

        if is_printed:
            print(sorter_object.get_algorithm_name + " sort execution time: " + str(execution_time))


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