#!/usr/bin/python
# Quicksort in python

#import datetime
from datetime import datetime


start_time = datetime.now()

import argparse
import sys

from qs_functions import *

# Usage message
def usage():
    print "Usage: quicksort.py <list of integers to sort>"
    print "\nProgram will return quicksort-sorted list, number of elements, time to run, and complexity analysis."
    sys.exit()

# Check to see that inputs have been provided:
if len(sys.argv)==1:
    print "** ERROR: Quicksort requires a list of integers"
    usage()

# Print intro message
print "\nWelcome to Quicksort!"

# Parse arguments
arr=[] #instantiate array
arr_length=0
for arg in sys.argv[1:]: # iterate through inputs
    # ensure the inputs are integers
    try: 
        arg=int(arg) 
    except:
        print "** ERROR: Quicksort requires a list of integers"
        usage()
    # add the inputs to the array
    arr.append(arg) 
    arr_length=arr_length+1

print "\nYou asked to sort:" 
# print the array
for i in range(arr_length):
  print ("%d" %arr[i]),
# Driver code to test above 
#arr = [10, 7, 8, 9, 1, 5] 

print ""
quickSort(arr,0,arr_length-1) 
print "\nSorted array is:" 
for i in range(arr_length): 
    print ("%d" %arr[i]),

runtime=get_millis(start_time)
#print ("Quicksort sorted %d elements in %d seconds" %arr_length %ms)
print "\n"
print ("Quicksort processed %d elements" %arr_length),
print ("in %d ms" %runtime),
print "\n"
