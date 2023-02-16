from distutils.core import setup, Extension
from Cython.Build import cythonize

extensions = [Extension('selection_sort_c', ["m_selection_sort.pyx"])]
setup(name="selection_sort_c", ext_modules=cythonize("m_selection_sort.pyx"))
