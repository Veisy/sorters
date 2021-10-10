from ctypes import *

# Loading my C libraries.
c_merge_sorter = CDLL('./merge_sorter.so')
c_insertion_sorter = CDLL('./insertion_sorter.so')

# NAME: VEYSEL YUSUF YILMAZ, NO: 190403062
# This is the Homework 1 of Introduction to Algorithms course.
# Several sorting algorithms are implemented and analyzed.
# TODO: User Interface implementation.

while True:
    operation = input("\n\nPlease select the operation you want to do:\n" +
                      "1-)Insertion Sort\n" +
                      "2-)Merge Sort\n" +
                      "3-)Exit\n")

    if operation == str(3):
        break
    elif operation == str(1):
        c_merge_sorter.main()
    elif operation == str(2):
        c_insertion_sorter.main()
    else:
        print("Invalid input. Please enter a number between 1-3.")




