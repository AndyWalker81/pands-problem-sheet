# plotask.py
# Week 8 Task
# A program that displays a plot of the functions f(x)=x, g(x)=x^2 and h(x)=x^3 in the range [0, 4] on the one set of axes
# Author: Andy Walker

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