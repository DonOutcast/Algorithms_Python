cpdef selection_sort_c(list array, int size):
    cdef int i
    cdef int j
    cdef int temp
    cdef int minimum
    for i in range(size):
        minimum = i
        for j in range(i + 1, size):
            if array[j] < array[minimum]:
                minimum = j
        temp = array[i]
        array[i] = array[minimum]
        array[minimum] = temp
    return array
