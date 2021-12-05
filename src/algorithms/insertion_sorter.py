from src.algorithms.sorter import Sorter


class InsertionSorter(Sorter):
    INSERTION_SORT = "Insertion Sort"

    @property
    def get_algorithm_name(self):
        return self.INSERTION_SORT

    def sort(self):
        self.insertion_sort()

        # If NOT animating, we only need sorted array.
        if not self.is_animating:
            self.intermediate_number_arrays.append(self.number_array)

    def insertion_sort(self):
        # Start from index 1 and compare values backward, and then jump the next index.
        i = 1
        while i < len(self.number_array):
            j = i
            while j > 0 and self.number_array[j - 1] > self.number_array[j]:
                # Swap and if animating, collect intermediate arrays
                self.swap(j, j - 1)

                j -= 1
            i += 1
