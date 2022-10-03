from src.algorithms.sorter import Sorter


class HeapSorter(Sorter):
    HEAP_SORT = "Heap Sort"

    @property
    def get_algorithm_name(self):
        return self.HEAP_SORT

    def sort(self):
        self.__heap_sort()

        # If NOT animating, we only need sorted array.
        if not self.is_animating:
            self.intermediate_number_arrays.append(self.number_array)

    # Double underscore prefix of the method name makes it private.
    def __heap_sort(self):
        n = len(self.number_array)

        # Build max heap
        for i in range(n // 2, -1, -1):
            self.__heapify(n, i)

        for i in range(n - 1, 0, -1):
            # Swap and if animating, collect intermediate arrays
            self.swap(i, 0)

            # Heapify root element
            self.__heapify(i, 0)

    def __heapify(self, n, i):
        # Find largest among root and children
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and self.number_array[i] < self.number_array[left]:
            largest = left

        if right < n and self.number_array[largest] < self.number_array[right]:
            largest = right

        # If root is not largest, swap with largest and continue heapify
        if largest != i:
            # Swap and if animating, collect intermediate arrays
            self.swap(i, largest)
            self.__heapify(n, largest)
