from src.algorithms.sorter import Sorter


class BubbleSorter(Sorter):
    BUBBLE_SORT = "Bubble Sort"

    @property
    def get_algorithm_name(self):
        return self.BUBBLE_SORT

    def sort(self):
        self.__bubble_sort(self.number_array, self.intermediate_number_arrays, self.is_animating)

        # If NOT animating, we only need sorted array.
        if not self.is_animating:
            self.intermediate_number_arrays.append(self.number_array)

    # Double underscore prefix of the method name makes it private.
    @staticmethod
    def __bubble_sort(number_array, intermediate_number_arrays, is_animating):
        length_number_array = len(number_array)

        # Loop through array and compare elements with adjacent elements.
        for i in range(length_number_array):

            for j in range(0, length_number_array - i - 1):

                if number_array[j] > number_array[j + 1]:
                    # Swap and if animating, collect intermediate arrays
                    Sorter.swap(number_array, j, j + 1, intermediate_number_arrays, is_animating)
