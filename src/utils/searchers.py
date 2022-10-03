def binary_search(number_array, element):
    low = 0
    high = len(number_array) - 1

    while low <= high:
        mid = (low + high) // 2

        if number_array[mid] < element:
            low = mid + 1
        elif number_array[mid] > element:
            high = mid - 1
        else:
            return mid

    return -1


def linear_search(number_array, element):
    for index in range(len(number_array)):
        if number_array[index] == element:
            return index

    return -1
