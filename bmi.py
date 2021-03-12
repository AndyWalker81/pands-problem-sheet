# bmi.py
# Week 2 Task
# A program to calculate a person's body mass index (BMI)
# Author: Andrew Walker

# these lines are the inputs 
height = int(input("Enter height in centimetres: "))
weight = int(input("Enter weight in kilograms: "))

# these lines are the outputs
# BMI = kg/m2 where kg is a person's weight in kilograms and m2 is their height in metres squared
# to calculate in centimetres, the height in metres must be divided by 100
# the operator **2 is used to calculate to the power of 2
# the round expression rounds the answer to 2 decimal places
print ("The height is {}cm".format(height))
print ("The weight is {}kg".format(weight))
BMI = (round(weight / (height/100)**2,2))
print ("The person's BMI is: \t{}".format(BMI))   