#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps = 0
    mid = 0
    #while (mid < len(arr)):    
    for i in range(0, len(arr)):
        if arr[i] != i+1 and arr[i] > arr[arr[i]-1]:
            temp = 0
            print ("value of i: ", i)
            print ("going to swap arr[i] and arr[arr[i]-1]", arr[i], arr[arr[i]-1])
            #arr[i], arr[arr[i]-1] = arr[arr[i]-1], arr[i]
            temp = arr[i]
            arr[i] = arr[arr[i]-1]
            print (arr[i])
            arr[arr[i]-1] = temp
            print (arr[arr[i]-1])
            print ("after swap arr[i] and arr[arr[i]-1]", arr[i], arr[arr[i]-1])
            swaps += 1
            #printList(arr)
            #print (arr[i], arr[arr[i]-1])
            print ("list after swap")
            for i in range(0, len(arr)):
                print(arr[i])
    return swaps
        
def printList(arr):
    print ("print the list after one swap: ")
    for i in range(len(arr)):
        print(arr[i])
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
