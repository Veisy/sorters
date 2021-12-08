import time
import matplotlib.pyplot as plt
import numpy as np

from numpy.random import randint
from numpy.random import seed
from src.algorithms.bubble_sorter import BubbleSorter
from src.algorithms.counting_sorter import CountingSorter
from src.algorithms.heap_sorter import HeapSorter
from src.algorithms.insertion_sorter import InsertionSorter
from src.algorithms.merge_sorter import MergeSorter
from src.algorithms.quick_sorter import QuickSorter
from src.algorithms.radix_sorter import RadixSorter


def comparison_test(canvas):
    # Declare sorter objects.
    insertion_sorter = InsertionSorter()
    merge_insertion_sorter = MergeSorter(is_insertion_based=True)
    merge_sorter = MergeSorter()
    bubble_sorter = BubbleSorter()
    quick_sorter = QuickSorter()
    heap_sorter = HeapSorter()
    counter_sorter = CountingSorter()
    radix_sorter = RadixSorter()

    # All sorters objects stored in one array to simplify access and loop.
    sorters = [insertion_sorter, merge_insertion_sorter, merge_sorter,
               bubble_sorter, quick_sorter, heap_sorter, counter_sorter, radix_sorter]

    different_array_sizes_print = [10, 20, 40, 60, 80, 100, 200, 300, 400, 500]
    different_array_sizes_small = np.arange(2, 100, 1)
    different_array_sizes_medium = np.arange(100, 550, 50)

    different_array_sizes = np.concatenate([different_array_sizes_small, different_array_sizes_medium])
    # different_array_sizes = different_array_sizes_small

    for array_size in different_array_sizes:
        # We need to use exactly same array to compare different algorithms
        # If we create different random arrays, the execution time did not differ noticeably in this case ,
        # but still it would not be a full comparison.
        # We seed with the same value to all Sorter objects,
        # which means all generated random arrays will be same.
        seed(1)

        # Print the analysis result if the array_size one of the different_array_sizes_print elements.
        will_be_printed = False

        if array_size in different_array_sizes_print:
            print("\n\nArray size: " + str(array_size) + "\n")
            will_be_printed = True

        # Analyze algorithms.
        for sorter in sorters:
            sorter.number_array = randint(1, array_size, array_size)
            __sort_analyzer(sorter, will_be_printed)

    # Plot execution times versus array sizes
    canvas.axes.get_xaxis().set_visible(True)
    canvas.axes.get_yaxis().set_visible(True)
    for sorter in sorters:
        canvas.axes.plot(different_array_sizes, sorter.execution_timings, label=sorter.get_algorithm_name)

    canvas.axes.legend()
    # show graph
    canvas.draw()


# Function to compare and analyze algorithms
def __sort_analyzer(sorter_object, is_printed):
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
