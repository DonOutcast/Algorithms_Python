from distutils.core import setup, Extension
from Cython.Build import cythonize

extensions = [Extension('quick_sort_c', ["m_quick_sort.pyx"])]
setup(name="quick_sort_c", ext_modules=cythonize("m_quick_sort.pyx"))
