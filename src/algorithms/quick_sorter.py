import random
from src.algorithms.sorter import Sorter


class QuickSorter(Sorter):
    QUICK_SORT = "Quick Sort"

    @property
    def get_algorithm_name(self):
        return self.QUICK_SORT

    def sort(self):
        self.__quick_sort(self.number_array, 0, len(self.number_array) - 1,
                          self.intermediate_number_arrays, self.is_animating)

        # If NOT animating, we only need sorted array.
        if not self.is_animating:
            self.intermediate_number_arrays.append(self.number_array)

    @staticmethod
    def __quick_sort(number_array, left, right, intermediate_number_arrays, is_animating):
        index = QuickSorter.__partition(number_array, left, right, intermediate_number_arrays, is_animating)
        # Sorting left half
        if left < index - 1:
            QuickSorter.__quick_sort(number_array, left, index - 1, intermediate_number_arrays, is_animating)
        # Sorting right half
        if index < right:
            QuickSorter.__quick_sort(number_array, index, right, intermediate_number_arrays, is_animating)

    @staticmethod
    def __partition(number_array, left, right, intermediate_number_arrays, is_animating):
        # Pivot Point
        pivot = number_array[(left + right) // 2]
        while left <= right:
            # Find the elements on left that should be on right
            while number_array[left] < pivot:
                left += 1
            # Find the elements on right that should be on left
            while number_array[right] > pivot:
                right -= 1

            # Swap elements, and move left and right indices
            if left <= right:
                # Swap and if animating, collect intermediate arrays
                Sorter.swap(number_array, left, right, intermediate_number_arrays, is_animating)
                left += 1
                right -= 1

        return left
