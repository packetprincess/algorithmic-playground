#!/usr/bin/python

from datetime import datetime

from datetime import timedelta
# returns the elapsed milliseconds since the start of the program
def get_millis(start_time):
   dt = datetime.now() - start_time
   ms = (dt.days * 24 * 60 * 60 + dt.seconds) * 1000 +          dt.microseconds / 1000.0
   return ms

# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot 
def partition(array,mindex,maxdex): 
    i = (mindex-1)         # index of smaller element 
    pivot = array[maxdex]     # pivot 
  
    for j in range(mindex,maxdex): 
  
        # If current element is smaller than or 
        # equal to pivot 
        if   array[j] <= pivot: 
          
            # increment index of smaller element 
            i = i+1 
            array[i],array[j] = array[j],array[i] 
  
    array[i+1],array[maxdex] = array[maxdex],array[i+1] 
    return(i+1) 
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
def quickSort(array,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        part_index = partition(array,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(array, low, part_index-1) 
        quickSort(array, part_index+1, high) 
