from src.algorithms.sorter import BaseSorter


class InsertionSorter(BaseSorter):

    INSERTION_SORT = "Insertion Sort"

    @property
    def get_algorithm_name(self):
        return InsertionSorter.INSERTION_SORT

    def sort(self):
        InsertionSorter.insertion_sort(self.number_array)

    @staticmethod
    def insertion_sort(number_array):
        # Start from index 1 and compare values backward, and then jump the next index.
        i = 1
        while i < len(number_array):
            j = i

            while j > 0 and number_array[j - 1] > number_array[j]:
                # Shortcut multi assignment in python without using a temp variable.
                number_array[j], number_array[j - 1] = number_array[j - 1], number_array[j]
                j -= 1

            i += 1
