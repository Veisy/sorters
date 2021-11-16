from sorter import BaseSorter


class HeapSorter(BaseSorter):

    HEAP_SORT = "Heap Sort"

    @property
    def get_algorithm_name(self):
        return HeapSorter.HEAP_SORT

    def sort(self):
        self.__heap_sort(self.number_array)

    # Double underscore prefix of the method name makes it private.
    @staticmethod
    def __heap_sort(number_array):
        n = len(number_array)

        # Build max heap
        for i in range(n // 2, -1, -1):
            HeapSorter.__heapify(number_array, n, i)

        for i in range(n - 1, 0, -1):
            # Swap
            number_array[i], number_array[0] = number_array[0], number_array[i]

            # Heapify root element
            HeapSorter.__heapify(number_array, i, 0)

    @staticmethod
    def __heapify(number_array, n, i):
        # Find largest among root and children
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and number_array[i] < number_array[l]:
            largest = l

        if r < n and number_array[largest] < number_array[r]:
            largest = r

        # If root is not largest, swap with largest and continue heapifying
        if largest != i:
            number_array[i], number_array[largest] = number_array[largest], number_array[i]
            HeapSorter.__heapify(number_array, n, largest)
