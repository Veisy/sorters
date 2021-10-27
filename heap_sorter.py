from sorter import BaseSorter


class HeapSorter(BaseSorter):

    HEAP_SORT = "Heap"

    def __init__(self, float_array):
        # Calls parent abstract class constructor (__init__ method).
        super().__init__(float_array)

    @property
    def get_algorithm_name(self):
        return HeapSorter.HEAP_SORT

    def sort(self):
        HeapSorter.heap_sort(self.float_array)

    @staticmethod
    def heap_sort(float_array):
        n = len(float_array)

        # Build max heap
        for i in range(n // 2, -1, -1):
            HeapSorter.heapify(float_array, n, i)

        for i in range(n - 1, 0, -1):
            # Swap
            float_array[i], float_array[0] = float_array[0], float_array[i]

            # Heapify root element
            HeapSorter.heapify(float_array, i, 0)

    @staticmethod
    def heapify(float_array, n, i):
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
            HeapSorter.heapify(float_array, n, largest)
