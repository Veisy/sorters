from abc import ABC, abstractmethod


# Base abstract class of sorting algorithms.
# This class defines methods for child classes.
class Sorter(ABC):

    def __init__(self, is_animating=False):
        # The number array to be sorted.
        self.number_array = []
        self.execution_timings = []

        self.is_animating = is_animating
        # Memory of sorting where each step, or in other words each intermediate array is stored.
        self.intermediate_number_arrays = []

    @abstractmethod
    def get_algorithm_name(self):
        pass

    @abstractmethod
    def sort(self):
        pass

    # Used by Bubble, Insertion, Heap and Quick Sorts.
    def swap(self, first_element, second_element):
        if self.number_array[first_element] != self.number_array[second_element]:
            self.number_array[first_element], self.number_array[second_element] \
                = self.number_array[second_element], self.number_array[first_element]

        self.collectIntermediateArrays(self.number_array)

    # If animating, collect intermediate arrays
    def collectIntermediateArrays(self, intermediate_array):
        if self.is_animating:
            self.intermediate_number_arrays.append(intermediate_array.copy())
