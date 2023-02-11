//#define PY_SSIZE_T_CLEAN
//#include <Python.h>
//
//int* bubble_sort(int array[], int size)
//
//static PyObject *_bubble_sort(PyObject *self, PyObject *args) {
//    for (int step = 0; step < size - 1; step++) {
//        int sorted_already = 1;
//        for (int i = 0; i < size - 1; i++) {
//            if (array[i] > array[i + 1]) {
//                int temp = array[i];
//                array[i] = array[i + 1];
//                array[i + 1] = temp;
//                sorted_already = 0;
//            }
//        }
//        if (sorted_already) {
//            break;
//        }
//    }
//
//}
//
//
//
//static struct PyModuleDef bubble = {PyModuleDef_HEAD_INIT, "bubble_sort",
//                                        NULL, -1, ModuleMethods};
//
//PyMODINIT_FUNC PyInit_calculator(void) { return PyModule_Create(&bubble); } PyInit_calculator(void) { return PyModule_Create(&bubble); }