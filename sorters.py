from abc import ABC, abstractmethod
from ctypes import *

import numpy as np
from numpy.ctypeslib import ndpointer

# Loading my c_sorters library functions.
c_sorters = CDLL('./c_sorters.so')
insertion_sort = c_sorters.insertion_sort
merge_insertion_sort = c_sorters.merge_insertion_sort
merge_sort = c_sorters.merge_sort


# Base abstract class of sorting algorithms.
# This class defines methods for child classes.
class BaseSorter(ABC):

    def __init__(self, float_array):
        # The list to be sorted.
        self.float_array = float_array

    @abstractmethod
    def get_algorithm_name(self):
        pass

    @abstractmethod
    def sort(self):
        pass


class InsertionSorter(BaseSorter):
    INSERTION_SORTER = "Insertion"

    def __init__(self, float_array):
        # Calls parent abstract class constructor (__init__ method).
        super().__init__(float_array)

    @property
    def get_algorithm_name(self):
        return InsertionSorter.INSERTION_SORTER

    def sort(self):
        array_length = len(self.float_array)
        # 1- Turn array in to numpy array
        # 2- Define return types of C function.
        # 3- Call C function by defining input types, and then return received value.
        self.float_array = np.array(self.float_array, dtype=c_float)
        insertion_sort.restype = ndpointer(dtype=c_float, shape=(array_length,))
        self.float_array = insertion_sort(c_void_p(self.float_array.ctypes.data), c_int(array_length))


class MergeSorter(BaseSorter):
    MERGE_SORT = "Merge"
    MERGE_INSERTION_SORT = "Merge-Insertion"

    def __init__(self, float_array, is_insertion_based=False):
        # Calls parent abstract class constructor (__init__ method).
        super().__init__(float_array)
        self.is_insertion_based = is_insertion_based

    @property
    def get_algorithm_name(self):
        if self.is_insertion_based:
            return MergeSorter.MERGE_INSERTION_SORT
        return MergeSorter.MERGE_SORT

    def sort(self):
        array_length = len(self.float_array)
        if self.is_insertion_based:
            # 1- Turn array in to numpy array
            # 2- Define return types of C function.
            # 3- Call C function by defining input types, and then return received value.
            self.float_array = np.array(self.float_array, dtype=c_float)
            merge_insertion_sort.restype = ndpointer(dtype=c_float, shape=(array_length,))
            self.float_array = merge_insertion_sort(c_void_p(self.float_array.ctypes.data), c_int(array_length))
        else:
            # The same here.
            self.float_array = np.array(self.float_array, dtype=c_float)
            merge_sort.restype = ndpointer(dtype=c_float, shape=(array_length,))
            self.float_array = merge_sort(c_void_p(self.float_array.ctypes.data), c_int(array_length))
