from distutils.core import setup, Extension
from Cython.Build import cythonize

extensions = [Extension('insertion_sort_c', ["m_insertion_sort.pyx"])]
setup(name="insertion_sort_c", ext_modules=cythonize("m_insertion_sort.pyx"))
