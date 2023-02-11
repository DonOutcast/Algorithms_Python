from distutils.core import setup, Extension
from Cython.Build import cythonize

extensions = [Extension('bubble_sort_c', ["m_bubble_sort.pyx"])]
setup(name="bubble_sort_c", ext_modules=cythonize("m_bubble_sort.pyx"))
