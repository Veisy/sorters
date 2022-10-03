# Check if number array is sorted or not.
def is_sorted(array):
    for index in range(len(array) - 1):
        if array[index] > array[index + 1]:
            return False
    return True
