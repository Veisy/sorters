from sorter import BaseSorter


class HeapSorter(BaseSorter):

    HEAP_SORT = "Heap Sort"

    @property
    def get_algorithm_name(self):
        return HeapSorter.HEAP_SORT

    def sort(self):
        self.__heap_sort(self.float_array)

    # Double underscore prefix of the method name makes it private.
    @staticmethod
    def __heap_sort(float_array):
        n = len(float_array)

        # Build max heap
        for i in range(n // 2, -1, -1):
            HeapSorter.__heapify(float_array, n, i)

        for i in range(n - 1, 0, -1):
            # Swap
            float_array[i], float_array[0] = float_array[0], float_array[i]

            # Heapify root element
            HeapSorter.__heapify(float_array, i, 0)

    @staticmethod
    def __heapify(float_array, n, i):
        # Find largest among root and children
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and float_array[i] < float_array[l]:
            largest = l

        if r < n and float_array[largest] < float_array[r]:
            largest = r

        # If root is not largest, swap with largest and continue heapifying
        if largest != i:
            float_array[i], float_array[largest] = float_array[largest], float_array[i]
            HeapSorter.__heapify(float_array, n, largest)
