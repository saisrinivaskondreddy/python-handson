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
    l = len(arr)
    sortNeed = sortNeeded(arr)
    
    while (sortNeed):
        mid = int(len(arr)/2)
        print ("Inside minimumSwaps, Mid Value is: ", mid)
        for m in range(mid, l):
            print ("calling sort: arr and mid", m)
            #printList(arr)
            swaps = sortByMid(arr, m, swaps)
            #print("After sortByMid")
            printList(arr)
        for m in range(0, mid):
            print ("calling sort-2: arr and mid", mid)
            sorts = sortByMid(arr, m, swaps)
            printList(arr)
        sortNeed = sortNeeded(arr)
    return swaps

def sortNeeded(arr):
    l = len(arr)
    srt = 0
    for i in range(0, l-1):
        if arr[i] > arr[i+1]:
            print ("Need sort")
            srt = 1
    if srt == 0:
        return False
    elif srt == 1:
        return True

def printList(arr):
    print ("Inside printList: ")
    for i in range(0, len(arr)):
        print(arr[i])

def sortByMid(arr, mid, swaps):
    minRightIndex = 0
    maxLeftIndex = 0
    print ("Inside sortByMid, find Max Left! While mid is: ", mid)
    for i in range(0, mid):
        print ("i is: ", i)
        if i == 0:
            maxLeftIndex = i
            print("i, maxLeftIndex and value", i, maxLeftIndex, arr[maxLeftIndex])
        elif i > 0 and i <= mid:
            if arr[maxLeftIndex] < arr[i]:
                maxLeftIndex = i
                print("i,maxLeftIndex and value", i, maxLeftIndex, arr[maxLeftIndex])
    print ("Inside sortByMid, find Min Right : ")
    for j in range(mid, len(arr)):
        print ("Inside sortByMid, find Min Right: ")
        if j == mid:
            minRightIndex = mid
            print("j, minRightIndex and value", j, minRightIndex, arr[minRightIndex])
        elif j < len(arr):
            if arr[minRightIndex] > arr[j]:
                minRightIndex = j
    print ("call Swap")
    if arr[minRightIndex] < arr[maxLeftIndex]:
        # swap
        print ("initiate swap of values at and minRightIndex ")
        #arr[minRightIndex], arr[maxLeftIndex] = arr[maxLeftIndex], arr[minRightIndex]
        temp = arr[minRightIndex]
        arr[minRightIndex] = arr[maxLeftIndex]
        arr[maxLeftIndex] = temp
        swaps += 1
        print ("********Number of swaps are******: ", swaps)
        return swaps
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()

