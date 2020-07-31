# Bashier Dahman CS560 

# PROGRAM TO SOLVE MAXIMUM SUBARRAY PROBLEM #
# RECURSIVELY AND WITH BRUTE FORCE #
# AND PLOTTING THE TIME IT TAKES # 

import random 
from random import randint
from sys import maxsize
import timeit
import matplotlib.pyplot as plt 
import math
import time

print ('Hello and welcome to the Brute Force/ Recursive Algorithms for Maximum SubArray Problems!')

##########################################
# PROMPTING THE USERS FOR ALL THE VALUES #
##########################################

print("\n======Due to the professors instructions... the array size generated is 1000======")
print("=======================AND WITH VALUES OF -50 THROUGH 50==========================")


# creating variables and setting them to 0 for future use
bruteArray = []
recursiveArray = []
timeListBrute = []
timeListRecursive = []

number = 0
max_so_far = 0
max_ending_here = 0
sum2= 0
sum3= 0
test = 0
elements = []

# # code to generate random values inside my array of fixed size 1000
# while number <1000:
#     # random.seed(number)
#     randNum = randint(bottomRange,topRange)
#     bruteArray.append(randNum)
#     recursiveArray.append(randNum)
#     number += 1

# while test < 1000:
#     plotArray.append(test)
#     test += 1




################ MY METHOD FOR FINDING MAXIMUM SUB ARRAY ##############    


def max_subarr_brute(input_array):
    
    global sum2 

    global_max = 0
    indices = []

    for x in range(0,len(input_array)):
        for j in range(len(input_array)+1):
            if input_array[x:j]:
                current_max = sum(input_array[x:j])

                if current_max > global_max:
                    global_max = current_max
                    indices.append((x, j-1))      


    return global_max

#############################################################

def brute_time(input_array):
    global sum2 

    n = len(input_array)
    maximum = 0
    for i in range(n):
        current = 0
        for j in range(n):
            current += input_array[j]
            if current > maximum:
                maximum = current
    return maximum          


##########################################################
def BRUTE_FORCE_FIND_MAX(A, low, high):


    max_profit = 0
    max_left = 0
    max_right = 0
    i = low
    j = i +1
    for i in range((high-1)):
        for j in range(high):
            profit = A[j] - A[i]
            if profit > max_profit:
                max_left = i
                max_right = j
                max_profit=profit


    return (max_left, max_right, max_profit)
    


###############################################################

def FIND_MAX_CROSSING_SUBARRAY(A, low, mid, high):
    left_sum = -math.inf
    sum = 0
    for i in range(mid, low-1, -1):
        sum = sum + A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    right_sum = -math.inf
    sum = 0
    for j in range(mid+1, high+1):
        sum = sum + A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    return (max_left, max_right, left_sum + right_sum)

###############################################################

def FIND_MAXIMUM_SUBARRAY(A, low, high):
    

    if (high == low):
        return (low, high, A[low])
    else: 
        mid = (𝑙𝑜𝑤 + ℎ𝑖𝑔ℎ) // 2
        (left_low, left_high, left_sum) = FIND_MAXIMUM_SUBARRAY(A, low, mid)
        (right_low, right_high, right_sum) = FIND_MAXIMUM_SUBARRAY(A, mid + 1, high)
        (cross_low, cross_high, cross_sum) =  FIND_MAX_CROSSING_SUBARRAY(A, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else: 
            return (cross_low, cross_high, cross_sum)


###############################################################

def maxCrossingSum(arr, l, m, h) : 
      
    # Include elements on left of mid. 
    sm = 0; left_sum = -math.inf
      
    for i in range(m, l-1, -1) : 
        sm = sm + arr[i] 
          
        if (sm > left_sum) : 
            left_sum = sm 
      
      
    # Include elements on right of mid 
    sm = 0; right_sum = -math.inf
    for i in range(m + 1, h + 1) : 
        sm = sm + arr[i] 
          
        if (sm > right_sum): 
            right_sum = sm 
      
  
    # Return sum of elements on left and right of mid 
    return left_sum + right_sum; 
  
 
def maxSubArraySum(A, low, high) : 

    # if there only exists one element return it
    if (low == high) : 
        return A[low] 
  
    
    # Find middle point 
    mid = (low + high) // 2
     


    return max(maxSubArraySum(A, low, mid), 
               maxSubArraySum(A, mid+1, high), 
               maxCrossingSum(A, low, mid, high)) 


def recursive_time():
    global sum3

    startRecursive = timeit.default_timer()
    n= len(recursiveArray)
    (maxSubArraySum(recursiveArray,-1,n-1))
    # timing my recursive algorithms
    stopRecursive = timeit.default_timer()
    execution_plot2 = stopRecursive - startRecursive
    sum3 += execution_plot2
    # adding the allotted time into my timeList
    return timeListRecursive.append(sum3)   

###############################################################


print("\nCurrently generating values for my arrays, performing my methods, AND plugging them into my lists for plotting")
print("This may take a few seconds, please be patient...")

for i in range(1,1001):
    # random.seed(number)
    randNum = randint(-50,50)
    bruteArray.insert(number,randNum)
    recursiveArray.insert(number,randNum)

n = len(bruteArray)
r = len(recursiveArray)
for i in range(1, n+1):
    elements.append(i)
    startBrute = time.perf_counter()
    (BRUTE_FORCE_FIND_MAX(bruteArray[:i],0,i))
    timeListBrute.append(time.perf_counter() - startBrute)

    startRecursive=time.perf_counter()
    maxSubArraySum(recursiveArray[:i],0,i-1)
    timeListRecursive.append(time.perf_counter()-startRecursive)    

print("\nYou're maximum subarray sum (BRUTE FORCE): ")
print(max_subarr_brute(bruteArray))


print("\nRecursive Max Subarray: ")
n= len(recursiveArray)
print(maxSubArraySum(recursiveArray,-1,n-1))

# begin plotting my brute force graph #
plt.plot(elements,timeListRecursive, label = "Recursive Method")
# begin plotting my brute force graph #
plt.plot(elements,timeListBrute, label = "Brute Force")

# labelling x and y axis
plt.xlabel("N")
plt.ylabel("Time")

# titling graph, and inserting a grid for a cleaner look
plt.title('Brute Force / Recursive Running Time')
plt.grid(True)
plt.legend()

plt.show()

