# This is a sample Python script.
import math
import sys
from timeit import Timer
from statistics import mean
from tqdm import tqdm


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    def add(x, y):
        return x + y


    def sub(x, y):
        return x - y


    def mul(x, y):
        return x * y


    def div(x, y):
        return x / y


    def foo1(oper, a, b):
        return funcs[oper](a, b)


    def foo2(oper, a, b):
        if oper == 'add':
            return add(a, b)
        elif oper == 'sub':
            return sub(a, b)
        elif oper == 'mul':
            return mul(a, b)
        elif oper == "1":
            return div(a, b)
        elif oper == "2":
            return div(a, b)
        elif oper == "3":
            return div(a, b)
        elif oper == "4":
            return div(a, b)
        elif oper == "5":
            return div(a, b)
        elif oper == "6":
            return div(a, b)
        elif oper == "7":
            return div(a, b)
        elif oper == "8":
            return div(a, b)
        elif oper == "9":
            return div(a, b)
        elif oper == "10":
            return div(a, b)
        else:
            return div(a, b)

    def foo3(oper, a, b):
        subfuncs[oper](a, b)

    def foo4(oper, a, b):
        subfuncs[alis[oper]](a, b)


    funcs = {'add': lambda x, y: x + y,
             'sub': lambda x, y: x - y,
             'mul': lambda x, y: x * y,
             '1': lambda x, y: x * y,
             '2': lambda x, y: x * y,
             '3': lambda x, y: x * y,
             '4': lambda x, y: x * y,
             '5': lambda x, y: x * y,
             '6': lambda x, y: x * y,
             '7': lambda x, y: x * y,
             '8': lambda x, y: x * y,
             '9': lambda x, y: x * y,
             '10': lambda x, y: x * y,
             'div': lambda x, y: x / y}

    subfuncs = {'add': add,
                'sub': sub,
                'mul': mul,
                '1': mul,
                '2': mul,
                '3': mul,
                '4': mul,
                '5': mul,
                '6': mul,
                '7': mul,
                '8': mul,
                '9': mul,
                '10': mul,
                'div': div}
    alis = {'ad': 'add',
            'su': 'sub',
            'mu': 'mul',
            'a': '1',
            'b': '2',
            'c': '3',
            'd': '4',
            'e': '5',
            'f': '6',
            'g': '7',
            'h': '8',
            'i': '9',
            'j': '10',
            'di': 'div'}

    times_to_run = 1000000
    ave1 = []
    ave2 = []
    ave3 = []
    ave4 = []
    for i in tqdm(range(100)):
        t1 = Timer("foo1('div', 3, 2)", "from __main__ import foo1")
        t2 = Timer("foo2('div', 3, 2)", "from __main__ import foo2")
        t3 = Timer("foo3('div', 3, 2)", "from __main__ import foo3")
        t4 = Timer("foo4('di', 3, 2)", "from __main__ import foo4")
        tot1 = t1.timeit(times_to_run)
        tot2 = t2.timeit(times_to_run)
        tot3 = t3.timeit(times_to_run)
        tot4 = t4.timeit(times_to_run)
        ave1.append(tot1)
        ave2.append(tot2)
        ave3.append(tot3)
        ave4.append(tot4)

    print("Total Time for foo1 is: {:4.2f}".format(sum(ave1)))
    print("Total Time for foo2 is: {:4.2f}".format(sum(ave2)))
    print("Total Time for foo3 is: {:4.2f}".format(sum(ave3)))
    print("Total Time for foo4 is: {:4.2f}".format(sum(ave4)))
    print("Time for foo1 is: {:4.2f}".format(mean(ave1)))
    print("Time for foo2 is: {:4.2f}".format(mean(ave2)))
    print("Time for foo3 is: {:4.2f}".format(mean(ave3)))
    print("Time for foo4 is: {:4.2f}".format(mean(ave4)))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
