import time

from numpy.random import seed
from numpy.random import rand
from insertion_sorter import InsertionSorter
from merge_sorter import MergeSorter


def sort_analyzer(sorter_object):
    # If array size is bigger then 10 thousand, we can not use Insertion sort anymore.
    if not (sorter_object.get_algorithm_name == "Insertion" and len(sorter_object.array_list) > 100000):
        start = time.time()
        sorter_object.sort()
        end = time.time()

        print(sorter_object.get_algorithm_name + " sort execution time: " + str(end - start))


repeat_main = True
while repeat_main:

    operation = input("\nPlease select the operation you want to do:\n" +
                      "1-)Insertion Sort\n" +
                      "2-)Merge Sort\n" +
                      "4-)Comparison Test\n" +
                      "5-)Exit\n")

    # Initially check if user wants to quit.
    if operation == str(5):
        repeat_main = False

    elif operation == str(4):
        different_array_sizes = [10, 20, 30, 100, 1000, 10000, 100000, 1000000, 10000000]

        for array_size in different_array_sizes:
            # We need to use exactly same array to compare different algorithms
            # If we create different random arrays, the execution time did not differ noticeably in this case ,
            # but still it would not be a full comparison.

            # We seed with the same value to all arrays,
            # which means all generated random arrays will be same.
            seed(1)
            insertion_sorter = InsertionSorter(rand(array_size))
            merge_sorter = MergeSorter(rand(array_size))

            print("\n\nArray size: " + str(array_size) + "\n")
            sort_analyzer(insertion_sorter)
            sort_analyzer(merge_sorter)

    else:
        if operation == str(1) or operation == str(2) or operation == str(3):
            print("\nPlease enter the value you want to sort:\n" +
                  "Press 'q' to sorting.")

            # Add numbers in list to sort.
            float_list = []

            controller = True
            while controller:
                input_string = input()
                if not input_string == "q":
                    float_input = float(input_string)
                    float_list.append(float_input)
                else:
                    controller = False

            if operation == str(1):
                sorter = InsertionSorter(float_list)
            else:
                sorter = MergeSorter(float_list)

            sorter.sort()

            print(sorter.array_list)




