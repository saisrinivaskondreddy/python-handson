#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    bribe = 0
    #print (type(q))
    #print (type(q[0]))
    for i in range(len(q)):
        if q[i] == i+1:
            # no bribe
            bribe = bribe 
        elif q[i] == i+2:
            bribe += 1
        elif q[i] == i+3:
            bribe += 2
        elif q[i] >= i+4:
            print ("Too chaotic")
            return
    print (bribe)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

