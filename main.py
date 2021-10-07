import time

from numpy.random import rand
from numpy.random import seed

from bubble_sorter import BubbleSorter
from insertion_sorter import InsertionSorter
from merge_sorter import MergeSorter

# NAME: VEYSEL YUSUF YILMAZ, NO: 190403062
# This is the Homework 1 of Introduction to Algorithms course.
# Several sorting algorithms are implemented and analyzed in Python.
# TODO: User Interface implementation.

# Arrays to store execution times.
insertion_timing_list = []
merge_timing_list = []
merge_insertion_timing_list = []
bubble_timing_list = []


# Function to compare and analyze algorithms
def sort_analyzer(sorter_object):
    # If array size is bigger than 10 thousand, we can not use Insertion and Bubble Sort anymore.
    if not ((sorter_object.get_algorithm_name == "Insertion" or sorter_object.get_algorithm_name == "Bubble Sort")
            and len(sorter_object.double_list) > 100000):
        start = time.time()
        sorter_object.sort()
        end = time.time()

        execution_time = str(end - start)

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

        print(sorter_object.get_algorithm_name + " sort execution time: " + execution_time)


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


# Main menu is opened.
# Repeat over and over until the repeat_main flag is false.
repeat_main = True
while repeat_main:

    operation = input("\nPlease select the operation you want to do:\n" +
                      "1-)Insertion Sort\n" +
                      "2-)Merge-Insertion Sort\n" +
                      "3-)Merge Sort\n" +
                      "4-)Bubble Sort\n" +
                      "5-)Comparison Test\n" +
                      "6-)Exit\n")

    # Initially check if user wants to quit.
    if operation == str(6):
        repeat_main = False

    elif operation == str(5):
        different_array_sizes = [10, 20, 30, 100, 1000, 10000]
        # 100000, 1000000, 10000000 are removed for now.

        for array_size in different_array_sizes:
            # We need to use exactly same array to compare different algorithms
            # If we create different random arrays, the execution time did not differ noticeably in this case ,
            # but still it would not be a full comparison.

            # We seed with the same value to all Sorter objects,
            # which means all generated random arrays will be same.
            seed(1)
            insertion_sorter = InsertionSorter(rand(array_size))
            merge_insertion_sorter = MergeSorter(rand(array_size), True)
            merge_sorter = MergeSorter(rand(array_size))
            bubble_sorter = BubbleSorter(rand(array_size))

            print("\n\nArray size: " + str(array_size) + "\n")
            sort_analyzer(insertion_sorter)
            sort_analyzer(merge_insertion_sorter)
            sort_analyzer(merge_sorter)
            sort_analyzer(bubble_sorter)

    else:
        if operation == str(1) or operation == str(2) or operation == str(3) or operation == str(4):
            print("\nPlease enter the value you want to sort:\n" +
                  "Press 'q' to sorting.")

            # Add numbers in list to sort.
            float_list = []

            controller = True
            while controller:
                input_string = check_input()
                if not input_string == "q":
                    float_input = float(input_string)
                    float_list.append(float_input)
                else:
                    controller = False

            if operation == str(1):
                sorter = InsertionSorter(float_list)
            elif operation == str(2):
                sorter = MergeSorter(float_list, True)
            elif operation == str(3):
                sorter = MergeSorter(float_list)
            else:
                sorter = BubbleSorter(float_list)

            sorter.sort()

            print(sorter.double_list)
