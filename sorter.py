from abc import ABC, abstractmethod


# Base abstract class of sorting algorithms.
# This class defines methods for child classes.
class Sorter(ABC):

    def __init__(self, double_list):
        # The list to be sorted.
        self.array_list = double_list

    @abstractmethod
    def get_algorithm_name(self):
        pass

    @abstractmethod
    def sort(self):
        pass

