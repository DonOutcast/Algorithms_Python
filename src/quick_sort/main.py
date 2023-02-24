import time
from m_quick_sort import quick_sort_c
from quick_sort import quick_sort

if __name__ == "__main__":
    m_list_ten = [8, 1, 3, 2, 4, 9, 5, 7, 0, 6]
    print("Test bubble sort with array of numbers size 10 not sorted.")
    start = time.monotonic()
    quick_sort_c(m_list_ten, 10)
    stop = time.monotonic()
    print(f"Speed Cython function {(stop - start) * 10 ** 6} seconds.")
    start = time.monotonic()
    quick_sort(m_list_ten)
    stop = time.monotonic()
    print(f"Speed Python function {(stop - start) * 10 ** 6} seconds.")
    m_list_ten_sorted = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Test quick sort with array of numbers size 10 sorted.")
    start = time.monotonic()
    quick_sort_c(m_list_ten_sorted, 10)
    stop = time.monotonic()
    print(f"Speed Cython function {(stop - start) * 10 ** 6} seconds.")
    start = time.monotonic()
    quick_sort(m_list_ten_sorted)
    stop = time.monotonic()
    print(f"Speed Python function {(stop - start) * 10 ** 6} seconds.")
    m_list_fifty = [12, 11, 20, 45, 49, 23, 47, 42, 28, 41, 25, 0, 36, 1, 24, 6, 29, 16, 22, 9, 14, 13, 4, 40, 46, 18, 34, 15, 3, 27, 37, 8, 26, 32, 38, 48, 21, 31, 35, 44, 7, 30, 33, 43, 2, 39, 17, 19, 10, 5]
    print("Test quick sort with array of numbers size 50  not sorted.")
    start = time.monotonic()
    quick_sort_c(m_list_fifty, 10)
    stop = time.monotonic()
    print(f"Speed Cython function {(stop - start) * 10 ** 6} seconds.")
    start = time.monotonic()
    quick_sort(m_list_fifty)
    stop = time.monotonic()
    print(f"Speed Python function {(stop - start) * 10 ** 6} seconds.")
    m_list_hundred = [40, 17, 24, 23, 84, 87, 71, 22, 49, 74, 32, 1, 48, 99, 0, 65, 43, 67, 28, 52, 70, 73, 85, 95, 38, 14, 82, 26, 98, 5, 53, 58, 78, 88, 15, 79, 34, 96, 30, 91, 19, 63, 57, 50, 89, 36, 94, 86, 31, 45, 42, 11, 93, 29, 64, 69, 33, 6, 4, 81, 76, 16, 10, 72, 62, 39, 61, 12, 2, 47, 77, 60, 66, 20, 37, 54, 41, 97, 13, 55, 25, 80, 46, 83, 8, 3, 27, 75, 21, 56, 51, 68, 9, 7, 92, 18, 44, 59, 35, 90]
    print("Test quick sort with array of numbers size 100  not sorted.")
    start = time.monotonic()
    quick_sort_c(m_list_hundred, 10)
    stop = time.monotonic()
    print(f"Speed Cython function {(stop - start) * 10 ** 6} seconds.")
    start = time.monotonic()
    quick_sort(m_list_hundred)
    stop = time.monotonic()
    print(f"Speed Python function {(stop - start) * 10 ** 6} seconds.")
