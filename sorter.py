from abc import ABC, abstractmethod


# Base abstract class of sorting algorithms.
# This class defines methods for child classes.
class BaseSorter(ABC):

    def __init__(self):
        # The list to be sorted.
        self.float_array = []
        self.execution_timings = []

    @abstractmethod
    def get_algorithm_name(self):
        pass

    @abstractmethod
    def sort(self):
        pass
