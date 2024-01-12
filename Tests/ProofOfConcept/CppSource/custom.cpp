// main.cpp
#include <pybind11/pybind11.h>

namespace py = pybind11;

// Define a C++ function that takes a Python list of objects
void process_list(py::list my_objects) {
    // Iterate through the Python list
    for (const auto& obj : my_objects) {
        // Assuming the Python class has a "display" method
        obj.attr("display")();
    }
}

PYBIND11_MODULE(custom, m) {
    // No need to define a C++ class here

    // Expose the process_list function to Python
    m.def("process_list", &process_list, "Process a list of Python objects");
}
