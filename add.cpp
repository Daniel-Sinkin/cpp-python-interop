// bindings.cpp
#include <pybind11/pybind11.h>

// Declaration of the function
int add(int a, int b)
{
    return a + b;
}

// Creating the module
PYBIND11_MODULE(add_module, m)
{
    m.def("add", &add, "A function that adds two numbers");
}