from src.algorithms.sorter import Sorter
from src.algorithms.insertion_sorter import InsertionSorter


class MergeSorter(Sorter):
    MERGE_SORT = "Merge Sort"
    MERGE_INSERTION_SORT = "Merge-Insertion Sort"

    def __init__(self, is_animating=False, is_insertion_based=False):
        super().__init__(is_animating)
        self.is_insertion_based = is_insertion_based

    @property
    def get_algorithm_name(self):
        if self.is_insertion_based:
            return self.MERGE_INSERTION_SORT
        return self.MERGE_SORT

    def sort(self):
        self.__merge_sort(self.number_array, self.intermediate_number_arrays,
                          self.is_animating, self.is_insertion_based)

        # If NOT animating, we only need sorted array.
        if not self.is_animating:
            self.intermediate_number_arrays.append(self.number_array)

    # Double underscore prefix of the method name makes it private.
    @staticmethod
    def __merge_sort(number_array, intermediate_number_arrays, is_animating, is_insertion_based=False):
        # Length of the array stored. Pre-calculated instead of multiple calls.
        length_float_array = len(number_array)

        # Base condition.
        if length_float_array < 2:
            return

        # Find the mid-index.
        midpoint = int(length_float_array / 2)

        # create left and right sub arrays
        # mid-elements (from index 0 till mid-1) should be part of left sub-array.
        # and (n-mid) elements (from mid to n-1) will be part of right sub-array.
        part_left = number_array[0: midpoint]
        part_right = number_array[midpoint: length_float_array]

        if is_insertion_based:
            InsertionSorter.insertion_sort(part_left, intermediate_number_arrays, is_animating)
            InsertionSorter.insertion_sort(part_right, intermediate_number_arrays, is_animating)
        else:
            MergeSorter.__merge_sort(part_left, intermediate_number_arrays, is_animating)
            MergeSorter.__merge_sort(part_right, intermediate_number_arrays, is_animating)

        Sorter.collectIntermediateArrays(number_array, intermediate_number_arrays, is_animating)

        MergeSorter.__merge(number_array, part_left, part_right, intermediate_number_arrays, is_animating)

    @staticmethod
    def __merge(number_array, part_left, part_right, intermediate_number_arrays, is_animating):
        i, j, k = 0, 0, 0
        length_part_left, length_part_right = len(part_left), len(part_right)

        while i < length_part_left and j < length_part_right:
            if part_left[i] < part_right[j]:
                number_array[k] = part_left[i]
                k, i = (k + 1), (i + 1)
            else:
                number_array[k] = part_right[j]
                k, j = (k + 1), (j + 1)

        while i < length_part_left:
            number_array[k] = part_left[i]
            k, i = (k + 1), (i + 1)

        while j < length_part_right:
            number_array[k] = part_right[j]
            k, j = (k + 1), (j + 1)

        Sorter.collectIntermediateArrays(number_array, intermediate_number_arrays, is_animating)
