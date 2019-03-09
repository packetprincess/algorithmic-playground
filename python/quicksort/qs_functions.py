#!/usr/bin/python

from datetime import datetime
from datetime import timedelta

# returns the elapsed milliseconds since the start of the program
def get_millis(start_time):
   dt = datetime.now() - start_time
   ms = (dt.days * 24 * 60 * 60 + dt.seconds) * 1000 +          dt.microseconds / 1000.0
   return ms

# Usage message
def usage():
    print "Usage: quicksort.py <list of integers to sort>"
    print "\nProgram will return quicksort-sorted list, number of elements and time to run."
    sys.exit()


def partition(array,mindex,maxdex): 
    i = (mindex-1)         # index of smaller element 
    pivot = array[maxdex]     # pivot 
  
    for j in range(mindex,maxdex): 
  
        if   array[j] <= pivot: 
          
            i = i+1 
            array[i],array[j] = array[j],array[i] 
  
    array[i+1],array[maxdex] = array[maxdex],array[i+1] 
    return(i+1) 
  

# Function to do Quick sort 
def quickSort(array,low,high): 
    if low < high: 
  
        part_index = partition(array,low,high) 
  
        quickSort(array, low, part_index-1) 
        quickSort(array, part_index+1, high) 
        
def print_summary(arr_length, runtime):
    print "\n"
    print ("Quicksort processed %d elements" %arr_length),
    print ("in %d ms" %runtime),
    obj_per_milli=float(arr_length)/float(runtime)
    print ("\nElements per ms: %f" %obj_per_milli)
    milli_per_obj=float(runtime)/float(arr_length)
    print ("\nms per element: %f" %milli_per_obj)
    print "\n"
