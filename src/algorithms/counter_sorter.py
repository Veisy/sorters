from abc import ABC

from src.algorithms.sorter import BaseSorter


class CounterSorter(BaseSorter, ABC):
    COUNTER_SORT = "Counter Sort"

    @property
    def get_algorithm_name(self):
        return CounterSorter.COUNTER_SORT

    def sort(self):
        self.number_array = CounterSorter.__counter_sort(self.number_array)

    @staticmethod
    def __counter_sort(number_array):
        # Initialize count array.
        counter_array_length = CounterSorter.__get_max_number(number_array) + 1
        count = [0] * counter_array_length

        # Store the count of each elements in count array
        for number in number_array:
            integer_item = int(number)
            count[integer_item] += 1

        # Store the cumulative count
        for i in range(1, counter_array_length):
            count[i] += count[i - 1]

        # Find the index of each element of the original array in count array
        # place the elements in output array.
        size = len(number_array)
        output = [0] * size

        i = size - 1
        while i >= 0:
            integer_item = int(number_array[i])
            output[count[integer_item] - 1] = number_array[i]
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
