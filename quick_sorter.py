import random
from sorter import BaseSorter


class QuickSorter(BaseSorter):

    QUICK_SORT = "Quick"

    def __init__(self, float_array):
        # Calls parent abstract class constructor (__init__ method).
        super().__init__(float_array)

    @property
    def get_algorithm_name(self):
        return QuickSorter.QUICK_SORT

    def sort(self):
        self.float_array = QuickSorter.quick_sort(self.float_array)

    @staticmethod
    def quick_sort(float_array):

        # If list is empty, return.
        if not any(float_array):
            return float_array
        pivot = float_array[random.choice(range(0, len(float_array)))]

        head = QuickSorter.quick_sort([x for x in float_array if x < pivot])
        tail = QuickSorter.quick_sort([x for x in float_array if x > pivot])
        return head + [x for x in float_array if x == pivot] + tail
