#!/usr/bin/python
# Quicksort in python

#import datetime & start counting 
from datetime import datetime
start_time = datetime.now()

import argparse
import sys

from qs_functions import *

# Check to see that inputs have been provided:
if len(sys.argv)==1:
    print "** ERROR: Quicksort requires a list of integers"
    usage()

# Print intro message
print "\nWelcome to Quicksort!"

# Parse arguments
array=[] #instantiate array
arr_length=0
for arg in sys.argv[1:]: # iterate through inputs
    # ensure the inputs are integers
    try: 
        arg=int(arg) 
    except:
        print "** ERROR: Quicksort requires a list of integers"
        usage()
    # add the inputs to the array
    array.append(arg) 
    arr_length=arr_length+1

print "\nYou asked to sort:" 
# print the array
for i in range(arr_length):
  print ("%d" %array[i]),

print "\nSorted array is:" 
quickSort(array,0,arr_length-1) 
for i in range(arr_length): 
    print ("%d" %array[i]),

runtime=get_millis(start_time)
#print ("Quicksort sorted %d elements in %d seconds" %arr_length %ms)

print_summary(arr_length, runtime)


