from src.algorithms.sorter import Sorter


class QuickSorter(Sorter):
    QUICK_SORT = "Quick Sort"

    @property
    def get_algorithm_name(self):
        return self.QUICK_SORT

    def sort(self):
        self.__quick_sort(0, len(self.number_array) - 1)

        # If NOT animating, we only need sorted array.
        if not self.is_animating:
            self.intermediate_number_arrays.append(self.number_array)

    def __quick_sort(self, left, right):
        index = self.__partition(left, right)
        # Sorting left half
        if left < index - 1:
            self.__quick_sort(left, index - 1)
        # Sorting right half
        if index < right:
            self.__quick_sort(index, right)

    def __partition(self, left, right):
        # Pivot Point
        pivot = self.number_array[(left + right) // 2]
        while left <= right:
            # Find the elements on left that should be on right
            while self.number_array[left] < pivot:
                left += 1
            # Find the elements on right that should be on left
            while self.number_array[right] > pivot:
                right -= 1

            # Swap elements, and move left and right indices
            if left <= right:
                # Swap and if animating, collect intermediate arrays
                self.swap(left, right)
                left += 1
                right -= 1

        return left
