# Bashier Dahman CS560 

# Assignment 1

import random 
from random import randint
import matplotlib.pyplot as plt 
import timeit
import time



print ('Hello and welcome to my wonderful sorting algorithm program!')

##########################################
# PROMPTING THE USERS FOR ALL THE VALUES #
##########################################

numValues = (int(input("\nPlease enter a size for the array you would like to generate? (Please enter a number greater than 0) \n")))

# if the input is negative or zero throw exception
if numValues <= 0:
    raise ValueError("Please enter a number that is not negative nor zero")

print("\n======Please enter a range you would like the random numbers for your array to be generated in between======")
bottomRange = (int(input("\nBeginning with the bottom range:\n")))
topRange = (int(input("\nLastly the top range:\n")))


# creating variables and setting them to 0 for future use
insertionArray = []
mergeArray = []
number = 0
timeListInsertion = []
timeListMerge = []
timeList = []
sum1 = 0 
sum2 = 0


# code to generate random values inside my array
while number < numValues:
    if number == numValues:
        continue
    else:
        random.seed(number)
        randNum = randint(bottomRange,topRange)
        insertionArray.append(randNum)
        mergeArray.append(randNum)
        number += 1

    
# show the randomly generated array (more useful if array size isn't too large)
if numValues <= 100:
    print("\nHere is your randomly generated array:")
    print(insertionArray)
else:
    print("Your array seems to be too large to print out\n, only when array size is less than or equal to 100 it will print")


# prompt the user to choose whether they would like to graph insertion / merge / or both sorting methods 
print("\n====Please select from the following options: (Numbers only)====")

print("\n1. Insertion Sort")
print("2. Merge Sort")
print("3. Graph both sorts")

selection = (int(input('')))

####################### THESE ARE MY SORTING METHODS #########################

################ MY METHOD FOR INSERTION SORT ##############
def insertion_sort(array): 
    
    global sum1


    for i in range(1, len(array)): 

        #start timing the algorithm
        startInsertion = timeit.default_timer()
        tmp = array[i]
        j = i-1
        while j >= 0 and tmp < array[j] : 
                array[j+1] = array[j] 
                j = j - 1
        array[j+1] = tmp 
        stopInsertion = timeit.default_timer()
        execution_plot1 = stopInsertion - startInsertion
        sum1 += execution_plot1
        # adding the allotted time into my timeList
        timeListInsertion.append(sum1)
        
############# MY METHOD FOR MERGE SORT ###############

def merge_sort(array):
    
    global sum2
    
    
    # as long as the array length is not one, continue with sort
    if len(array) > 1:
        
        
        startMerge = timeit.default_timer()
        # splitting my array in two and creating two more left / right subarrays
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        #Calling my method recursively
        merge_sort(left)
        merge_sort(right)
        
        # setting i and j to 0 so I can traverse my array's
        i = 0
        j = 0
        
        # setting k to 0 so i can iterate through my main array 
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
              array[k] = left[i]
              # increment to the next index 
              i += 1
            else:
                array[k] = right[j]
                j += 1
            # increment to the next index
            k += 1

        # For all the remaining values
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k]=right[j]
            j += 1
            k += 1

        stopMerge = timeit.default_timer()
        execution_plot = stopMerge - startMerge
        sum2 += execution_plot
        timeListMerge.append(sum2)    
##############################################################################


if (selection == 1):
    startInsertion = timeit.default_timer()
    timeListInsertion.append(0)
    insertion_sort(insertionArray)
    stopInsertion = timeit.default_timer()
    execution_time = stopInsertion - startInsertion
    if numValues <= 100:
        print("\nYour new sorted array: ")
        print(insertionArray)
    print("\n Time it took to sort: ")
    print(execution_time)

    # begin plotting my graph #
    plt.plot(insertionArray,timeListInsertion)

    # labelling x and y axis
    plt.xlabel("Numbers")
    plt.ylabel("Total time it takes to sort")

    # titling graph, and inserting a grid for a cleaner look
    plt.title('Insertion Sort Running Time')
    plt.grid(True)
    plt.show()


elif (selection == 2):
    startMerge = timeit.default_timer()
    timeListMerge.append(0) 
    merge_sort(mergeArray)
    stopMerge = timeit.default_timer()
    execution_time = stopMerge - startMerge
    if numValues <= 100:
        print("\nYour new sorted array: ")
        print(mergeArray)
    print("\n Time it took to sort: ")
    print(execution_time)

    # begin plotting my graph #
    plt.plot(mergeArray,timeListMerge)

    # labelling x and y axis
    plt.xlabel("Numbers")
    plt.ylabel("Total time it takes to sort")

    # titling graph, and inserting a grid for a cleaner look
    plt.title('Merge Sort Running Time')
    plt.grid(True)
    plt.show()

elif (selection == 3):

    #I add these two values to make sure my timeList corressponds with my array size
    timeListMerge.append(0) 
    timeListInsertion.append(0)


    #calling my sorting algorithms

    #measuring time it takes to sort
    startMerge = timeit.default_timer()
    merge_sort(mergeArray)
    stopMerge = timeit.default_timer()
    execution_time1 = stopMerge - startMerge
    print("\n Time it took to sort (Using Merge Sort): ")
    print(execution_time1)

    startInsertion = timeit.default_timer()
    insertion_sort(insertionArray)
    stopInsertion = timeit.default_timer()
    execution_time2 = stopInsertion - startInsertion
    print("\n Time it took to sort (Using Insertion Sort): ")
    print(execution_time2)

    
    # begin plotting my insertion sort graph #
    plt.plot(insertionArray,timeListInsertion, label = "Insertion Sort")

    # begin plotting my merge sort graph #
    plt.plot(mergeArray,timeListMerge, label = "Merge Sort")

    # labelling x and y axis
    plt.xlabel("N")
    plt.ylabel("Total time it takes to sort")

    # titling graph, and inserting a grid for a cleaner look
    plt.title('Insertion / Merge Sort Running Time')
    plt.grid(True)
    plt.legend()
    plt.show()