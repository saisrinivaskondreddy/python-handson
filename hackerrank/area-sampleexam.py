#!/bin/python3

import math
import os
import random
import re
import sys


class Rectangle:
    
    def __init__(self, a, b):
        self.l = a
        self.b = b
    def area(self):
        area = self.l * self.b
        print (area)
        return area

class Circle:
    
    def __init__(self, r1):
        self.r = r1
    def area(self):
        area = math.pi * self.r**2
        print (area)
        return area

if __name__ == '__main__':  
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input("Enter number of queries: "))
    queries = []
    for _ in range(q):
        args = input("share and sides: ").split()
        shape_name, params = args[0], tuple(map(int, args[1:]))
        if shape_name == "rectangle":
            a, b = params[0], params[1]
            shape = Rectangle(a, b)
        elif shape_name == "circle":
            r = params[0]
            shape = Circle(r)
        else:
            raise ValueError("invalid shape type")
        fptr.write("%.2f\n" % shape.area())
    fptr.close()

