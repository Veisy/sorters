from abc import ABC
from functools import reduce
from src.algorithms.sorter import Sorter


class RadixSorter(Sorter, ABC):
    RADIX_SORT = "Radix Sort"

    @property
    def get_algorithm_name(self):
        return self.RADIX_SORT

    def sort(self):
        self.__radix_sort()

        # If NOT animating, we only need sorted array.
        if not self.is_animating:
            self.intermediate_number_arrays.append(self.number_array)

    def __radix_sort(self):
        num_digit = self.__get_num_digits()

        for digit in range(0, num_digit):
            buckets = [[] for _ in range(10)]
            for item in self.number_array:
                # num is the bucket number that the item will be put into.
                num = int(item // 10 ** digit % 10)
                buckets[num].append(item)

                self.collectIntermediateArrays(RadixSorter.__flatten(buckets))

            self.number_array = self.__flatten(buckets)

    # get number of digits in largest item
    def __get_num_digits(self):
        max_digit = 0
        for item in self.number_array:
            max_digit = max(max_digit, item)

        # Convert int to get whole part, and then str to get length.
        return len(str(int(max_digit)))

    @staticmethod
    def __flatten(buckets):
        return reduce(lambda x, y: x + y, buckets)
