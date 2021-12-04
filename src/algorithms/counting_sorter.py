from abc import ABC

from src.algorithms.sorter import Sorter


class CountingSorter(Sorter, ABC):
    COUNTING_SORT = "Counting Sort"

    @property
    def get_algorithm_name(self):
        return CountingSorter.COUNTING_SORT

    def sort(self):
        self.number_array = self.__counting_sort(self.number_array, self.intermediate_number_arrays, self.is_animating)

        # If NOT animating, we only need sorted array.
        if not self.is_animating:
            self.intermediate_number_arrays.append(self.number_array)

    @staticmethod
    def __counting_sort(number_array, intermediate_number_arrays, is_animating):
        # Initialize count array.
        counting_array_length = CountingSorter.__get_max_number(number_array) + 1
        count = [0] * counting_array_length

        # Store the count of each element in count array
        for number in number_array:
            integer_item = int(number)
            count[integer_item] += 1

        # Store the cumulative count
        for i in range(1, counting_array_length):
            count[i] += count[i - 1]

        # Find the index of each element of the original array in count array
        # place the elements in output array.
        size = len(number_array)
        output = [0] * size

        i = size - 1
        while i >= 0:
            integer_item = int(number_array[i])
            # Place the element at its position
            output[count[integer_item] - 1] = number_array[i]

            # If animating, collect intermediate arrays
            Sorter.collectIntermediateArrays(output, intermediate_number_arrays, is_animating)

            count[integer_item] -= 1
            i -= 1

        # Copy the sorted elements into original array
        for i in range(0, size):
            number_array[i] = output[i]

        return number_array

    @staticmethod
    def __get_max_number(number_array):
        max_number = 0
        for number in number_array:
            max_number = max(max_number, number)

        return int(max_number)
