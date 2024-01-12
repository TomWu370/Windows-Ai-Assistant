cmake_minimum_required(VERSION 3.5)
project(collision) # module name

# Find Pybind11 package
find_package(pybind11 REQUIRED)

pybind11_add_module(collision CollisionDetection.cpp) # map module name to cpp file (filename)
target_link_libraries(collision PRIVATE pybind11::module) # libraries that cpp will use, PRIVATE indicates it's only for this file
