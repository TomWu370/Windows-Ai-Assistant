#include <pybind11/pybind11.h>
using namespace std;
namespace py = pybind11;

// function
bool collide(py::object a, py::object b) {
    auto a_x = a.attr("x").cast<double>();
    auto a_y = a.attr("y").cast<double>();
    auto a_width = a.attr("width").cast<double>();
    auto a_height = a.attr("height").cast<double>();
    auto b_x = b.attr("x").cast<double>();
    auto b_y = b.attr("y").cast<double>();
    auto b_width = b.attr("width").cast<double>();
    auto b_height = b.attr("height").cast<double>();
    return a_x <= (b_x + b_width) && (a_x + a_width) >= b_x && a_y <= (b_y + b_height) && (a_y + a_height) >= b_y;
}

PYBIND11_MODULE(collision, m) {
    // Expose the process_list function to Python
    m.def("collide", &collide, "check if 2 object collide");
}

