# weekday.py
# Weekly Task 05
# A program that outputs whether or not today is a weekday.
# Author: Andy Walker

# reference: https://pythontic.com/datetime/date/weekday accessed 23/2/21
# reference: https://stackoverflow.com/questions/12382190/automatically-update-stored-value-of-datetime-datetime-now accessed 23/2/21

# import Python's datetime module

import datetime

# days of the week as a tuple
days = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")

# automatically set the correct date
date = datetime.datetime.now()

# today as an integer
today = date.weekday()

# convert integer to string taking information from tuple of days of  the week
todayAsString = days[today]

# if the day of the week is one of the first 5 days in tuple print that it is a weekday.
# if the day of the week is not one of the first 5 days then it prints that is is a weekend.
if today in range (0,5):
    print ("Today is {} which is a weekday.".format(todayAsString))
else:
    print ("Yay! Today is {} which is the weekend!".format(todayAsString))
