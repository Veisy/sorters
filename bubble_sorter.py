from sorter import BaseSorter


class BubbleSorter(BaseSorter):

    BUBBLE_SORT = "Bubble Sort"

    @property
    def get_algorithm_name(self):
        return BubbleSorter.BUBBLE_SORT

    def sort(self):
        BubbleSorter.__bubble_sort(self.float_array)

    # Double underscore prefix of the method name makes it private.
    @staticmethod
    def __bubble_sort(float_array):
        length_float_array = len(float_array)

        # Loop through array and compare elements with adjacent elements.
        for i in range(length_float_array):

            for j in range(0, length_float_array - i - 1):

                if float_array[j] > float_array[j + 1]:
                    # Shortcut multi assignment in python without using a temp variable.
                    float_array[j], float_array[j + 1] = float_array[j + 1], float_array[j]
