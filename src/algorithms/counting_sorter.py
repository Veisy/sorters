from abc import ABC

from src.algorithms.sorter import Sorter


class CountingSorter(Sorter, ABC):
    COUNTING_SORT = "Counting Sort"

    @property
    def get_algorithm_name(self):
        return CountingSorter.COUNTING_SORT

    def sort(self):
        self.__counting_sort()

        # If NOT animating, we only need sorted array.
        if not self.is_animating:
            self.intermediate_number_arrays.append(self.number_array)

    def __counting_sort(self):
        # Initialize count array.
        counting_array_length = self.__get_max_number() + 1
        count = [0] * counting_array_length

        # Store the count of each element in count array
        for number in self.number_array:
            integer_item = int(number)
            count[integer_item] += 1

        # Store the cumulative count
        for i in range(1, counting_array_length):
            count[i] += count[i - 1]

        # Find the index of each element of the original array in count array
        # place the elements in output array.
        size = len(self.number_array)
        output = [0] * size

        i = size - 1
        while i >= 0:
            integer_item = int(self.number_array[i])
            # Place the element at its position
            output[count[integer_item] - 1] = self.number_array[i]

            # If animating, collect intermediate arrays
            self.collectIntermediateArrays(output)

            count[integer_item] -= 1
            i -= 1

        # Copy the sorted elements into original array
        for i in range(0, size):
            self.number_array[i] = output[i]

    def __get_max_number(self):
        max_number = 0
        for number in self.number_array:
            max_number = max(max_number, number)

        return int(max_number)
