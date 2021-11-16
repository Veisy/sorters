import random
from sorter import BaseSorter


class QuickSorter(BaseSorter):

    QUICK_SORT = "Quick Sort"

    @property
    def get_algorithm_name(self):
        return QuickSorter.QUICK_SORT

    def sort(self):
        self.number_array = QuickSorter.__quick_sort(self.number_array)

    @staticmethod
    def __quick_sort(number_array):

        # If list is empty, return.
        if not any(number_array):
            return number_array
        pivot = number_array[random.choice(range(0, len(number_array)))]

        head = QuickSorter.__quick_sort([x for x in number_array if x < pivot])
        tail = QuickSorter.__quick_sort([x for x in number_array if x > pivot])
        return head + [x for x in number_array if x == pivot] + tail
