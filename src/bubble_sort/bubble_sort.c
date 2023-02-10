#include <stdio.h>
void bubble_sort(int array[], int size) {
    for (int step = 0; step < size - 1; step++) {
        int sorted_already = 1;
        for (int i = 0; i < size - 1; i++) {
            if (array[i] > array[i + 1]) { 
                int temp = array[i];
                array[i] = array[i + 1];
                array[i + 1] = temp;
                sorted_already = 0;
            }
        }
        if (sorted_alredy) {
            break;
        }
    }
}

