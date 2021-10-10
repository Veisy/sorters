from sorter import BaseSorter


class InsertionSorter(BaseSorter):

    INSERTION_SORTER = "Insertion"

    def __init__(self, float_array):
        # Calls parent abstract class constructor (__init__ method).
        super().__init__(float_array)

    @property
    def get_algorithm_name(self):
        return InsertionSorter.INSERTION_SORTER

    def sort(self):
        InsertionSorter.insertion_sort(self.float_array)

    @staticmethod
    def insertion_sort(float_array):
        # Start from index 1 and compare values backward, and then jump the next index.
        i = 1
        while i < len(float_array):
            j = i

            while j > 0 and float_array[j - 1] > float_array[j]:
                # Shortcut multi assignment in python without using a temp variable.
                float_array[j], float_array[j - 1] = float_array[j - 1], float_array[j]
                j -= 1

            i += 1
