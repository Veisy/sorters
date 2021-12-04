from src.algorithms.sorter import Sorter


class HeapSorter(Sorter):
    HEAP_SORT = "Heap Sort"

    @property
    def get_algorithm_name(self):
        return self.HEAP_SORT

    def sort(self):
        self.__heap_sort(self.number_array, self.intermediate_number_arrays, self.is_animating)

        # If NOT animating, we only need sorted array.
        if not self.is_animating:
            self.intermediate_number_arrays.append(self.number_array)

    # Double underscore prefix of the method name makes it private.
    @staticmethod
    def __heap_sort(number_array, intermediate_number_arrays, is_animating):
        n = len(number_array)

        # Build max heap
        for i in range(n // 2, -1, -1):
            HeapSorter.__heapify(number_array, n, i, intermediate_number_arrays, is_animating)

        for i in range(n - 1, 0, -1):
            # Swap and if animating, collect intermediate arrays
            Sorter.swap(number_array, i, 0, intermediate_number_arrays, is_animating)

            # Heapify root element
            HeapSorter.__heapify(number_array, i, 0, intermediate_number_arrays, is_animating)

    @staticmethod
    def __heapify(number_array, n, i, intermediate_number_arrays, is_animating):
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
            # Swap and if animating, collect intermediate arrays
            Sorter.swap(number_array, i, largest, intermediate_number_arrays, is_animating)
            HeapSorter.__heapify(number_array, n, largest, intermediate_number_arrays, is_animating)
