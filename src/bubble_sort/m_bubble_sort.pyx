cpdef bubble_sort_c(list array, int size):
    cdef int i
    cdef int j
    cdef int sorted_already
    cdef int temp
    for i in range(size):
        sorted_already = 1
        for j in range(size - 1 - i):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
                sorted_already = 0
        if sorted_already:
            break
    return array
