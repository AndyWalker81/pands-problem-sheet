# squareRoot.py
# to estimate square root of number
# Author: Andy Walker

# reference: https://www.school-for-champions.com/algebra/square_root_approx.htm#.YD3x8tynxPa
# reference: https://medium.com/@sddkal/newton-square-root-method-in-python-270853e9185d
# reference: https://www.w3schools.com/python/ref_func_round.asp
# reference: https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/

# first define function sqrt
# the number value is defined later in the code
# the more iterations it is possible to be more accurate, although too many is less efficient
# Newton's Method: sqrt n = 0.5 * (n + a / n) where:
# n is a postive number you want to find square root of
# a is your guess that when squared will be close to equalling n 

# define function: n is the number inputted by user, and the number iterations to run
# a is initially the number inputted by the user - initally this is used as the first guess
# each time an iteration is run, the result of the previous guess is used to make the answer for n more accurate
def sqrt(n, iterations = 1000):
    a = float(n)
    for i in range(iterations):
        n = 0.5 * (n + a / n)
    return n

number = float(input("Please enter a number: "))

#runs the function
answer = (sqrt(number))
# rounds the result to 1 decimal place
print ("The estimated square root is: {}".format(round(answer,1)))