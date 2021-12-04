from src.algorithms.sorter import Sorter


class InsertionSorter(Sorter):
    INSERTION_SORT = "Insertion Sort"

    @property
    def get_algorithm_name(self):
        return self.INSERTION_SORT

    def sort(self):
        self.insertion_sort(self.number_array, self.intermediate_number_arrays, self.is_animating)

        # If NOT animating, we only need sorted array.
        if not self.is_animating:
            self.intermediate_number_arrays.append(self.number_array)

    @staticmethod
    def insertion_sort(number_array, intermediate_number_arrays, is_animating):
        # Start from index 1 and compare values backward, and then jump the next index.
        i = 1
        while i < len(number_array):
            j = i
            while j > 0 and number_array[j - 1] > number_array[j]:
                # Swap and if animating, collect intermediate arrays
                Sorter.swap(number_array, j, j - 1, intermediate_number_arrays, is_animating)

                j -= 1
            i += 1
