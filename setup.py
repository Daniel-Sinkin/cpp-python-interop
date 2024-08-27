# setup.py
# pybind11 include directory
import pybind11
from setuptools import Extension, setup

# Extension module
ext_modules = [
    Extension(
        "add_module",  # name of the module
        ["bindings.cpp"],  # source files
        include_dirs=[pybind11.get_include()],
        language="c++",
    ),
]

setup(
    name="add_module",
    version="0.0.1",
    author="Your Name",
    description="A simple example of a C++ function exposed to Python",
    ext_modules=ext_modules,
)
