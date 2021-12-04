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
    @staticmethod
    def swap(number_array, first_element, second_element, intermediate_number_arrays, is_animating):
        if number_array[first_element] != number_array[second_element]:
            number_array[first_element], number_array[second_element] \
                = number_array[second_element], number_array[first_element]

        Sorter.collectIntermediateArrays(number_array, intermediate_number_arrays, is_animating)

    # If animating, collect intermediate arrays
    @staticmethod
    def collectIntermediateArrays(number_array, intermediate_number_arrays, is_animating):
        if is_animating:
            intermediate_number_arrays.append(number_array.copy())
