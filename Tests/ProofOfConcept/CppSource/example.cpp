#include <pybind11/pybind11.h>
using namespace std;
// function
int add(int a, int b) {
    return a+b;
}


// binding
PYBIND11_MODULE(example, m) { // need to pass module name as bind
    m.doc() = "pybind11 example plugin"; // optional module docstring
    m.def("add", &add, "A function which return a string");
}