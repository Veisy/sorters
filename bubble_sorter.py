from sorter import Sorter


class BubbleSorter(Sorter):

    def __init__(self, double_list):
        # Calls parent abstract class constructor (__init__ method).
        super().__init__(double_list)

    @property
    def get_algorithm_name(self):
        return "Bubble Sort"

    def sort(self):
        BubbleSorter.bubble_sort(self.double_list)

    @staticmethod
    def bubble_sort(double_list):
        length_double_list = len(double_list)

        # Loop through all array elements
        for i in range(length_double_list):

            for j in range(0, length_double_list - i - 1):

                if double_list[j] > double_list[j + 1]:
                    # Shortcut multi assignment in python without using a temp variable.
                    double_list[j], double_list[j + 1] = double_list[j + 1], double_list[j]





