from sorter import Sorter


class MergeSorter(Sorter):

    def __init__(self, double_list):
        # Calls parent abstract class constructor (__init__ method).
        super().__init__(double_list)

        # The list to be sorted.
        self.double_list = double_list

    @property
    def get_algorithm_name(self):
        return "Merge"

    def sort(self):
        self.merge_sort(self.double_list)

    def merge_sort(self, double_list):
        # Base condition.
        if len(double_list) < 2:
            return

        # Find the mid index.
        midpoint = int(len(double_list) / 2)

        # create left and right sub arrays
        # mid elements (from index 0 till mid-1) should be part of left sub-array.
        # and (n-mid) elements (from mid to n-1) will be part of right sub-array.
        part_left = double_list[0: midpoint]
        part_right = double_list[midpoint: len(double_list) - midpoint]

        self.merge_sort(part_left)
        self.merge_sort(part_right)
        self.merge(double_list, part_left, part_right)

    @staticmethod
    def merge(double_list, part_left, part_right):
        i, j, k = 0, 0, 0

        while i < len(part_left) and j < len(part_right):
            if part_left[i] < part_right[j]:
                double_list[k] = part_left[i]
                i += 1
            else:
                double_list[k] = part_right[j]
                j += 1
            k += 1

        while i < len(part_left):
            double_list[k] = part_left[i]
            k += 1
            i += 1

        while j < len(part_right):
            double_list[k] = part_right[j]
            k += 1
            j += 1

