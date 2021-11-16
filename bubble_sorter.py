from sorter import BaseSorter


class BubbleSorter(BaseSorter):

    BUBBLE_SORT = "Bubble Sort"

    @property
    def get_algorithm_name(self):
        return BubbleSorter.BUBBLE_SORT

    def sort(self):
        BubbleSorter.__bubble_sort(self.number_array)

    # Double underscore prefix of the method name makes it private.
    @staticmethod
    def __bubble_sort(number_array):
        length_number_array = len(number_array)

        # Loop through array and compare elements with adjacent elements.
        for i in range(length_number_array):

            for j in range(0, length_number_array - i - 1):

                if number_array[j] > number_array[j + 1]:
                    # Shortcut multi assignment in python without using a temp variable.
                    number_array[j], number_array[j + 1] = number_array[j + 1], number_array[j]
