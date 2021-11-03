import random
from sorter import BaseSorter


class QuickSorter(BaseSorter):

    QUICK_SORT = "Quick Sort"

    @property
    def get_algorithm_name(self):
        return QuickSorter.QUICK_SORT

    def sort(self):
        self.float_array = QuickSorter.__quick_sort(self.float_array)

    @staticmethod
    def __quick_sort(float_array):

        # If list is empty, return.
        if not any(float_array):
            return float_array
        pivot = float_array[random.choice(range(0, len(float_array)))]

        head = QuickSorter.__quick_sort([x for x in float_array if x < pivot])
        tail = QuickSorter.__quick_sort([x for x in float_array if x > pivot])
        return head + [x for x in float_array if x == pivot] + tail
