# squareRoot.py
# to estimate square root of number
# Author: Andy Walker

# reference: https://www.school-for-champions.com/algebra/square_root_approx.htm#.YD3x8tynxPa
# reference: https://medium.com/@sddkal/newton-square-root-method-in-python-270853e9185d
# reference: https://www.w3schools.com/python/ref_func_round.asp
# reference: https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
# reference: https://runestone.academy/runestone/books/published/thinkcspy/MoreAboutIteration/NewtonsMethod.html
# reference: https://runestone.academy/runestone/books/published/StudentCSP/CSPWhileAndForLoops/whileCount.html
# reference: https://www.w3schools.com/python/python_while_loops.asp

# first define function sqrt
# the number value is defined later in the code
# the more iterations it is possible to be more accurate, although too many is less efficient
# Newton's Method: sqrt n = 0.5 * (n + a / n) where:
# n is a postive number you want to find square root of
# a is your guess that when squared will be close to equalling n 

# define function: n is the number inputted by user and a count value
# a is initially the number inputted by the user - initally this is used as the first guess
# the code takes this number and halves it as a first approximate guess
# the code also takes this number and performes Newton's Method using the approximate guess
# if the two guesses do not match then the loop runs again using the latest approximate guess
# each time an iteration is run, the result of the previous guess is used to make the answer for n more accurate
# a counter tracks the number of iterations
# once the guess is not able to be improved (when the two guess values match), the loop ends
# the program prints the number of iterations run and the square root to 4 decimal places

def sqrt(n, count):
    a = float(n)
    approx = 0.5 * a
    better = 0.5 * (approx + n/approx)
    while better != approx: 
        approx = better
        better = 0.5 * (approx + n/approx)
        count = count + 1
    print ("The number of iterations is: {}".format(count))
    return approx
    
number = float(input("Please enter a number: "))

#runs the function
answer = (sqrt(number, 1))

# rounds the result to 4 decimal places
print ("The estimated square root is: {}".format(round(answer,4)))


