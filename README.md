# pands-problem-sheet

## Andrew Walker 
### (G00398788@gmit.ie)

README file for the 20-21: 52167 -- Programming and Scripting Module 
Lecturer -- Andrew Beatty (andrew.beatty@gmit.ie)

This file is the submission problem sheet for the module and contains the code, references, and comments for the 8 weekly tasks set over the duration of the course. 

## Week 1

N/A - no submission of code required.

## Week 2: Statements - Toggle

*Write a program that calculates somebody's Body Mass Index (BMI). Call the file bmi.py*
*The inputs are the person's height in centimetres and weight in kilograms.*
*The output  is their weight divided by their height in metres squared.*

### Code:

```python
height = int(input("Enter height in centimetres: "))
weight = int(input("Enter weight in kilograms: "))

print ("The height is {}cm".format(height))
print ("The weight is {}kg".format(weight))

BMI = (round(weight / (height/100)**2,2))

print ("The person's BMI is: \t{}".format(BMI))  
```

### Explanation: 
The user is first asked to enter height in centimetres and weight in kilgrams as integers. The program then outputs the values entered along with the units for height and weight. 

The calculation for BMI is then performed, based upon the values for height and weight previously entered. 
*BMI = kg/m^2 where kg is a person's weight in kilograms and m^2 is their height in metres squared*
As the height was entered in centimetres, height in metres must be divided by 100
The operator **2 is used to calculate to the power of 2
The round expression rounds the answer to 2 decimal places

### References:
W3Schools, Python round() function, W3Schools, viewed 12th March 2021, <https://www.w3schools.com/python/ref_func_round.asp>
NHS, BMI healthy weight calculator, NHS, viewed 12th March 2021, <https://www.nhs.uk/live-well/healthy-weight/bmi-calculator/>
Canadian Diabetes Association, How to calculate Body Mass Index, Canadian Diabetes Association, viewed 12th March 2021, <https://www.diabetes.ca/managing-my-diabetes/tools---resources/body-mass-index-(bmi)-calculator>











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

