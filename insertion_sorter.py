from sorter import Sorter


class InsertionSorter(Sorter):

    def __init__(self, double_list):
        # Calls parent abstract class constructor (__init__ method).
        super().__init__(double_list)

        # The list to be sorted.
        self.double_list = double_list

    @property
    def get_algorithm_name(self):
        return "Insertion"

    def sort(self):
        InsertionSorter.insertion_sort(self.double_list)

    @staticmethod
    def insertion_sort(double_list):
        i = 1
        while i < len(double_list):
            j = i

            while j > 0 and double_list[j - 1] > double_list[j]:
                temp_value = double_list[j]
                double_list[j] = double_list[j - 1]
                double_list[j - 1] = temp_value
                j -= 1

            i += 1
