# plotask.py
# Week 8 Task
# A program that displays a plot of the functions f(x)=x, g(x)=x^2 and h(x)=x^3 in the range [0, 4] on the one set of axes
# Author: Andy Walker

# https://stackoverflow.com/questions/13544078/python-how-to-create-a-function-e-g-fx-ax2
# https://pythonspot.com/functions/   
# https://www.pitt.edu/~naraehan/python2/user_defined_functions.html
# https://pythonprogramming.net/legends-titles-labels-matplotlib-tutorial/
# https://www.w3schools.com/python/numpy_intro.asp
# https://matplotlib.org/

# import modules 
import numpy as np
import matplotlib.pyplot as plt

# set absolute variables
x = np.array(range(0,4))
y = np.array(range(0,4))

# define first function and plot
def f(x):
    return x
plt.plot(y, f(x), "r", label = "f(x)")

# define second function and plot
def g(x):
    return x ** 2
plt.plot(y, g(x), "b", label = "g(x)")

# define third function and plot
def h(x):
    return x ** 3
plt.plot(y, h(x),  "g", label = "h(x)")

# add title, labels, legend, show the plot, and save the plot as .png file 
plt.title("Weekly Task 8")
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.savefig("plottask.png")
plt.show()
