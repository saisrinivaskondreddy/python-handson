#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'transformSentence' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def transformSentence(sentence):
    # Write your code here
    for i in range(len(sentence)):
        if i == 0:
            continue
        elif i >= 1 and sentence[i-1] > sentence[i]:
            sentence[i].upper()
        elif i >=1 and sentence[i-1] < sentence[i]:
            sentence[i].lower()
    print (sentence)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = transformSentence(sentence)

    fptr.write(result + '\n')

    fptr.close()

