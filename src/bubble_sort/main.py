import time
from m_bubble_sort import bubble_sort_c
from bubble import bubble_sort
from ctypes import *

if __name__ == "__main__":
    so_file = "my_c_bubble_sort.so"
    my_fun = cdll.LoadLibrary(so_file)
    print(my_fun())
    # print(my_fun([1, 2, 3, 4], 4))
    # m_list_ten = [8, 1, 3, 2, 4, 9, 5, 7, 0, 6]
    # print("Test bubble sort with array of numbers size 10 not sorted.")
    # start = time.monotonic()
    # bubble_sort_c(m_list_ten, 10)
    # stop = time.monotonic()
    # print(f"Speed Cython function {(stop - start) * 10 ** 6 } seconds.")
    # start = time.monotonic()
    # bubble_sort(m_list_ten)
    # stop = time.monotonic()
    # print(f"Speed Python function {(stop - start) * 10 ** 6 } seconds.")
    # m_list_ten_sorted = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # print("Test bubble sort with array of numbers size 10 sorted.")
    # start = time.monotonic()
    # bubble_sort_c(m_list_ten_sorted, 10)
    # stop = time.monotonic()
    # print(f"Speed Cython function {(stop - start) * 10 ** 6 } seconds.")
    # start = time.monotonic()
    # bubble_sort(m_list_ten_sorted)
    # stop = time.monotonic()
    # print(f"Speed Python function {(stop - start) * 10 ** 6 } seconds.")
