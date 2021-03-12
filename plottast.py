# plotask.py
# Week 8 Task
# A program that displays a plot of the functions f(x)=x, g(x)=x^2 and h(x)=x^3 in the range [0, 4] on the one set of axes
# Author: Andy Walker

# https://stackoverflow.com/questions/13544078/python-how-to-create-a-function-e-g-fx-ax2
# https://pythonspot.com/functions/   
# https://www.pitt.edu/~naraehan/python2/user_defined_functions.html

import numpy as np
import matplotlib.pyplot as plt

# set absolute variables
x = np.array(range(0,4))
y = np.array(range(0,4))

def f(x):
    return x

plt.plot(f(x), y, "r")
#print (f(x))

def g(x):
    return x ** 2

plt.plot(g(x), y, "b")
#print (g(x))

def h(x):
    return x ** 3

plt.plot(h(x), y, "g")
#print (h(x))

plt.show()