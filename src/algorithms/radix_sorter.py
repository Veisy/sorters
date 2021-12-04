from abc import ABC
from functools import reduce
from src.algorithms.sorter import Sorter


class RadixSorter(Sorter, ABC):
    RADIX_SORT = "Radix Sort"

    @property
    def get_algorithm_name(self):
        return self.RADIX_SORT

    def sort(self):
        self.number_array = self.__radix_sort(self.number_array, self.intermediate_number_arrays, self.is_animating)

        # If NOT animating, we only need sorted array.
        if not self.is_animating:
            self.intermediate_number_arrays.append(self.number_array)

    @staticmethod
    def __radix_sort(number_array, intermediate_number_arrays, is_animating):
        num_digit = RadixSorter.__get_num_digits(number_array)

        for digit in range(0, num_digit):
            buckets = [[] for _ in range(10)]
            for item in number_array:
                # num is the bucket number that the item will be put into.
                num = int(item // 10 ** digit % 10)
                buckets[num].append(item)

                Sorter.collectIntermediateArrays(RadixSorter.__flatten(buckets), intermediate_number_arrays, is_animating)

            number_array = RadixSorter.__flatten(buckets)

        return number_array

    # get number of digits in largest item
    @staticmethod
    def __get_num_digits(number_array):
        max_digit = 0
        for item in number_array:
            max_digit = max(max_digit, item)

        # Convert int to get whole part, and then str to get length.
        return len(str(int(max_digit)))

    @staticmethod
    def __flatten(buckets):
        return reduce(lambda x, y: x + y, buckets)
