# see example.cpp for using c++ methods in python
import example
test = example.add(1, 1)
print(test)
# add function from cpp is adding 2 numbers together. therefore output should be 2

# see custom.cpp for using python class in c++, vice versa is possible if you only use c++ method to interate with the
# c++ objects
import custom
from custom_object import MyObject

# Create a list of MyObject instances
objects = [MyObject(i) for i in range(5)]

# Pass the list to the C++ function
custom.process_list(objects)
