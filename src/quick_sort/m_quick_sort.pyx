cpdef quick_sort_c(list array, int size):
    cdef int i
    cdef int j
    if len(array) < 2:
        return array
    pivot = array[0]
    less = [i for i in array[1:] if i > pivot]
    greater = [j for j in array[1:] if j < pivot]
    return quick_sort_c(less) + [pivot] + quick_sort_c(greater)
