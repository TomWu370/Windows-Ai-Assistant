#include <pybind11/pybind11.h>
using namespace std;
namespace py = pybind11;

// Define a C++ struct representing a box
struct Box {
    public:
        Box(py::object obj) {
            // Get the x, y, width and height of each object
            x = obj.attr("x").cast<double>();
            y = obj.attr("y").cast<double>();
            width = obj.attr("width").cast<double>();
            height = obj.attr("height").cast<double>();
        }
    double x;
    double y;
    double width;
    double height;
};

// function
bool collide(py::object a_obj, py::object b_obj) {
    Box a = Box(a_obj);
    Box b = Box(b_obj);

    // Check for collision including touching surfaces
    bool horizontal_overlap = (a.x <= (b.x + b.width) && (a.x + a.width) >= b.x) ||
                              (b.x <= (a.x + a.width) && (b.x + b.width) >= a.x);
    bool vertical_overlap = (a.y <= (b.y + b.height) && (a.y + a.height) >= b.y) ||
                            (b.y <= (a.y + a.height) && (b.y + b.height) >= a.y);

    return horizontal_overlap && vertical_overlap;
}

PYBIND11_MODULE(collision, m) {
    // Expose the process_list function to Python
    m.def("collide", &collide, "check if 2 object collide");
}

