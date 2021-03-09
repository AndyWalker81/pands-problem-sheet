# pands-problem-sheet
pands-problem-sheet

31/1/21
Created pands-problem-sheet repository
Uploaded program for Week 2 task - bmi.py
This program calculates a person's BMI

8/2/21
Uploaded program for Week 3 task - secondString.py
This program asks a user to input a string and outputs every second letter in reverse order. 

16/2/21
Uploaded program for Week 4 task - collatz.py
This program uses flow control to make calculations on a user-inputted number until the number reaches 1.
For future reference: maybe change this program to use lists 

23/2/21
Uploaded program for Week 5 task - weekday.py
A program that outputs whether or not today is a weekday.
reference: https://pythontic.com/datetime/date/weekday accessed 23/2/21
reference: https://stackoverflow.com/questions/12382190/automatically-update-stored-value-of-datetime-datetime-now accessed 23/2/21

2/3/21
Uploaded program for Week 6 task - squareRoot.py
to estimate square root of number

reference: https://www.school-for-champions.com/algebra/square_root_approx.htm#.YD3x8tynxPa
reference: https://medium.com/@sddkal/newton-square-root-method-in-python-270853e9185d
reference: https://www.w3schools.com/python/ref_func_round.asp
reference: https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/

first define function sqrt
the number value is defined later in the code
the more iterations it is possible to be more accurate, although too many is less efficient
Newton's Method: sqrt n = 0.5 * (n + a / n) where:
n is a postive number you want to find square root of
a is your guess that when squared will be close to equalling n 

define function: n is the number inputted by user, and the number iterations to run
a is initially the number inputted by the user - initally this is used as the first guess
each time an iteration is run, the result of the previous guess is used to make the answer for n more accurate

9/3/21
Uploaded program for Week 7 task - es.py
A program that reads in a text file and outputs the number of e's it contains
It was not specified in task instructions whether to include capital E's
Decision made to count and return both e's and E's separately and also return the total
The program takes the filename from an argument on the command line

