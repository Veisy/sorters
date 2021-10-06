from sorter import Sorter
from insertion_sorter import InsertionSorter


class MergeSorter(Sorter):

    def __init__(self, double_list):
        # Calls parent abstract class constructor (__init__ method).
        super().__init__(double_list)

        # The list to be sorted.
        self.double_list = double_list

    @property
    def get_algorithm_name(self):
        return "Merge (Fake)"

    def sort(self):
        self.merge_sort(self.double_list)

    @staticmethod
    def merge_sort(double_list):
        # Length of the array stored. Pre-calculated instead of multiple calls.
        double_list_length = len(double_list)

        # Base condition.
        if double_list_length < 2:
            return

        # Find the mid index.
        midpoint = int(double_list_length / 2)

        # create left and right sub arrays
        # mid elements (from index 0 till mid-1) should be part of left sub-array.
        # and (n-mid) elements (from mid to n-1) will be part of right sub-array.
        part_left = double_list[0: midpoint]
        part_right = double_list[midpoint: double_list_length]

        # MergeSorter.merge_sort(part_left)
        # MergeSorter.merge_sort(part_right)
        InsertionSorter.insertion_sort(part_left)
        InsertionSorter.insertion_sort(part_right)
        MergeSorter.merge(double_list, part_left, part_right)

    @staticmethod
    def merge(double_list, part_left, part_right):
        i, j, k = 0, 0, 0
        part_left_length = len(part_left)
        part_right_right = len(part_right)

        while i < part_left_length and j < part_right_right:
            if part_left[i] < part_right[j]:
                double_list[k] = part_left[i]
                i += 1
            else:
                double_list[k] = part_right[j]
                j += 1
            k += 1

        while i < part_left_length:
            double_list[k] = part_left[i]
            k += 1
            i += 1

        while j < part_right_right:
            double_list[k] = part_right[j]
            k += 1
            j += 1
