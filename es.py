# es.py
# Weekly Task 7
# A program that reads in a text file and outputs the number of e's it contains
# It was not specified in task instructions whether to include capital E's
# Decision made to count and return both e's and E's separately and also return the total
# The program takes the filename from an argument on the command line
# Author: Andy Walker



# import sys module
import sys

# sys.argv is a list, which contains the command-line arguments passed to the script
# When a python script is executed with arguments, it is captured by Python and stored in a list called sys.argv. 
# sys.argv[0] is always the filename/script executed and sys.argv[1] is the first command line argument passed to the script
# Therfore, sys.argv[1] is used to read from a text file specified in the command line in the format: python es.py test.txt
filename = sys.argv[1]

# “with open(…) as …” pattern used to open file
with open (filename, "rt") as f:
    data = f.read()
    e = data.count("e")
    E = data.count("E")
    print ("There are {} occurances of 'e' and there are {} occurances of 'E'".format(e, E))
    print ("Therefore, there is a total of {} occurances".format(e + E ) )

# References: 
# https://www.knowledgehut.com/blog/programming/sys-argv-python-examples
# https://www.codegrepper.com/code-examples/python/pass+a+file+as+argument+in+python+sys+argv
# https://realpython.com/working-with-files-in-python/
# https://www.educative.io/edpresso/how-to-open-files-in-python
# https://www.programiz.com/python-programming/methods/list/count