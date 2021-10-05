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
        i = 1
        while i < len(self.double_list):
            j = i

            while j > 0 and self.double_list[j - 1] > self.double_list[j]:
                temp_value = self.double_list[j]
                self.double_list[j] = self.double_list[j - 1]
                self.double_list[j - 1] = temp_value
                j -= 1

            i += 1




