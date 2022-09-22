#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps = 0
    #mid = 0
    while (listSorted(arr) == False):
        for i in range(0, len(arr)):
            if arr[i] != i+1:
                j = arr[i]-1
                if i < j and arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
                    swaps += 1
                elif i > j and arr[i] < arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
                    swaps += 1
    return swaps

def listSorted(arr):
    for i in range(0, len(arr)):
        if arr[i] != i+1:
            return False
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()

