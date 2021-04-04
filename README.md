# pands-problem-sheet

## Andrew Walker (G00398788@gmit.ie)

### README file for the 20-21: 52167 -- Programming and Scripting Module 

#### Lecturer -- Andrew Beatty (andrew.beatty@gmit.ie)

This file is the submission problem sheet for the module and contains the code, references, and comments for the 8 weekly tasks set over the duration of the course. 

## Week 1

N/A - no submission of code required.

## Week 2: Statements 

*Write a program that calculates somebody's Body Mass Index (BMI). Call the file bmi.py*
*The inputs are the person's height in centimetres and weight in kilograms.*
*The output  is their weight divided by their height in metres squared.*

### Code:
bmi.py

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

*BMI = kg/m^2 where kg is a person's weight in kilograms and m^2 is their height in metres squared*.

As the height was entered in centimetres, height in metres must be divided by 100.
The operator **2 is used to calculate to the power of 2.
The round expression rounds the answer to 2 decimal places.

### References:
1. W3Schools (n.d), *Python round() function* [Online]. Available at https://www.w3schools.com/python/ref_func_round.asp (Accessed 12th March 2021)
2. NHS (2018), *BMI healthy weight calculator* [Online]. Available at https://www.nhs.uk/live-well/healthy-weight/bmi-calculator/ (Accessed 12th March 2021)
3. Canadian Diabetes Association (2021), *How to calculate Body Mass Index* [Online]. Available at https://www.diabetes.ca/managing-my-diabetes/tools---resources/body-mass-index-(bmi)-calculator (Accessed 12th March 2021)


## Week 3: Variables

*Write a program that takes asks a user to input a string and outputs every second letter in reverse order.*

### Code:
secondString.py

```python
txt = input("Please enter a sentence: ")
print (txt[::-2])
```

### Explanation: 
The user is asked to enter a sentence which is saved as a string. According to W3Schools (Reference 1), there is no built in function to reverse a string in Python; the easiest way is to use a slice that steps backward. 

The slice statement [::-2] in the code means start at the end of the string and end at position 0, move with the step -2, negative two, which means two steps backwards. 

The returns every second character in reverse order as per the example given in the task:

*Please enter a sentence: The quick brown fox jumps over the lazy dog.*

*.o zletrv pu o wr cu h*

### References:
1. W3Schools (n.d), *How to Reverse a String in Python* [Online]. Available at https://www.w3schools.com/python/python_howto_reverse_string.asp (Accessed 12th March 2021)
 

## Week 4: Controlling the flow

*Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation.*

*At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.*

*Have the program end if the current value is one.*

### Code:
collatz.py

```python
userNumber = int(input("Please enter a positive integer: "))
print (userNumber,  end = ' ')

while userNumber != 1:
    if ((userNumber % 2) == 0):
        userNumber = int(userNumber / 2 )
    else:
        userNumber = int(userNumber * 3 + 1)
    
    print (userNumber, end = ' ')
```

### Explanation: 

The program first asks the user to input a positive interger which is stored as ```userNumber``` and then printed. The ```end = ' '```python code means that the following items to be printed will be on the same line (by default python's print() function ends with a new line). (Please note - this value will not be printed until the rest of the program has run).

The program then performs a while loop while ```userNumber``` does not equal 1 :
- The modulus operator (%) is used to determine if ```userNumber``` is even or odd.
- If the result of ```userNumber % 2``` is 0 then ```userNumber``` is even and the program will divide ```userNumber``` by 2 and replaces the value of ```userNumber``` with the new value. 
- If the result of ```userNumber % 2``` is not 0 then ```userNumber``` is odd and the program will multiply ```userNumber``` by 3 and add 1. 
- On each step of the loop, the program replaces the orginal ```userNumber``` with the newly calculated value. This figure is printed out. 
- The loop ends when the value ```userNumber``` is equal to 1.
- None of the values for ```userNumber``` print until the loop ends, and each is printed on the same line using ```end = ' '```.

### References:
1. GeeksforGeeks (n.d.), *Python end parameter in print()* [Online]. Available at https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/ (Accessed 18th March 2021)
2. W3Schools (n.d.) *Python While Loops* [Online]. Available at https://www.w3schools.com/python/python_while_loops.asp (Accessed 18th March 2021)
3. W3Schools (n.d.) *Python If ... Else* [Online]. Available at https://www.w3schools.com/python/python_conditions.asp (Accessed 18th March 2021)
4. W3Schools (n.d.) *Python Operators* [Online]. Available at https://www.w3schools.com/python/python_operators.asp (Accessed 18th March 2021)




## Week 5: Data

*Write a program that outputs whether or not today is a weekday.*

### Code:
weekday.py

```python
import datetime

days = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
date = datetime.datetime.now()
today = date.weekday()
todayAsString = days[today]

if today <= 4:
    print ("Today is {} which is a weekday.".format(todayAsString))
else:
    print ("Yay! Today is {} which is the weekend!".format(todayAsString))
```

### Explanation: 

A date in Python is not a data type of its own. Therefore, the program first imports the module ```datetime``` to work with dates as date objects. 

Four variables are defined:

- days: the seven days of the week 
- date: the current date and time in the format ```YYYY-MM-DD 00:00:00.000000```
- today: the ```weekday``` function returns an integer corresponding to day of the week (e.g.: 0 for Monday, 6 for Sunday)
- todayAsString: converts integer to string 

The program then runs an if loop. If the value of the 'today' integer is less than or equal to 4 (i.e. 0 to 4; Monday to Friday) then the program prints a line of code stating that the current day is a weekday. If the value of the integer is not less than or equal to 4 (i.e. 5 or 6; Saturday or Sunday) then the program prints a line of code stating that the current day is the weekend. The program ends after one iteration of the loop.

### References:
1. Pythontic (2020), *Weekday Function In Python* [Online]. Available at https://pythontic.com/datetime/date/weekday (Accessed 30th March 2021)
2. Stack Overflow (n.d.) *Automatically update stored value of datetime.datetime.now()* [Online]. Available at https://stackoverflow.com/questions/12382190/automatically-update-stored-value-of-datetime-datetime-now (Accessed 30th March 2021)
3. W3Schools (n.d.) *Python Datetime* [Online]. Available at https://www.w3schools.com/python/python_datetime.asp (Accessed 30th March 2021)



## Week 6: Functions

*Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.*

*You should create a function called <tt>sqrt</tt> that does this.*

*I am asking you to create your own sqrt function and not to use the built in functions ```x ** .5``` or ```math.sqrt(x)```.*

*This is to demonstrate that you can research and code a process (If you really needed the square root you would use one of the above methods).*

*I suggest that you look at the newton method at estimating square roots.*

*This is a more difficult task than some of the others, but will be marked equally, so only do as much work on this as you feel comfortable.*

### Code:
squareroot.py

```python
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
answer = (sqrt(number, 1))

print ("The estimated square root is: {}".format(round(answer,4)))
```

### Explanation: 

When run, the program asks the user to input a number which can be a float. This number is saved as the variable ```number```. The program calls the function ```sqrt``` which has two arguments: 

1. ```n``` - the number that the user inputted
2. ```count```- initially set at 1

The ```sqrt``` function uses Newton's method:

n = 0.5 * (n + a / n), where:

n is a postive number you want to find square root of

a is a guess that when squared will be close to equalling n 

The program first creates variable ```approx``` by multiplying the inputted number by 0.5. Following the first guess, the result will be saved as variable ```better```which is now used as the new "guess" value. The more iterations are run, the closer the result will be to the value of n until the correct answer is reached. However, once the correct answer is reached, further iterations are uneccessary and will be a waste of processing resources. Therefore, the while loop ends when the values for ```approx``` and ```better``` are equal. 

The function adds 1 to the ```count``` value each time the while loop runs. Once the correct answer is reached, the function prints the number of iterations run and the answer rounded to 4 decimal places.

### References:
1. School for Champions (2012), *Newton's Square Root Approximation* [Online]. Available at https://www.school-for-champions.com/algebra/square_root_approx.htm#.YGMNcz_TVPb (Accessed 30th March 2021)
2. Sıddık Açıl (2018) *Newton Square Root Method in Python* [Online]. Available at https://medium.com/@sddkal/newton-square-root-method-in-python-270853e9185d (Accessed 30th March 2021)
3. W3Schools (n.d.) *Python round() Function* [Online]. Available at https://www.w3schools.com/python/ref_func_round.asp (Accessed 30th March 2021)
4. Geeks for Geeks (2020) *Find root of a number using Newton’s method* [Online]. Available at https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/ (Accessed 30th March 2021)
5. thinkcspy (n.d.) *8.6. Newton’s Method* [Online]. Available at https://runestone.academy/runestone/books/published/thinkcspy/MoreAboutIteration/NewtonsMethod.html (Accessed 30th March 2021)
6. StudentCSP (n.d.) *8.3. Counting with a While Loop* [Online]. Available at https://runestone.academy/runestone/books/published/StudentCSP/CSPWhileAndForLoops/whileCount.html (Accessed 30th March 2021)
7. W3Schools (n.d.) *Python While Loops* [Online]. Available at https://www.w3schools.com/python/python_while_loops.asp (Accessed 30th March 2021)


## Week 7: Files

*Write a program that reads in a text file and outputs the number of e's it contains.*

*The program should take the filename from an argument on the command line.*

### Code:
es.py

```python
filename = sys.argv[1]

with open (filename, "rt") as f:
    data = f.read()
    e = data.count("e")
    E = data.count("E")
    print ("There are {} occurances of 'e' and there are {} occurances of 'E'".format(e, E))
    print ("Therefore, there is a total of {} occurances".format(e + E ) )
```

### Explanation: 

```sys.argv``` is a list, which contains the command-line arguments passed to the script. When a python script is executed with arguments, it is captured by Python and stored in a list called ```sys.argv```. ```sys.argv[0]``` is always the filename/script executed and ```sys.argv[1]``` is the first command line argument passed to the script. Therefore, ```sys.argv[1]``` is used to read from a text file specified in the command line in the format: ```python es.py test.txt```

The program uses Python's ```with open(...) as...``` pattern to open the file specified in the command line and saved as variable ```filename```. ```"rt"```is used to open the file as reading in text mode. 

The program reads the contents of the text file and saves as variable ```data```. The program uses the ```count()``` method which returns the number of times the specified elements (e and E) appear in ```data```. The program prints out the number of occurances of each element, as well as adds the numbers of occurances together and prints the total occurances. 

It was not specified in task instructions whether to include capital E's; a decision made to count and return both e's and E's separately and also return the total. 


### References:
1. School for Champions (2012), *Newton's Square Root Approximation* [Online]. Available at https://www.school-for-champions.com/algebra/square_root_approx.htm#.YGMNcz_TVPb (Accessed 30th March 2021)
2. Sıddık Açıl (2018) *Newton Square Root Method in Python* [Online]. Available at https://medium.com/@sddkal/newton-square-root-method-in-python-270853e9185d (Accessed 30th March 2021)
3. W3Schools (n.d.) *Python round() Function* [Online]. Available at https://www.w3schools.com/python/ref_func_round.asp (Accessed 30th March 2021)
4. Geeks for Geeks (2020) *Find root of a number using Newton’s method* [Online]. Available at https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/ (Accessed 30th March 2021)
5. thinkcspy (n.d.) *8.6. Newton’s Method* [Online]. Available at https://runestone.academy/runestone/books/published/thinkcspy/MoreAboutIteration/NewtonsMethod.html (Accessed 30th March 2021)
6. StudentCSP (n.d.) *8.3. Counting with a While Loop* [Online]. Available at https://runestone.academy/runestone/books/published/StudentCSP/CSPWhileAndForLoops/whileCount.html (Accessed 30th March 2021)
7. W3Schools (n.d.) *Python While Loops* [Online]. Available at https://www.w3schools.com/python/python_while_loops.asp (Accessed 30th March 2021)

https://www.knowledgehut.com/blog/programming/sys-argv-python-examples
https://www.codegrepper.com/code-examples/python/pass+a+file+as+argument+in+python+sys+argv
https://realpython.com/working-with-files-in-python/
https://www.educative.io/edpresso/how-to-open-files-in-python
https://www.programiz.com/python-programming/methods/list/count











## Week 8: Plot 

*Write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.*
*Some marks will be given for making the plot look nice.*

### Code:

```python
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

# add title, axis labels, legend, and show the plot
plt.title("Weekly Task 8")
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.show()
```

### Explanation: 
1. The program first imports the modules numpy and pyplot from matplotlib. 
    - Numpy is a Python library used for working with arrays. 
    - Matplotlib is a library for creating visualizations in Python. 
    - matplotlib.pyplot is a collection of functions that make matplotlib work like MATLAB. Each pyplot function makes some change to a figure: e.g., creates a figure, creates a plotting area in a figure, plots some lines in a plotting area, decorates the plot with labels, etc.
2. The program then defines each of the three functions required for the task in turn: f(x), g(x), and h(x). Each function returns the value stated in the task instruction.
3. After each function, the program uses pyploy to plots the result in a line plot. The result is not shown at each of these stages.
    - Each line is given a colour (red, blue, and green respectively)
    - Each line is given a label 
4. The program then adds a title, axis labels, displays the legend.
5. Finally, the program shows the finished plot.

### References:
1. https://www.w3schools.com/python/numpy_intro.asp 
2. https://matplotlib.org/ 
3. https://pythonprogramming.net/legends-titles-labels-matplotlib-tutorial/
4. https://stackoverflow.com/questions/13544078/python-how-to-create-a-function-e-g-fx-ax2
5. https://pythonspot.com/functions/   
6. https://www.pitt.edu/~naraehan/python2/user_defined_functions.html
