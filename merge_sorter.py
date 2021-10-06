from sorter import Sorter
from insertion_sorter import InsertionSorter


class MergeSorter(Sorter):

    def __init__(self, double_list):
        # Calls parent abstract class constructor (__init__ method).
        super().__init__(double_list)

    @property
    def get_algorithm_name(self):
        return "Merge (Fake)"

    def sort(self):
        self.merge_sort(self.double_list)

    @staticmethod
    def merge_sort(double_list):
        # Length of the array stored. Pre-calculated instead of multiple calls.
        length_double_list = len(double_list)

        # Base condition.
        if length_double_list < 2:
            return

        # Find the mid index.
        midpoint = int(length_double_list / 2)

        # create left and right sub arrays
        # mid elements (from index 0 till mid-1) should be part of left sub-array.
        # and (n-mid) elements (from mid to n-1) will be part of right sub-array.
        part_left = double_list[0: midpoint]
        part_right = double_list[midpoint: length_double_list]

        # MergeSorter.merge_sort(part_left)
        # MergeSorter.merge_sort(part_right)
        InsertionSorter.insertion_sort(part_left)
        InsertionSorter.insertion_sort(part_right)
        MergeSorter.merge(double_list, part_left, part_right)

    @staticmethod
    def merge(double_list, part_left, part_right):
        i, j, k = 0, 0, 0
        length_part_left, length_part_right = len(part_left), len(part_right)

        while i < length_part_left and j < length_part_right:
            if part_left[i] < part_right[j]:
                double_list[k] = part_left[i]
                k, i = (k + 1), (i + 1)
            else:
                double_list[k] = part_right[j]
                k, j = (k + 1), (j + 1)

        while i < length_part_left:
            double_list[k] = part_left[i]
            k, i = (k + 1), (i + 1)

        while j < length_part_right:
            double_list[k] = part_right[j]
            k, j = (k + 1), (j + 1)
