cpdef insertion_sort_c(list array, int size):
    cdef int i
    cdef int j
    cdef int temp
    for i in range(1, size):
        key = array[i]
        j = i -1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key
    return array
