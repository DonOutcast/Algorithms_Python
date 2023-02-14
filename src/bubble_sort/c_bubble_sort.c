#include <stdio.h>

int * c_bubble_sort(int *array, int size) {
     int i, j, already_sorted, temp;
    for (i = 0; i < size - 1; i++) {
        already_sorted = 1;  
        for (j = 0; j < size - i - 1; j++) {
            if (array[j] > array[j + 1]) {
                temp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = temp;
                already_sorted = 0;
            }
        }
        if (already_sorted) {
            break;
        }
    }
    return array;
}

