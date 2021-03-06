# collatz.py
# Week 4 task
# A program that asks the user to input any positive integer and outputs the successive values of the following calculation.
# At each step it calculates the next value by taking the current value
# If it is even, it divides it by two
# If it is odd, it multiplies it by three and add one.
# The program ends if the value is one.
# Author: Andy Walker

# Input the number
userNumber = int(input("Please enter a positive integer: "))

# Prints the inputted number 
# This will not show until the rest of the code runs
# The end key avoids a new line
# Reference: https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/

print (userNumber,  end = ' ')

# The program will run until the userNumber equals 1
while userNumber != 1:
    if ((userNumber % 2) == 0):
        userNumber = int(userNumber / 2 )
    else:
        userNumber = int(userNumber * 3 + 1)

    # It will then print out the rest of the numbers on the same line as the original number

    print (userNumber, end = ' ')
        