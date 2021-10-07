from sorter import Sorter


class InsertionSorter(Sorter):

    INSERTION_SORTER = "Insertion"

    def __init__(self, double_list):
        # Calls parent abstract class constructor (__init__ method).
        super().__init__(double_list)

    @property
    def get_algorithm_name(self):
        return InsertionSorter.INSERTION_SORTER

    def sort(self):
        InsertionSorter.insertion_sort(self.double_list)

    @staticmethod
    def insertion_sort(double_list):
        # Start from index 1 and compare values backward, and then jump the next index.
        i = 1
        while i < len(double_list):
            j = i

            while j > 0 and double_list[j - 1] > double_list[j]:
                # Shortcut multi assignment in python without using a temp variable.
                double_list[j], double_list[j - 1] = double_list[j - 1], double_list[j]
                j -= 1

            i += 1
